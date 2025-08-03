import csv
#寫入
def write_csv(x, data):
    with open(x, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(data)
        writer.writerow(["a", "b"])  

data = [
    ['姓名', '年齡', '城市'],
    ['小明', 25, '台北'],
    ['小華', 30, '台中'],
    ['小王', 22, '高雄'],
    ['小李', 28, ]
]


write_csv('people.csv', data)


#讀取
def read_csv(G):
    with open(G, mode='r', newline='', encoding='utf-8') as file:#newline=''避免換行符號問題
        reader = csv.reader(file)
        n=0
        for row in reader:
            n+=1
            print(f"第 {n} 行:", row)

read_csv('people.csv')


# 寫入 CSV - 有加 newline=''
# with open('with_newline.csv', mode='w', newline='', encoding='utf-8') as file:
#     writer = csv.writer(file)
#     writer.writerows(data)


# # 寫入 CSV - 沒加 newline 參數（使用預設）
# with open('without_newline.csv', mode='w', encoding='utf-8') as file:
#     writer = csv.writer(file)
#     writer.writerows(data)



