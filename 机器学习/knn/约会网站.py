from numpy import *
import matplotlib
import matplotlib.pyplot as plt
from knn.KNN import classify0


def file2matrix(filename):
    """
    用于读取数据
    :param filename:
    :return:
    """
    with open(filename, 'r') as fr:
        arrayOLines = fr.readlines()
        numberOfLines = len(arrayOLines)
        returnMat = zeros((numberOfLines, 3))
        classLabel = []
        index = 0
        for line in arrayOLines:
            line = line.strip()
            listFromline = line.split('\t')
            returnMat[index, :] = listFromline[0: 3]
            classLabel.append(int(listFromline[-1]))
            index += 1
    return returnMat, classLabel


def mscatter(x, y, ax=None, m=None, **kw):
    """
    用于绘制散点图，可以实现不同类别的点具有不同的形状
    :param x:
    :param y:
    :param ax:
    :param m: 形状列表
    :param kw:
    :return:
    """
    import matplotlib.markers as mmarkers
    if not ax:
        ax = plt.gca()
    sc = ax.scatter(x, y, **kw)
    if (m is not None) and (len(m)==len(x)):
        paths = []
        for marker in m:
            if isinstance(marker, mmarkers.MarkerStyle):
                marker_obj = marker
            else:
                marker_obj = mmarkers.MarkerStyle(marker)
            path = marker_obj.get_path().transformed(
                        marker_obj.get_transform())
            paths.append(path)
        sc.set_paths(paths)
    return sc


def auto_norm(dataset):
    minvals = dataset.min(0)
    maxvals = dataset.max(0)
    ranges = maxvals - minvals
    # norm_dataset = zeros(shape(dataset))
    m = dataset.shape[0]
    norm_dataset = dataset - tile(minvals, (m, 1))
    norm_dataset = norm_dataset / tile(ranges, (m, 1))
    return norm_dataset, ranges, minvals


def dating_class_test(k=3):
    ratio = 0.2
    dating_datamat, dating_labels = file2matrix(FILENAME)
    norm_mat, norm_ranges, min_vals = auto_norm(dating_datamat)
    m = norm_mat.shape[0]
    num_test_vecs = int(m*ratio)
    error_count = 0
    for i in range(num_test_vecs):
        classifier_result = classify0(norm_mat[i, :], norm_mat[num_test_vecs: m, :],
                                      dating_labels[num_test_vecs: m], k)
        print("预测结果为：%d，真实结果为：%d" % (classifier_result, dating_labels[i]))
        if classifier_result != dating_labels[i]:
            error_count += 1
    print("错误率为 %f" % (error_count/num_test_vecs))


if __name__ == '__main__':
    FILENAME = 'E:\\学习资料\\machinelearninginaction-master\\Ch02\\datingTestSet2.txt'
    dating_class_test(6)




# 绘制散点图
# fig = plt.figure()
# ax = fig.add_subplot(111)
# m = {1: 'o', 2: 's', 3: '+'}
# color = {1: 'r', 2: 'b', 3: 'y'}
# cm = list(map(lambda x: m[x], dating_labels))#将相应的标签改成对应的marker
# c_color = list(map(lambda x: color[x], dating_labels))#将相应的标签改成对应的marker
# scatter = mscatter(dating_datamat[:, 1], dating_datamat[:, 0], c=c_color, m=cm, ax=ax, cmap=plt.cm.RdYlBu)
# plt.show()

