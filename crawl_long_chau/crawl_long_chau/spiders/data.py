from typing import Iterable

import scrapy
from scrapy import Request
import pandas as pd


class DataSpider(scrapy.Spider):
    name = "data"
    # allowed_domains = ["nhathuoclongchau.com.vn"]
    # start_urls = ["https://nhathuoclongchau.com.vn/thuc-pham-chuc-nang/siro-giup-giam-ho-bo-phe-labebe-120-ml.html"]

    def start_requests(self):
        _categories = [
            "thuc-pham-chuc-nang",
            "duoc-my-pham",
            "cham-soc-ca-nhan",
            "trang-thiet-bi-y-te",
            "thuoc"
        ]

        _counts = [
            1872,
            979,
            818,
            858,
            6586
        ]

        p_id = 0

        for i in range(5):

            for _ in range(_counts[i]):

                try:
                    if i < 4:
                        df = pd.read_csv(f'/home/long.vk@citigo.id/longvk/python/crawl_data_long_chau/tmp/{_categories[i]}_product_{p_id}.csv')
                    else:
                        df = pd.read_csv(f'/home/long.vk@citigo.id/longvk/python/crawl_data_long_chau/tmp1/{_categories[i]}_product_{p_id}.csv')
                    df_dict = df.to_dict(orient='records')[0]

                    url = str(df_dict['product_url'])

                    yield scrapy.Request(url=url, callback=self.parse, meta={'p_id': p_id})

                except Exception:
                    pass

                p_id += 1

    def parse(self, response):
        usage = ""
        try:
            for row in response.xpath("//div[@class='usage']/div/p"):
                if len(usage) > 0:
                    usage += "***"
                usage += row.xpath("./text()").get()
        except Exception:
            pass

        specification = ""
        description = ""

        try:
            for row in response.xpath("//table[@class='content-list']/tbody/tr"):
                if row.xpath("./td[1]/p/text()").get() == "Quy cách":
                    specification = row.xpath("./td[2]/div/text()").get()

                if row.xpath("./td[1]/p/text()").get() == "Mô tả ngắn":
                    description = row.xpath("./td[2]/div/p/text()").get()
        except Exception:
            pass
        yield {
            'p_id': response.meta['p_id'],
            'usage': usage,
            'specification': specification,
            'description': description
        }
