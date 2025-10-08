import pandas as pd
s = pd.Series(
    [2171, 2487, 1868, 1260, 1308],
    index=['北京', '上海', '广州', '深圳', '重庆'],
    name="人口（万人）"
)

print("🏙️ 原始数据：")
print(s)

print(f"\n👑 人口最多的城市：{s.idxmax()}（{s.max()} 万人）")

# 批量更新
s.update(pd.Series({'北京': s['北京'] * 2, '上海': s['上海'] * 3}))

print("\n🔄 更新后的数据：")
print(s)
dataframe={
    "姓名":["小明","小红","小刚","小丽"],
    "年龄":[18,17,18,17],
    "成绩":[85,92,78,88]
}
df=pd.DataFrame(dataframe)
print("📋 原始表格：")
print(df)
print(f"\n共有 {df.shape[0]} 行，{df.shape[1]} 列。")

print(f"\n平均成绩：{df['成绩'].mean():.1f}")
print("\n成绩最高的学生：")
print(df.loc[df['成绩'].idxmax()])

print("\n只查看姓名与成绩列：")
print(df.filter(['姓名', '成绩']))

df['是否及格'] = df['成绩'] >= 60
print("\n✅ 新增“是否及格”列：")
print(df)

print("\n📈 统计摘要：")
print(df.describe())

