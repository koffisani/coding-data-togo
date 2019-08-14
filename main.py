import scraper
from scrapy.crawler import CrawlerProcess
from db import Db
import matplotlib.pyplot as plt

langages = {
    'javascript': 0,
    'python': 0,
    'java': 0,
    'php': 0,
    'ruby': 0,
    'typescript': 0,
    'csharp': 0,
    'c++': 0,
    'css': 0,
    'html': 0,
}

plateformes = {
    'nodejs': 0,
    'android': 0,
    'xamarin': 0,
}

frameworks = {
    'react': 0,
    'angular': 0,
    'ionic': 0,
    'laravel': 0,
    'symfony': 0,
    'bootstrap': 0,
    'vue': 0,
    'django': 0,
    'flask': 0,
    'rails': 0,
    'jquery': 0,
    'vuejs': 0,
}

outils = {
    'git': 0,
    'github': 0,
    'gitlab': 0,
    'circle': 0,
    'travis': 0,
    'bitbucket': 0,
}

def analyse():
    select = "SELECT * FROM scraped"
    db = Db.getInstance()
    cursor = db.conn.cursor()
    data = cursor.execute(select)


    for row in data:
        # Traitement
        for key in langages:
            if key.lower() in row[2].lower():
                langages[key] += 1

        for key in frameworks:
            if key.lower() in row[2].lower():
                frameworks[key] += 1

        for key in outils:
            if key.lower() in row[2].lower():
                outils[key] += 1

        for key in plateformes:
            if key.lower() in row[2].lower():
                plateformes[key] += 1
        
    

if __name__ == '__main__':
    
    process = CrawlerProcess()

    process.crawl(scraper.Scrap)
    process.start()

    analyse()
    print (langages)
    print (outils)
    print (frameworks)
    print (plateformes)

    lngg = plt.figure(1)
    plt.barh(list(langages.keys()), langages.values())
    plt.title("Langages de programmation")
    plt.savefig("output/langages.png")

    frmw = plt.figure(2)
    plt.barh(list(frameworks.keys()), frameworks.values())
    plt.title("Frameworks")
    plt.savefig("output/frameworks.png")

    pltf = plt.figure(3)
    plt.barh(list(plateformes.keys()), plateformes.values())
    plt.title("Plateformes")
    plt.savefig("output/platformes.png")

    outls = plt.figure(4)
    plt.barh(list(outils.keys()), outils.values())
    plt.title("Outils de développements")
    plt.savefig("output/outils.png")
