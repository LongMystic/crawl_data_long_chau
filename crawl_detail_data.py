from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import pandas as pd
import time

website = "https://nhathuoclongchau.com.vn/"


def main():
    p_id = 0
    val = 387

    uris = [
        "thuc-pham-chuc-nang",
        "duoc-my-pham",
        "cham-soc-ca-nhan",
        "trang-thiet-bi-y-te",
        "thuoc"
    ]

    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)

    driver.get(website)
    driver.maximize_window()
    time.sleep(3)

    for uri in uris:

        df = pd.read_csv(f'./data/{uri}_product.csv')
        data_dicts = df.to_dict(orient='records')

        for data_dict in data_dicts:
            if p_id < val:
                p_id += 1
                continue

            data = {
                "product_id": [],
                "product_name": [],
                "product_category": [],
                "product_category_tree": [],
                "usage": [],
                "specification": [],
                "description": [],
                "image_urls": [],
                "product_url": []
            }

            driver.get(f"{data_dict['product_url']}")
            time.sleep(5)

            # process category and category tree
            category = []
            for row in driver.find_elements(By.XPATH, "//ol[@class='my-3 flex flex-wrap md:my-4 container-lite']/li"):
                category.append(row.find_element(By.XPATH, "./span/a").get_attribute("innerHTML"))

            category_tree = ""
            for i in range(1, len(category)):
                if len(category) > 0:
                    category_tree += ">>"
                category_tree += category[i]
            if len(category) == 0:
                print(f"Crawl num {p_id} failed!")
                p_id += 1
                continue

            # process usage
            usage = ""
            try:
                usage = driver.find_element(By.XPATH, "//div[@class='usage']/div/p").get_attribute("innerHTML")
            except Exception:
                pass

            specification = ""
            description = ""

            try:
                for row in driver.find_elements(By.XPATH, "//table[@class='content-list']/tbody/tr"):
                    if row.find_element(By.XPATH, "./td[1]/p").get_attribute("innerHTML") == "Quy cách":
                        specification = driver.find_element(By.XPATH, "//table[@class='content-list']/tbody/tr[4]/td[2]/div").get_attribute("innerHTML")

                    if row.find_element(By.XPATH, "./td[1]/p").get_attribute("innerHTML") == "Mô tả ngắn":
                        description = driver.find_element(By.XPATH, "//table[@class='content-list']/tbody/tr[8]/td[2]/div").get_attribute("innerHTML")
            except Exception:
                pass

            image_urls = ""
            try:
                for row in driver.find_elements(By.XPATH, "//div[@class='lg-thumb-outer lg-thumb-align-middle lg-grab']/div/div"):
                    image_url = row.find_element(By.XPATH, "./img").get_attribute("src")
                    if len(image_url) > 0:
                        image_urls += "***"
                    image_urls += image_url
            except Exception:
                pass

            data['product_id'].append(p_id)
            data['product_name'].append(data_dict['product_name'])
            data['product_category'].append(category[-1])
            data['product_category_tree'].append(category_tree)
            data['usage'].append(usage)
            data['specification'].append(specification)
            data['description'].append(description)
            data['image_urls'].append(image_urls)
            data['product_url'].append(data_dict['product_url'])

            new_df = pd.DataFrame(data)
            new_df.to_csv(f"./tmp/{uri}_product_{p_id}.csv", index=False)
            print(f"Crawl num {p_id} successfully!")
            p_id += 1


if __name__ == "__main__":
    main()
