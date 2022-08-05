from scrapy.commands import ScrapyCommand
from scrapy.utils import project
import scrapy
from scrapy.spiderloader import SpiderLoader
from scrapy.crawler import CrawlerProcess


class Command(ScrapyCommand):
    requires_project = True

    def syntax(self):
        return '[options]'

    def short_desc(self):
        return '爬取目标m3u8'

    def run(self, args, opts):
        url = args[0]
        settings = project.get_project_settings()
        spider_loader = SpiderLoader.from_settings(settings)
        spider_class = spider_loader.load('basepro')
        spider_class.url = url
        crawler_process = CrawlerProcess(settings)
        crawler_process.crawl(spider_class)
        crawler_process.start()
