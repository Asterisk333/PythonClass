import pandas as pd
from clean_data import clean_data

df = clean_data(pd.read_csv('amazon.csv'))


def top_discounted_products(df):
    # Ordered py percentage desc
    df_sorted = df.sort_values(by="discount_percentage", ascending=False)

    # select top 10
    df_top10 = df_sorted.head(10)

    # return needed data
    df_top10 = df_top10[["product_name", "actual_price", "discounted_price", "discount_percentage"]]

    return df_top10


print(top_discounted_products(df))
