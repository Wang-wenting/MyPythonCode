import pandas as pd
import numpy as np
import math


dataFile0 = "E:\\chrome下载\\train_step2.csv"
dataFile1 = "E:\\chrome下载\\test_step2.csv"
train_data_f = pd.read_csv(dataFile0, encoding='utf-8', engine='python')
test_data_f = pd.read_csv(dataFile1, encoding='utf-8', engine='python')


# 滑动平均回归
def move_average_re(data, window=5):
    v = data['value'].values.tolist()
    r = []
    # 去除异常值
    for i in range(len(v)):
        if v[i] < 0:
            v[i] = 0
        if v[i] > 100:
            v[i] = 100

    if math.isnan(v[-1]):
        r = [np.nan for _ in range(91)]

    else:
        for i in range(91):
            p = np.mean(v[-window:])
            r.append(p)
            v.append(p)
    return r


# 加权滑动平均回归
def weight_move_average_re(data, window=5):
    v = data['value'].values.tolist()
    if len(v) < window:
        for t in range(window-len(v)):
            v.append(v[-1])
    # 去除异常值
    for i in range(len(v)):
        if v[i] < 0:
            v[i] = 0
        if v[i] > 100:
            v[i] = 100

    r = []
    for i in range(91):
        weight = np.array(range(1, window+1))
        weight = np.reshape(weight/weight.sum(), [window, 1])
        p = np.array(v[-window:]).dot(weight)[0]
        r.append(p)
        v.append(p)
    return r


result = []
for name, group in train_data_f.groupby("id"):
    result.extend(move_average_re(group, window=5))

test_data_f["value"] = np.array(result)
test_data_f.to_csv("../weight_move_average_result_7.txt", index=False)
