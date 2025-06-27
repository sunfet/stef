import pandas as pd

# 读取 CSV 文件（不假设列名）
data = pd.read_csv('TEK00000.csv', nrows=5)  # 只读前5行用于调试
print("CSV 文件内容预览:")
print(data)