import os
import numpy as np

path = 'E:\pythonfile\data'
file = os.listdir(path)
print(file)
file_path = []
for filename in file:
    file_path.append(path + '\\' + filename)
#
#
# for name in file_path:
#     with open(name, "r", encoding='utf-8') as f:  # 打开文件
#         data = f.readlines()
#         for line in data:
#             line = line.strip('\n')  # 去掉列表中每一个元素的换行符
#         for i in range(19, len(data)):
#             data[i] = data[i].split('2147483648')[0]+'\n'
#     with open(name, "w", encoding='utf-8') as f:
#         for d in data:
#             f.write(d)
name = 'E:\横向课题\昇阳项目资料\加速度信号转速度信号及位移信号\\2A浆液循环泵电机非驱动端4-2.txt'
list1 = []
with open(name, "r", encoding='utf-8') as f:  # 打开文件
    data = f.readlines()
    for line in data:
        line = line.strip('\n')
    for i in range(14, len(data)):
        a = float(data[i].split()[1])
        list1.append(a)
print(len(list1))