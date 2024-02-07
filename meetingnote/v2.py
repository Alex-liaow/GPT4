# 引入依賴套件
import pandas as pd
import os
import openai
from dotenv import load_dotenv

# 載入.env中的環境變數
load_dotenv()

# 從.env讀取API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# 讀取CSV資料，如果文件不存在或者无法解析，就退出
try:
    df = pd.read_csv("v1.csv")
except FileNotFoundError:
    print("Error: File not found.")
    exit()
except pd.errors.ParserError:
    print("Error: Fail to parse CSV file.")
    exit()

# 遍歷DataFrame中每一项，處理每一个内容
for index, row in df.iterrows():
    for col in df.columns:
        content = row[col]
        # 检查内容是否为空字串
        if content and isinstance(content, str):
            # 使用GPT模型处理文本
            response = openai.Completion.create(
              engine="engine_id",
              prompt=f"幫我把會議逐字稿的贅字移除，使用繁體中文：{content}",
              max_tokens=60
            )
            # 將结果写入DataFrame
            row[col] = response.choices[0].text.strip()

# 保存处理过的CSV数据
df.to_csv("v2.csv", index=False)