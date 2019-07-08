import scrapy 
from db import Db

class Scrap(scrapy.Spider):
    name = "togo_coding_job_data"

    db = Db()

    def start_requests(self):
        yield scrapy.Request('https://www.emploi.tg/recherche-jobs-togo/?f%5B0%5D=im_field_offre_metiers:31', self.crawl_emploi_tg)
        '''
        yield scrapy.Request('https://www.rmo-jobcenter.com/fr/togo/offres-emploi/ntic.html', self.crawl)
        yield scrapy.Request('http://www.lucreatif.com/nouvelle_offre_d_emploi.html', self.crawl)
        yield scrapy.Request('https://anpetogo.org/espace-chercheur-d-emploi/nos-offres-demplois/?ajax_filter=true&sort-by=recent&sector_cat=developpement-informatique&posted=all', self.crawl)
        yield scrapy.Request('https://emploitogo.com/jobs/?layout=list&post_type=jobboard-post-jobs&specialism-filters%5B%5D=58', self.crawl)
        '''

    '''
    Crawling data by url : emploi.tg
    '''
    def crawl_emploi_tg (self, response):
        SITE_URL = 'https://www.emploi.tg'
        SET_SELECTOR = '.job-description-wrapper'
        for search_result in response.css(SET_SELECTOR):
            HREF_SELECTOR = 'a ::attr(href)'
            
            detail_page_url = SITE_URL + search_result.css(HREF_SELECTOR).extract_first()
            # Deep into the job description
            yield scrapy.Request(
                response.urljoin(detail_page_url),
                callback = self.detail_page_emploi_tg,
            )
    
    
    '''
    Crawling data by url : 
    '''
    def crawl (self, response):
        SET_SELECTOR = ''
        self.logger.info('A response from %s', response.url)

    def detail_page_emploi_tg (self, response):
        DETAILS_SELECTOR = '.content ul li ::text'
        SITE_URL = 'https://www.emploi.tg'
        details = response.css(DETAILS_SELECTOR)
        if details :
            #print ('Détail ', details.extract(), sep='=>')
            #print (type(details.extract()))
            text_list = details.extract()
            for item in text_list:
                if not item :
                     self.db.c.execute("INSERT INTO scraped (site, url, content) VALUES ( ?, ?, ?) ",  (SITE_URL, '', item))
            self.db.conn.commit()
            #self.db.conn.close()

    def closed(self, reason):
        self.db.close_connection()