from operator import index
from day21_recipe import Recipe
recipes=[]
# 添加新菜谱
# 参数:
# recipe(Recipe): 要添加的菜谱对象
# 返回:
# bool: 添加成功返回True，失败返回False
def add_recipe(recipe):
    # 检查对象和是否存在
    if not isinstance(recipe,Recipe):
        print("错误：只能添加Recipe类型的对象")
        return False
    # 这段代码的作用是进行类型检查，确保只有Recipe类的实例才能被添加到菜谱管理系统中。具体解释如下：
    # 为什么需要这段代码？
    # 1.类型安全防止错误类型的对象被添加到recipes列表中，避免后续操作（如调用recipe.name或recipe.show()）时崩溃。
    # 2. 维护数据一致性确保recipes列表中的所有元素都是 Recipe 对象，方便统一管理。
    # 3. 友好提示 直接告诉用户问题出在哪里，而不是抛出晦涩的异常（比如AttributeError: 'str' object has no attribute 'name'）
    # 示例场景
    # 错误用法（会被拦截）：
    # add_recipe("番茄炒蛋")  # 传入字符串，触发错误提示
    # add_recipe({"name": "红烧肉"})  # 传入字典，触发错误提示
    # 正确用法（通过检查）：
    # from recipe import Recipe
    # recipe = Recipe("番茄炒蛋", ["番茄", "鸡蛋"], ["步骤1", "步骤2"])
    # add_recipe(recipe)  # 通过检查，成功添加
    for existing_recipe in recipes:
        if existing_recipe.name==recipe.name:
            print(f"提示：菜谱{recipe.name}已经存在，无需重复添加")
            return False
    recipes.append(recipe)
    print(f"菜谱{recipe.name}添加成功！")
    return True
#遍历并打印所有菜谱的简略信息
def show_recipes():
    if not recipes:
        print("当前没有菜谱")
        return 0
    print(f"\n当前共有{len(recipes)}个菜谱")
    for i,recipe in enumerate(recipes,1):
        print(f"{i},{recipe.get_summary()}")

    return len(recipes)
# 显示制定菜谱的详细信息
# 参数:
# index(int, optional): 菜谱的索引位置（从1开始）
# name(str, optional): 菜谱的名称
# 返回:
# bool: 显示成功返回True，失败返回False
# 注意: 优先使用index参数，如果index为None则使用name参数
def show_recipe_details(index=None,name=None):
    recipe=None


    if index is not None:
        if index < 1 or index > len(recipes):
            print("错误：无效的菜谱索引")
            return False
        recipe = recipes[index - 1]
    elif name is not None:
        for r in recipes:
            if r.name == name:
                recipe = r
                break
        if recipe is None:
            print(f"错误：找不到名为 '{name}' 的菜谱")
            return False
    else:
        print("错误：请提供菜谱索引或名称")
        return False

    print("\n" + "=" * 50)
    recipe.show()
    print("=" * 50)
    return True
# 删除指定名称的菜谱
# 参数:
# name(str): 要删除的菜谱名称
# 返回:
# bool: 删除成功返回True，失败返回False
# Recipe: 如果删除成功，返回被删除的菜谱对象
def delete_recipe(name):
    global recipes

    for i, recipe in enumerate(recipes):
        if recipe.name == name:
            deleted_recipe = recipes.pop(i)
            print(f"菜谱 '{name}' 已删除")
            return True, deleted_recipe

    print(f"错误：找不到名为 '{name}' 的菜谱")
    return False, None
