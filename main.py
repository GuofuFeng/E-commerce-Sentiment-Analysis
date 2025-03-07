# -*- coding: utf-8 -*-
# main.py

from data_loader import load_raw_data
from data_cleaner import clean_data
from sentiment_analysis import analyze_sentiment
from visualize_results import generate_visualizations
from config import INPUT_FILE, CLEANED_DATA, RESULTS_CSV


def main():
    # 数据加载
    print("正在加载原始数据...")
    raw_df = load_raw_data(INPUT_FILE)
    print(f"原始数据记录数：{len(raw_df)}")

    # 数据清洗
    print("\n正在清洗数据...")
    cleaned_df = clean_data(raw_df)
    print(f"清洗后有效数据记录数：{len(cleaned_df)}")
    cleaned_df.to_csv(CLEANED_DATA, index=False)

    # 情感分析
    print("\n正在执行情感分析...")
    analyzed_df = analyze_sentiment(cleaned_df)
    analyzed_df.to_csv(RESULTS_CSV, index=False, encoding='utf-8-sig')

    # 可视化
    print("\n正在生成可视化图表...")
    generate_visualizations(analyzed_df)

    print("\n=== 分析完成 ===")


if __name__ == "__main__":
    main()