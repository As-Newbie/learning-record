from operator import index

import pandas as pd

# 练习 1：Series 操作
# 创建一个 pandas.Series，表示 5 个城市的人口数（单位：万人），自定义索引为城市名。
# 打印出人口最多的城市及其人口数。
# 将其中一个城市的人口修改为原来的两倍。
s=pd.Series([2171, 2487, 1868, 1260, 1308],index=['北京', '上海', '广州', '深圳', '重庆'])
print(f"五个城市的人口为\n{s}")
print(f"人口最多的城市为{s.idxmax()},其人数为:{s.max()}")
s["北京"]=s["北京"]*2
s.loc["上海"]=s["上海"]*3
print(f"北京人口翻两倍，上海人口翻三倍后的表为\n{s}")
# 练习 2：DataFrame 操作
# 创建一个包含以下数据的 DataFrame：
# 姓名	年龄	成绩
# 小明	18	85
# 小红	17	92
# 小刚	18	78
# 小丽	17	88
# 输出：
# 平均成绩
# 成绩最高的学生信息
# 只查看“姓名”和“成绩”两列
# 新增一列“是否及格”（成绩≥60 为 True）
dataframe={
    "姓名":["小明","小红","小刚","小丽"],
    "年龄":[18,17,18,17],
    "成绩":[85,92,78,88]
}
df=pd.DataFrame(dataframe)
print(f"原始数据：\n{df}")
# 计算平均成绩
average_score=df["成绩"].mean()
print(f"\n平均成绩：{average_score:.1f}")
# 成绩最高学生信息
max_score_row=df.loc[df["成绩"].idxmax()]
print(f"成绩最高的学生信息：\n{max_score_row}")
# 只查看“姓名”和“成绩”两列
new_date=df[['姓名','成绩']]
print(f"\n姓名和成绩列：\n{new_date}")
# 新增一列“是否及格”（成绩≥60 为 True）
df['是否及格'] = df['成绩'] >= 60
print(f"\n新增是否及格列后：\n{df}")
