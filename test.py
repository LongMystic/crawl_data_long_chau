import pandas as pd

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


def main():
    p_id = 0
    new_df = pd.read_csv('./crawl_long_chau/temp.csv').sort_values('p_id')

    for _category in _categories:
        df = pd.read_csv(f'./final_result/{_category}.csv')
        for j in range(len(df)):
            for i in range(len(new_df)):
                if df.loc[j, 'product_id'] == new_df.loc[i, 'p_id']:
                    df.loc[j, 'usage'] = new_df.loc[i, 'usage']
                    df.loc[j, 'specification'] = new_df.loc[i, 'specification']
                    df.loc[j, 'description'] = new_df.loc[i, 'description']
        df.to_csv(f'./final_result_3/{_category}.csv', index=False)


if __name__ == "__main__":
    main()
