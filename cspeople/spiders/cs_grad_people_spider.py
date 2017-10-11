import scrapy
from scrapy.selector import Selector
from cspeople.items import ProfilePictureItem


class CSGradPeople(scrapy.Spider):
    name = "csgrad"
    # list of allowed domains
    allowed_domains = ['http://www.cs.princeton.edu/people/grad']
    start_urls = [
        'http://www.cs.princeton.edu/people/restech',
    ]

    def parse(self, response):
        sel = Selector(response)

        xpath = '//div[@class="person-photo"]/img/@src | //div[@class="person-photo"]/a/img/@src'
        images = sel.xpath(xpath).extract()

        for image in images:
            item = ProfilePictureItem()
            item['image_urls'] = [response.urljoin(image)]
            yield item
