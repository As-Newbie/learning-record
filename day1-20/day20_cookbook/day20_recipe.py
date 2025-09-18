class Recipe:
    def __init__(self, name, ingredients, steps):
        # 定义类 包含 菜名、原料、步骤
        self.name = name
        self.ingredients = ingredients
        self.steps = steps

    def show(self):
        # 打印完整菜谱
        print(f"菜名：{self.name}")
        print(f"原料：")
        for i, ingredients in enumerate(self.ingredients):
            print(f"{i}.{ingredients}")
        print(f"步骤：{self.steps}")
        for i, step in enumerate(self.steps):
            print(f"{i},{step}")

    def __str__(self):

        # 返回菜谱的简短字符串表示。
        # 返回: str: 包含菜名和基本信息的字符串。

        return f"Recipe(name='{self.name}', ingredients_count={len(self.ingredients)}, steps_count={len(self.steps)})"

    def get_summary(self):
        # 获取菜谱的摘要信息。
        # 返回:    str: 包含菜名、原料数和步骤数的摘要字符串。
        return f"{self.name} ({len(self.ingredients)}种原料, {len(self.steps)}个步骤)"