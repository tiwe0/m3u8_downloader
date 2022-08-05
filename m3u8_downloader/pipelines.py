# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class StarsPipeline:
    def process_item(self, item, spider):
        mode = item.get('mode', 'wb')
        with open('./movie/{movie_path}/{file_name}'.format(movie_path=spider.movie_name, file_name=item['name']), mode=mode) as f:
            f.write(item['content'])
