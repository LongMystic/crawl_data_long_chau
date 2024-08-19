import pandas as pd

uris = [
    "thuc-pham-chuc-nang",
    "duoc-my-pham",
    "cham-soc-ca-nhan",
    "trang-thiet-bi-y-te",
    "thuoc"
]

cnt = 0
for uri in uris:
    df = pd.read_csv(f'./data/{uri}_product.csv')
    # tmp = df.to_dict(orient='records')
    # for dt in tmp:
    #     print(dt)
    print(f"{uri}: {len(df)}")
    cnt += len(df)

print(cnt)
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# options = webdriver.ChromeOptions()
# options.add_experimental_option("detach", True)
# driver = webdriver.Chrome(options=options)
#
# website = "https://nhathuoclongchau.com.vn/trang-thiet-bi-y-te/urgo-scarform-gel-dieu-tri-seo-phi-dai-seo-loi-and-mo-tham-7-g.html"
# # get all category_url
# driver.get(website)
# driver.maximize_window()
# time.sleep(3)
#
# print(driver.find_element(By.XPATH, "//div[@class='usage']/div").get_attribute("innerHTML"))

# for i in range(10):
#     num = []
#     try:
#         if i < 3:
#             num.append(i)
#         else:
#             raise Exception
#     except:
#         continue
#     print(i)

