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


def main():
    p_id = 0

    for i in range(5):

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

        for _ in range(_counts[i]):
            try:
                if i < 4:
                    df = pd.read_csv(f'./tmp/{_categories[i]}_product_{p_id}.csv')
                else:
                    df = pd.read_csv(f'./tmp1/{_categories[i]}_product_{p_id}.csv')
                df_dict = df.to_dict(orient='records')[0]
                # print(df_dict)
                data['product_id'].append(df_dict['product_id'])
                data['product_name'].append(df_dict['product_name'])
                data['product_category'].append(df_dict['product_category'])
                data['product_category_tree'].append(df_dict['product_category_tree'][2:])
                data['usage'].append(df_dict['usage'])
                data['specification'].append(df_dict['specification'])
                data['description'].append(df_dict['description'])
                data['image_urls'].append(str(df_dict['image_urls'])[3:])
                data['product_url'].append(str(df_dict['product_url']))
            except:
                pass

            p_id += 1

        # for k, v in data.items():
        #     print(f"{k} {len(v)}")
        # print(len(data))
        new_df = pd.DataFrame(data)
        new_df.to_csv(f"./final_result/{_categories[i]}.csv", index=False)


if __name__ == "__main__":
    main()
