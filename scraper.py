import scrapy 

class Scrap(scrapy.Spider):
    name = "togo_coding_job_data"
    start_urls = [
        'https://www.emploi.tg/recherche-jobs-togo/?f%5B0%5D=im_field_offre_metiers%3A31',
        'https://www.rmo-jobcenter.com/fr/togo/offres-emploi/ntic.html',
        'http://www.lucreatif.com/nouvelle_offre_d_emploi.html',
        'https://anpetogo.org/espace-chercheur-d-emploi/nos-offres-demplois/?ajax_filter=true&sort-by=recent&sector_cat=developpement-informatique&posted=all',
        'https://emploitogo.com/jobs/?layout=list&post_type=jobboard-post-jobs&specialism-filters%5B%5D=58',
    ]

    def parse (self, response):
        SET_SELECTOR = ''