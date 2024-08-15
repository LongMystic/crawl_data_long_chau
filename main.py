from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import pandas as pd
import time

website = "https://nhathuoclongchau.com.vn/"


def main():
    p_id = 0

    uris = [
        # "thuc-pham-chuc-nang",
        "duoc-my-pham",
        # "cham-soc-ca-nhan",
        # "trang-thiet-bi-y-te"
    ]

    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)

    for uri in uris:
        driver.get(f"{website}/{uri}")
        driver.maximize_window()
        time.sleep(3)

        data = {
            'product_id': [],
            'product_name': [],
            'product_url': []
        }

        while 1:
            try:
                xem_them_button = driver.find_element(By.XPATH, "//button[@class='mt-3 flex w-full items-center justify-center p-[10px]']")
                xem_them_button.click()
                time.sleep(3)
            except Exception:
                break

        for row in driver.find_elements(By.XPATH, "//div[@class='grid  grid-cols-2 gap-2 md:grid-cols-4 md:gap-5']/div"):
            p_url = row.find_element(By.XPATH, "./div/div/a").get_attribute("href")
            p_name = row.find_element(By.XPATH, "./div/div/a/h3").get_attribute("innerHTML")
            data['product_id'].append(p_id)
            data['product_name'].append(p_name)
            data['product_url'].append(p_url)
            p_id += 1

        df = pd.DataFrame(data)
        df.to_csv(f"./data/{uri}_product.csv", index=False)


if __name__ == "__main__":
    main()
