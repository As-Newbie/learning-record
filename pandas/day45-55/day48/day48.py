# 操作                        说明                                              返回值
# df.duplicated()       判断每一行是否是重复行（相对于它前面的行）   一个布尔类型的 Series
# df.duplicated().sum() 计算重复行的总数                        一个整数
# df[df.duplicated()]   筛选并查看所有被标记为重复的行             一个 DataFrame
# 🧠 练习题
import pandas as pd
import numpy as np

data = {
    "姓名": ["小明", "小红", "小刚", "小丽", "小美", "小美"],
    "年龄": [18, np.nan, 20, 19, np.nan, np.nan],
    "成绩": [85, 92, 999, 88, 95, 95]
}
df = pd.DataFrame(data)
print(df)
# 1️⃣ 删除所有重复行
df_drop_duplicates=df.drop_duplicates()
print(f"Delete duplicate rows\n{df_drop_duplicates}")
# 2️⃣ 用 “年龄” 列的平均值填充缺失值
age_mean=df_drop_duplicates["年龄"].mean()
df_drop_duplicates=df_drop_duplicates.copy()
# 创建副本 但似乎没什么用处？
df_drop_duplicates["年龄"]=df_drop_duplicates["年龄"].fillna(age_mean)
# 不过在大型数据处理中，可以使用链式方式更简洁：
# df_drop_duplicates["年龄"].fillna(df_drop_duplicates["年龄"].mean(), inplace=True)
print(f"Fill in the missing values with the average value {age_mean} of the age column:\n{df_drop_duplicates}")
# 3️⃣ 删除成绩为异常值（超出正常区间）的行（用 IQR 方法）
q1=df_drop_duplicates["成绩"].quantile(0.25)
#   第一四分位数 (Q1)
q3=df_drop_duplicates["成绩"].quantile(0.75)
#   第三四分位数 (Q3)
IQR=q3-q1
# 四分位距
low_bound=q1-1.5*IQR
# 下限
up_bound=q3+1.5*IQR
# 上限
print(f"Statistical information of the grades column:\n"
      f"Q1={q1},Q3={q3}\n"
      f"Range of normal value:\n"
      f"[{low_bound},{up_bound}]")
# 如果要让输出更可读，可以加一点格式化美化：
# print(f"成绩列统计信息：Q1={q1:.2f}, Q3={q3:.2f}, 正常范围=[{low_bound:.2f}, {up_bound:.2f}]")
df_clean=df_drop_duplicates[(df_drop_duplicates["成绩"]>=low_bound)&(df_drop_duplicates["成绩"]<=up_bound)]

# 过滤掉异常值
# 4️⃣ 打印清洗后的最终 DataFrame
print(f"The final data after cleaning is：\n{df_clean}")
# 建议在最终输出后，也可以顺便验证一下是否存在缺失或异常：
# print("\n是否还有缺失值？")
# print(df_clean.isna().sum())