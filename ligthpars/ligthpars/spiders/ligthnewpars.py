import scrapy


class LigthnewparsSpider(scrapy.Spider):
    name = "ligthnewpars"
    allowed_domains = ["https://divan.ru"]
    start_urls = ["https://www.divan.ru/category/podvesnye-svetilniki"]

    def parse(self, response):
        ligths = response.css('div.WdR1o')
        for ligth in ligths:
            yield {
                'name' : ligth.css('div.lsooF span::text').get(),
                'price' : ligth.css('div.pY3d2 span::text').get(),
                'url' : ligth.css('a').attrib['href']

            }



