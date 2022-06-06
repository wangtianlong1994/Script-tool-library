# 查看训练数据集中测试集中各类数量，判断测试数据是否均衡
import os
hao = 0
ao = 0
txt_list = os.listdir("./val")
paths = "./val/"
for i in txt_list:
    f = open(f"{paths+i}", "r+")
    data = f.read()
    data = data.split(" ")[0]

    if data == "1":
        ao += 1
    else:
        hao += 1

print(f"测试数据集中好有：{hao}个,凹坑有：{ao}个。")