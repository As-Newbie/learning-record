import random

# 生成三个随机数，范围在 99% ~ 99.9%
random_numbers = [random.uniform(99.5, 99.9) for _ in range(3)]

# 保留 4 位小数
random_numbers = [round(num, 2) for num in random_numbers]

# 按换行输出
print("\n".join(str(num) for num in random_numbers))
