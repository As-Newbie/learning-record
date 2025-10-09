import pandas as pd

data = {
    "姓名": ["小明", "小红", "小刚", "小丽", "小美"],
    "年龄": [18, 17, 18, 17, 19],
    "成绩": [85, 92, 78, 88, 95],
    "城市": ["北京", "上海", "广州", "深圳", "北京"]
}

df = pd.DataFrame(data)
print(df)
# 🧠 练习题
# 1️⃣ 选出成绩在 80 分以上的学生。
# 2️⃣ 新增一列 “是否成年”（年龄 ≥ 18）。
# 3️⃣ 删除 “城市” 这一列。
# 4️⃣ 按成绩从高到低排序。
# 5️⃣ 计算每个城市的平均成绩。

# 1️⃣ 选出成绩在 80 分以上的学生。
test1=df[df["成绩"]>80]
print(" 1️⃣ 选出成绩在 80 分以上的学生")
print(test1)
# 2️⃣ 新增一列 “是否成年”（年龄 ≥ 18）。
df['是否成年'] = df['年龄'] >= 18
# 💡 小优化（如果想让 True/False 更易读）：
# df['是否成年'] = np.where(df['年龄'] >= 18, '是', '否')
print(" 2️⃣ 新增一列 “是否成年”（年龄 ≥ 18）")
print(df)
# 3️⃣ 删除 “城市” 这一列。
df_deleted=df.drop(columns=["城市"])
print("️ 3️⃣ 删除 “城市” 这一列")
print(df_deleted)
# 4️⃣ 按成绩从高到低排序。
df_sort=df.sort_values(by="成绩", ascending=False)
print("️ 4️⃣ 按成绩从高到低排序")
print(df_sort)
# 5️⃣ 计算每个城市的平均成绩。
df_mean=df.groupby("城市")["成绩"].mean()
# 💡 小优化：
# 可以直接显示“前几名”：
# df.nlargest(3, "成绩")  # 成绩最高的前三名
# 💡 小优化（显示成 DataFrame 而非 Series）：
# df_mean = df.groupby("城市", as_index=False)[["成绩"]].mean()
print("️ 5️⃣ 计算每个城市的平均成绩")
print(df_mean)

