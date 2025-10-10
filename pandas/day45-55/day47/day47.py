import pandas as pd
# 🧠 练习题（请你先完成）
# 1️⃣ 创建两个 DataFrame：
# df_a：包含 姓名、年龄
# df_b：包含 姓名、成绩
df_a=pd.DataFrame({
    "name":["zhang san","li si","wang wu"],
    "age":[20,22,25]
})
df_b=pd.DataFrame({
    "name":["zhang san","li si","zhao liu"],
    "score":[90,85,88]
})
# 请使用 pd.merge() 按“姓名”合并两表（类型为 inner join）。
df_merge=pd.merge(df_a,df_b,on="name",how="inner")
# 💡 小优化：
# 可以加上 indicator=True 参数，这样可以看出每行来自哪个表：
# df_merge = pd.merge(df_a, df_b, on="name", how="inner", indicator=True)
print(f" 1️⃣ 使用 pd.merge() 按“姓名”合并两表（类型为 inner join）\n{df_merge}")
# 2️⃣ 在合并后的结果中，将缺失的成绩填充为 60。
df_outer=pd.merge(df_a,df_b,on="name",how="outer")
print(f" 2️⃣ 使用 pd.merge() 按“姓名”合并两表（类型为 outer join）\n{df_outer}")
df_outer["score"].fillna(60,inplace=True)
# 💡 小优化建议：
# 可以一步完成合并与填充：
# df_outer = pd.merge(df_a, df_b, on="name", how="outer").fillna({"score": 60})
print(f" 2️⃣ 在合并后的结果中，将缺失的成绩填充为 60\n{df_outer}")
# 3️⃣ 再使用 pd.concat() 将一个新的 DataFrame（包含两名新学生）追加到结果表中。
df_c=pd.DataFrame({
    "name":["zhou qi","wu ba"],
    "score":[75,None],
    "age":[23,24]
})
df_add=pd.concat([df_outer,df_c],ignore_index=True)
# 💡 小优化：
# 如果列顺序不确定，可以让 Pandas 自动对齐列：
# df_add = pd.concat([df_outer, df_c], ignore_index=True, sort=False)
# 👉 sort=False 可以避免自动字母排序。
print(f" 3️⃣ 使用 pd.concat() 将一个新的 DataFrame（包含两名新学生）追加到结果表中\n{df_add}")
# 4️⃣ 最后，删除所有有缺失值的行。
print(f" 4️⃣ 缺失值矩阵的构成如下：（“True”表示存在值，而“False”表示缺失值。）\n{df_add.notna()}")
df_clean=df_add.dropna()
# 💡 小改进：
# 通常我们在清洗数据时会先统计缺失量：
# print(df_add.isna().sum())  # 每列缺失数量
print(f" 4️⃣ 删除所有有缺失值的行\n{df_clean}")

