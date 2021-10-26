import os


path = 'D:\电机故障数据\电机故障实验数据9-12通道_2020年10月'
file = os.listdir(path)
print(file)
file_path = []
for filename in file:
    file_path.append(path + '\\' + filename)
# print(file_path)

data_name = []
for file_Path in file_path:
    data_Name = os.listdir(file_Path)
    data_name.append(data_Name)
print(len(data_name))
print(data_name[0])

condition = ['15Hz_0V', '15Hz_1V', '15Hz_1.5V', '25Hz_0V', '25Hz_1V', '25Hz_2V', '35Hz_0V', '35Hz_1V', '35Hz_2V',
             '45Hz_0V', '45Hz_1V', '45Hz_2V']
condition_1 = ['15Hz_0V', '15Hz_0.5V', '25Hz_0V', '25Hz_0.5V', '35Hz_0V', '35Hz_0.5V', '35Hz_1V', '45Hz_0V',
               '45Hz_0.5V', '45Hz_1V']

for i in range(len(file_path)):
    for j in range(len(data_name[i])):
        raw_name = file_path[i] + '\\' + data_name[i][j]
        name = data_name[i][j]
        fault = file[i]
        # date = name.split('_2020')[1][0:4]
        # time = name.split(' ')[1][0:4]
        if len(data_name[i]) == 12:
            new_name = file_path[i] + '\\' + fault + '_' + condition[j] + '.txt'
            os.rename(raw_name, new_name)
        elif len(data_name[i]) == 10:
            new_name = file_path[i] + '\\' + fault + '_' + condition_1[j] + '.txt'
            os.rename(raw_name, new_name)
        else:
            print(file_path[i])
    print(file[i]+'修改完成')



