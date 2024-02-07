import os
import dotenv
from openai import OpenAI

# 載入.env檔案中的環境變數
dotenv.load_dotenv()

# 從.env檔案中讀取API金鑰
api_key = os.getenv('API_KEY')

# 創建OpenAI客戶端並使用讀取到的API金鑰
client = OpenAI(api_key=api_key)

# 讀取 prompt 檔案
with open('script.txt', 'r') as file:
    prompt = file.read()

# 讀取 preprompt 檔案
with open('preprompt.txt', 'r') as file:
    preprompt = file.read()

# 使用 prompt 和 preprompt 變數的內容進行 API 調用
response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": preprompt},
        {"role": "user", "content": prompt}
    ]
)

# 獲取API回應的內容
output = response.choices[0].message.content

# 將結果寫入Markdown檔案
with open('output.md', 'w') as file:
    file.write(output)

print("結果已成功輸出到output.md檔案中。")
