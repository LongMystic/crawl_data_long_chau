# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import csv


class CrawlLongChauPipeline:
    def open_spider(self, spider):
        self.csvfile = open('temp.csv', 'w', newline='', encoding='utf-8')
        self.fieldnames = ['p_id', 'usage', 'specification', 'description']
        self.writer = csv.DictWriter(self.csvfile, fieldnames=self.fieldnames)
        self.writer.writeheader()

    def close_spider(self, spider):
        self.csvfile.close()

    def process_item(self, item, spider):
        self.writer.writerow(item)
        return item
