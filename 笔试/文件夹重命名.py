import os
import time

path = 'D:\电机故障数据\电机故障实验数据9-12通道_2020年10月'
file = os.listdir(path)
print(file)
old_names = ['不对中', '不平衡', '电气故障_断条_3条', '电气故障_电压不平衡_二分之一', '电气故障_电压不平衡_四分之一', '电气故障_缺相', '短路_百分之五_二分之一', '短路_百分之五_最大',
             '短路_百分之十_二分之一', '短路_百分之十_最大', '轴弯曲', '非驱动端_保持架_中等断裂', '非驱动端_保持架_轻微(尼龙)', '非驱动端_保持架_轻微断裂', '驱动端_保持架_严重_1',
             '驱动端_保持架_严重断裂', '驱动端_保持架_中等断裂', '驱动端_保持架_轻微断裂', '驱动端_保持架_轻微断裂(固定螺栓松动)', '驱动端_内圈_严重', '驱动端_内圈_中等',
             '驱动端_内圈_轻微', '驱动端_四种复合故障', '驱动端_复合故障_内圈严重外圈中度滚动体轻微', '驱动端_复合故障_内圈严重滚动体严重', '驱动端_复合故障_内圈严重滚动体轻微',
             '驱动端_复合故障_内圈中等外圈严重滚动体轻微', '驱动端_复合故障_内圈中等外圈中等保持架严重(尼龙)', '驱动端_复合故障_内圈中等外圈中等滚动体严重', '驱动端_复合故障_外圈严重内圈中等',
             '驱动端_复合故障_外圈严重内圈中等_1', '驱动端_复合故障_外圈严重滚动体严重', '驱动端_复合故障_外圈严重滚动体轻微', '驱动端_复合故障_外圈中等内圈严重', '驱动端_外圈_中等',
             '驱动端_外圈_轻微', '驱动端_外圈严重', '驱动端_正常', '驱动端_滚动体_严重', '驱动端_滚动体_中等', '驱动端_滚动体_轻微']
new_names = ['MS', 'IBS', 'RB-3', 'VIB-50', 'VIB-25', 'PL', 'SC-5-50', 'SC-5-100', 'SC-10-50', 'SC-10-100', 'BS',
             'F-C-II', 'F-C-III(NFC)', 'F-C-I', 'D-C-III(NFC)', 'D-C-III', 'D-C-II', 'D-C-I', 'D-C-I(loosened bolts)',
             'D-I-III', 'D-I-II', 'D-I-I', 'D-O-II+I-II+B-II+C-II', 'D-O-II+I-III+B-I', 'D-I-III+B-III', 'D-I-III+B-I',
             'D-O-III+I-II+B-I', 'D-O-II+I-II+C-III', 'D-O-II+I-II+B-III', 'D-O-III+I-II', 'D-O-III+I-II-1',
             'D-O-III+B-III', 'D-O-III+B-I', 'D-I-III+O-II', 'D-O-II', 'D-O-I', 'D-O-III', 'NC', 'D-B-III', 'D-B-II',
             'D-B-I']
newDirPath = [path + '\\' + x for x in new_names]
oldDirPath = [path + '\\' + x for x in old_names]
for i in range(len(newDirPath)):
    if os.path.exists(oldDirPath[i]):
        os.rename(oldDirPath[i], newDirPath[i])
    else:
        print(oldDirPath[i])
