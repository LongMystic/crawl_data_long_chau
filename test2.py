import pandas as pd
import ast


def get_tree(lv1, lv2, lv3):
    res = ""
    res += lv1
    res += ">>"
    res += lv2
    if pd.isna(lv3):
        pass
    else:
        res += ">>"
        res += lv3
    return res


def get_urls(arr1):
    arr = ""
    try:
        arr = ast.literal_eval(arr1)
    except Exception:
        pass
    # print(arr1)
    urls = ""
    for url in arr:
        # print(url)
        if len(urls) > 0:
            urls += "***"
        urls += url
    return urls


def main():
    data = {
        "product_id": [],
        "product_name": [],
        "product_category": [],
        "product_category_tree": [],
        "image_urls": [],
        "product_url": []
    }

    p_id = 0
    df = pd.read_csv('./products_thuoc_an_khang.csv', delimiter='\t')
    for i in range(len(df)):
        data['product_id'].append(p_id)
        data['product_name'].append(df.iloc[i]['product_name'])
        if pd.isna(df.iloc[i]['category_lv3']):
            data['product_category'].append(df.iloc[i]['category_lv2'])
        else:
            data['product_category'].append(df.iloc[i]['category_lv3'])
        data['product_category_tree'].append(get_tree(df.iloc[i]['category_lv1'], df.iloc[i]['category_lv2'], df.iloc[i]['category_lv3']))
        # print(df.iloc[i]['image'])
        data['image_urls'].append(get_urls(df.iloc[i]['image']))
        data['product_url'].append("")
        print(df.iloc[i]['image'])

        p_id += 1

    new_df = pd.DataFrame(data)
    new_df.to_csv('./data_an_khang.csv', index=False)


if __name__ == "__main__":
    main()