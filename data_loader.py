# -*- coding: utf-8 -*-
# data_loader.py

import pandas as pd
import re


def load_raw_data(file_path: str) -> pd.DataFrame:
    """
    解析Stanford SNAP的txt格式数据
    """
    products = []
    reviews = []
    current_product = {}

    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            # 解析字段
            if line.startswith("product/"):
                key_value = re.split(r':\s+', line, maxsplit=1)
                key = key_value[0].replace("product/", "")
                current_product[key] = key_value[1] if len(key_value) > 1 else None
            elif line.startswith("review/"):
                key_value = re.split(r':\s+', line, maxsplit=1)
                key = key_value[0].replace("review/", "")
                value = key_value[1] if len(key_value) > 1 else None

                # 关键修复：将 review/score 存入 rating 列
                if key == 'score':
                    current_product['rating'] = value
                else:
                    current_product[key] = value

                # 当遇到新评论时保存上一个产品信息
                if key == 'userId' and current_product:
                    reviews.append(current_product.copy())
                    current_product.clear()

        # 添加最后一个评论
        if current_product:
            reviews.append(current_product)

    return pd.DataFrame(reviews)


# 测试代码
if __name__ == "__main__":
    from config import INPUT_FILE

    df = load_raw_data(INPUT_FILE)
    print(df.head())