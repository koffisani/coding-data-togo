import scraper
from scrapy.crawler import CrawlerProcess

if __name__ == '__main__':
    print("Yes")

    process = CrawlerProcess()

    process.crawl(scraper.Scrap)
    process.start()

