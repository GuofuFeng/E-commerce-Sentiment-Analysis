# -*- coding: utf-8 -*-
# visualize_results.py

import matplotlib.pyplot as plt
from wordcloud import WordCloud
import pandas as pd
from config import WORDCLOUD_IMAGE, SENTIMENT_PLOT


def generate_visualizations(df: pd.DataFrame):
    """
    生成词云和情感分布图（修复中文显示）
    """
    # 配置中文字体（需提前下载字体文件，如SimHei.ttf）
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False

    # 词云生成
    text = ' '.join(df['review_text'].dropna())
    wordcloud = WordCloud(width=800, height=400, background_color='white', font_path='SimHei.ttf').generate(text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title('评论高频词云图')
    plt.savefig(WORDCLOUD_IMAGE)
    plt.close()

    # 情感分布直方图
    plt.figure(figsize=(10, 6))
    df['sentiment_label'].value_counts().plot(kind='bar')
    plt.title('情感分布统计')
    plt.xlabel('情感类别')
    plt.ylabel('评论数量')
    plt.savefig(SENTIMENT_PLOT)
    plt.close()


# 测试代码
if __name__ == "__main__":
    from config import RESULTS_CSV

    df = pd.read_csv(RESULTS_CSV)
    generate_visualizations(df)
    print(f"可视化结果已保存至: {WORDCLOUD_IMAGE}, {SENTIMENT_PLOT}")