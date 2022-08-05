import scrapy
import os
from scrapy.responsetypes import Response
from m3u8.m3u8 import M3U8


class BaseSpider(scrapy.Spider):
    name = 'basepro'
    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:98.0) Gecko/20100101 Firefox/98.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
    }

    def __init__(self):
        super().__init__(name='basepro')
        self.movie_name = self.url.replace("/", " ").strip().split(" ")[-1].split(".")[0]

    def start_requests(self):
        if not os.path.exists('./movie/{}'.format(self.movie_name)):
            os.mkdir('./movie/{}'.format(self.movie_name))
        self.logger.info("fetch m3u8 file...")
        return [scrapy.Request(url=self.url, headers=self.header, callback=self.fetch_ts)]

    def fetch_ts(self, response: Response):
        base_url = '/'.join(response.url.split('/')[:-1]) + '/{}'
        m3u8 = M3U8(response.text)
        data = {
            'name': self.movie_name + '.m3u8',
            'content': response.text,
            'mode': 'wt'
        }
        self.logger.info("saving m3u8 file: {}".format(data['name']))
        yield data

        self.logger.info("fetch key file...")
        yield scrapy.Request(url=base_url.format(m3u8.ext_x_key['URI']), headers=self.header, meta={'ts': m3u8.ext_x_key['URI']}, callback=self.save_ts)

        self.logger.info("fetch ts files...")
        for item in m3u8.extinf:
            yield scrapy.Request(url=base_url.format(item.ts), headers=self.header, meta={'ts': item.ts}, callback=self.save_ts)

    def save_ts(self, response):
        data = {
            'name': response.meta['ts'],
            'content': response.body
        }
        self.logger.info("saving ts file: {}".format(data['name']))
        return data
