# -*- coding: utf-8 -*-
# sentiment_analysis.py

from textblob import TextBlob
import pandas as pd
from sklearn.metrics import accuracy_score
from config import CLEANED_DATA, RESULTS_CSV


def analyze_sentiment(input_df: pd.DataFrame) -> pd.DataFrame:
    """
    执行情感分析并添加结果列（修复变量名冲突）
    """
    processed_df = input_df.copy()

    # 计算情感极性
    processed_df['sentiment'] = processed_df['review_text'].apply(
        lambda x: TextBlob(x).sentiment.polarity
    )

    # 划分情感类别
    processed_df['sentiment_label'] = pd.cut(
        processed_df['sentiment'],
        bins=[-1, -0.1, 0.1, 1],
        labels=['负面', '中性', '正面']
    )

    # 定义标签转换函数（确保 rating 为整数）
    def rating_to_label(rating: int) -> str:
        if rating >= 4:
            return '正面'
        elif rating <= 2:
            return '负面'
        else:
            return '中性'

    # 应用标签转换
    processed_df['true_label'] = processed_df['rating'].apply(rating_to_label)

    # 计算准确率
    valid_data = processed_df.dropna(subset=['sentiment_label', 'true_label'])
    accuracy = accuracy_score(
        valid_data['true_label'],
        valid_data['sentiment_label']
    )
    print(f"\n情感分类准确率：{accuracy:.2%}")

    return processed_df


# 测试代码
if __name__ == "__main__":
    cleaned_df = pd.read_csv(CLEANED_DATA)
    analyzed_df = analyze_sentiment(cleaned_df)
    analyzed_df.to_csv(RESULTS_CSV, index=False, encoding='utf-8-sig')
    print("情感分析结果已保存至:", RESULTS_CSV)