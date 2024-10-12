import random
import csv


# 获取用户输入的餐馆列表
def get_restaurants():
    print("请输入你喜欢的餐馆，每输入一个餐馆按回车，完成后输入 'done'：")
    restaurants = []
    while True:
        restaurant = input("餐馆名称：")
        if restaurant.lower() == 'done':
            break
        restaurants.append(restaurant)
    if not restaurants:
        print("未输入任何餐馆，使用默认餐馆列表。")
        restaurants = ['周真真南昌粉面', '太二酸菜鱼', '饼学兼优', '绿茶餐厅', '大熊叔叔', '牛腩饭', '东北铁锅炖']#这是作者喜欢吃的，可以根据自己的喜好修改
    return restaurants


# 星期列表
days = ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期天']


# 随机生成一周的菜谱
def generate_menu(restaurants):
    menu = []
    for day in days:
        lunch = random.choice(restaurants)
        dinner = random.choice(restaurants)
        menu.append([day, lunch, dinner])
    return menu


# 保存到 CSV 文件
def save_menu_to_csv(menu, filename='/Users/hhm/weekly_menu.csv'):#更改为输出文件的路径
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Day', 'Lunch', 'Dinner'])
        writer.writerows(menu)
    print(f"菜谱已保存到文件: {filename}")


# 主程序
def main():
    # 获取餐馆列表
    restaurants = get_restaurants()

    # 生成菜谱
    menu = generate_menu(restaurants)

    # 保存菜谱到 CSV 文件
    save_menu_to_csv(menu)


if __name__ == '__main__':
    main()