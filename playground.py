import pandas as pd

# 假设我们有一个 DataFrame
data = {
    'id': [1, 1, 2, 2, 3, 3],
    'name': ['A', 'B', 'C', 'D', 'E', 'F'],
    'value': [10, 20, 30, 40, 50, 60]
}

df = pd.DataFrame(data)

# 打印原始 DataFrame
print("原始 DataFrame:")
print(df)

# 对 id 列进行分组，并获取每组的第一行
grouped_df = df.groupby('id').first().reset_index()

# 打印新的 DataFrame
print("\n新的 DataFrame:")
print(grouped_df)