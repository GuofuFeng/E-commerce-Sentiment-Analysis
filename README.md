# 🛒 美妆电商评论情感分析项目

## 📌 项目简介
基于 Stanford SNAP 的亚马逊美妆产品评论数据集，通过数据清洗、情感分析和可视化，挖掘用户对商品的真实反馈，为选品优化和营销策略提供数据支持。

## 🛠️ 技术栈
- **数据分析**: Python (Pandas + TextBlob)
- **可视化**: Matplotlib + Power BI
- **数据清洗**: 缺失值处理 + 异常值检测
- **工具**: PyCharm + Git

## 📂 项目结构
amazon_sentiment_analysis/
├── data/ # 原始数据与清洗后数据
│ ├── raw/ # 原始TXT文件 (需自行从Stanford SNAP下载)
│ └── cleaned_data.csv # 清洗后数据样例
├── src/ # 源代码
│ ├── main.py # 主程序入口
│ ├── data_loader.py # 数据加载与解析
│ ├── data_cleaner.py # 数据清洗
│ └── visualize_results.py # 可视化生成
├── outputs/ # 生成结果
│ ├── wordcloud.png # 评论词云图
│ └── sentiment_distribution.png # 情感分布图
├── requirements.txt # 依赖库列表 (通过 pip freeze > requirements.txt 生成)
└── README.md # 本说明文件


## 🚀 快速开始
### 环境配置
```bash
# 1. 克隆仓库
git clone https://github.com/你的用户名/E-commerce-Sentiment-Analysis.git

# 2. 安装依赖
pip install -r requirements.txt

# 3. 下载数据集 (从以下链接手动下载并放入 data/raw/)
# Stanford SNAP 美妆数据: https://snap.stanford.edu/data/web-Amazon-links.html

运行项目
# 执行主程序 (自动生成清洗数据、分析结果和图表)
python src/main.py

📊 关键成果
词云分析
![wordcloud](https://github.com/user-attachments/assets/bdbcf62e-b6ed-43ec-88a0-3d6a41d7b884)


情感分布
![sentiment_distribution](https://github.com/user-attachments/assets/073fc699-94f5-4a9e-b274-555b3fc9ce99)


📝 注意事项
中文字体配置：将 SimHei.ttf 字体文件放入项目根目录以正常显示中文

数据路径：修改 config.py 中的 INPUT_FILE 为你的实际数据路径

🤝 贡献与联系
GitHub Issues：提交代码问题或建议

邮箱: fgf13267069391@163.com
