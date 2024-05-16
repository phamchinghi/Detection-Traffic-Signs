from per.dataaccess import Crawling

def getImages(url):
    Crawling.download_images(url)


if __name__ == '__main__':
    url = "https://en.wikipedia.org/wiki/Road_signs_in_Vietnam"
    getImages(url)