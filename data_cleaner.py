# -*- coding: utf-8 -*-
# data_cleaner.py

import pandas as pd
from datetime import datetime


def clean_data(raw_df: pd.DataFrame) -> pd.DataFrame:
    """
    数据清洗与格式转换
    """
    # 删除无用列
    df = raw_df.drop(columns=['profileName', 'helpfulness'], errors='ignore')

    # 处理时间字段
    df = df.dropna(subset=['time'])
    df['time'] = df['time'].apply(lambda x: datetime.utcfromtimestamp(int(x)))

    # 转换rating列为整数类型
    df['rating'] = pd.to_numeric(df['rating'], errors='coerce').astype('Int64')
    df = df.dropna(subset=['rating'])

    # 处理价格字段
    df['price'] = pd.to_numeric(df['price'], errors='coerce')

    # 重命名列
    df = df.rename(columns={
        'productId': 'product_id',
        'title': 'product_title',
        'text': 'review_text'
    })

    # 删除缺失评论内容
    df = df.dropna(subset=['review_text'])

    return df


# 测试代码
if __name__ == "__main__":
    from data_loader import load_raw_data
    from config import INPUT_FILE, CLEANED_DATA

    raw_df = load_raw_data(INPUT_FILE)
    cleaned_df = clean_data(raw_df)
    cleaned_df.to_csv(CLEANED_DATA, index=False)
    print("清洗后数据已保存至:", CLEANED_DATA)