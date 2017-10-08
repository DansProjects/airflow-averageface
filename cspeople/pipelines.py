from scrapy.contrib.pipeline.images import ImagesPipeline
from scrapy.http import Request
from scrapy import log
import hashlib


class CSGradPeoplePipeline(ImagesPipeline):

    # use default file_path function for sha1
    # def file_path(self, request, response=None, info=None):
        # just use default
        # image_guid = hash(request.url)
        # log.msg(image_guid, level=log.DEBUG)
        # return 'cspeople/%s' % image_guid + '.jpg'


    def get_media_requests(self, item, info):
        yield Request(item['image_urls'][0], meta=item)