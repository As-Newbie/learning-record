from day21_recipe import Recipe
from day21_manager import add_recipe, show_recipes, delete_recipe, recipes
def get_input(prompt, multi_line=False):
    """获取用户输入，支持多行输入"""
    print(prompt)
    if multi_line:
        lines = []
        while True:
            line = input()
            if line.lower() == 'done':
                break
            lines.append(line)
        return lines
    return input().strip()


def main():
    print("=== 欢迎使用电压力锅菜谱管理系统 ===")
    while True:
        print("\n主菜单:")
        print("1. 添加菜谱")
        print("2. 查看所有菜谱")
        print("3. 删除菜谱")
        print("4. 退出系统")

        choice = input("请选择操作 (1-4): ")

        if choice == "1":
            name = get_input("请输入菜谱名称:")
            ingredients = get_input("请输入原料（每行一个，输入'done'结束）:", multi_line=True)
            steps = get_input("请输入步骤（每行一个，输入'done'结束）:", multi_line=True)
            cooking_time = get_input("请输入烹饪时间（分钟）:")

            if not ingredients or not steps:
                print("错误：原料和步骤不能为空")
                continue

            new_recipe = Recipe(name, ingredients, steps,cooking_time)
            add_recipe(new_recipe)

        elif choice == "2":
            show_recipes()
            if recipes:  # 如果有菜谱，显示查看详情的选项
                detail_choice = input("\n输入菜谱编号查看详情（直接回车返回主菜单）: ")
                if detail_choice.isdigit():
                    index = int(detail_choice) - 1
                    if 0 <= index < len(recipes):
                        recipes[index].show()

        elif choice == "3":
            show_recipes()
            if recipes:
                name = input("\n请输入要删除的菜谱名称: ")
                delete_recipe(name)

        elif choice == "4":
            print("\n感谢使用电压力锅菜谱管理系统，再见！")
            break

        else:
            print("无效输入，请重新选择")


if __name__ == "__main__":
    main()