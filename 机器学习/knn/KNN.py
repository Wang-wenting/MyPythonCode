from numpy import *
import operator

def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    diffMat = tile(inX, (dataSetSize, 1)) - dataSet
    sqDiffMat = diffMat**2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances**0.5
    sortedDistIndicies = distances.argsort()
    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    sortedClassCount = sorted(classCount.items(), key=lambda kv: kv[1], reverse=True)
    return sortedClassCount[0][0]

# group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
# label = ['A', 'A', 'B', 'B']
# # print(group.shape[0])
# # print(group.shape[1])
# # print(group.shape)
# a = array([1, 0.9])
# # b = tile(a, (4, 1))
# # c = (b-group)**2
# # print(c)
# # print(c.argsort())
# # print((c.sum(axis=1)**0.5).argsort())
# # print((c.sum(axis=1)**0.5))
# print(classify0(a, group, label, 2))