# import pandas as pd
# import glob
# import os
#
# csv_files = glob.glob('./final_result/*.csv')  # Update with the correct path
#
# # List to hold the DataFrames
# df_list = []
#
# # Iterate over the list of CSV files
# for file in csv_files:
#     df = pd.read_csv(file)
#     df_list.append(df)
#
# # Concatenate all DataFrames in the list into a single DataFrame
# final_df = pd.concat(df_list, ignore_index=True)
#
# final_df.to_csv('./final_result.csv', index=False)
# print(len(final_df))


import pandas as pd

df1 = pd.read_csv('./final_result.csv')

df2 = pd.read_csv('./crawl_long_chau/temp.csv')

df1.update(df1[['product_id']].merge(df2[['p_id', 'usage', 'specification', 'description']], left_on='product_id',
                                     right_on='p_id', how='left'))

df1.to_csv('./final_resulttt.csv', index=False)