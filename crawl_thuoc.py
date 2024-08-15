from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import pandas as pd
import time

website = "https://nhathuoclongchau.com.vn/thuoc"


def main():
    p_id = 5000

    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)

    # get all category_url
    driver.get(website)
    driver.maximize_window()
    time.sleep(3)

    category = {
        "category_name": [],
        "category_url": []
    }

    for row in driver.find_elements(By.XPATH, "//div[@class='md: mt-4 grid grid-cols-1 gap-3 md:mt-5 md:grid-cols-3 md:gap-y-4 md:gap-x-5']/a"):
        name = row.find_element(By.XPATH, "./div/h3").get_attribute("innerHTML")
        url = row.find_element(By.XPATH, ".").get_attribute("href")
        print(url)
        category['category_name'].append(name)
        category['category_url'].append(url)

    data = {
        'product_id': [],
        'product_name': [],
        'product_url': []
    }

    for url in category['category_url']:
        driver.get(url)
        time.sleep(3)

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
    df.to_csv(f"./data/thuoc_product.csv", index=False)


if __name__ == "__main__":
    main()
