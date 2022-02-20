from math import log
from DecisionTree.tree_plotter import create_plot
import operator
import pickle
import random

def clac_shannon_ent(dataset):
    num_entries = len(dataset)
    label_counts = {}
    for feature in dataset:
        current_label = feature[-1]
        if current_label not in label_counts:
            label_counts[current_label] = 0
        label_counts[current_label] += 1
    shannon_ent = 0
    for key in label_counts.keys():
        prob = float(label_counts[key])/num_entries
        shannon_ent -= prob*log(prob, 2)
    return shannon_ent


def create_dataset():
    dataset = [[2, 1, 'maybe'], [1, 1, 'yes'], [1, 1, 'yes'], [1, 0, 'no'],
               [1, 0, 'no'], [0, 1, 'no']]
    labels = ['no surfacing', 'flippers']
    return dataset, labels


def split_dataset(dataset, axis, value):
    ret_dataset = []
    for feature in dataset:
        if feature[axis] == value:
            reduced_feature = feature[: axis]
            reduced_feature.extend(feature[axis+1:])
            ret_dataset.append(reduced_feature)
    return ret_dataset


def choose_best_feature2split(dataset):
    num_features = len(dataset[0]) - 1
    base_entropy = clac_shannon_ent(dataset)
    best_info_gain = 0
    best_feature = -1
    for i in range(num_features):
        fea_list = [example[i] for example in dataset]
        unique_vals = set(fea_list)
        new_entropy = 0
        for value in unique_vals:
            subdataset = split_dataset(dataset, i, value)
            prob = len(subdataset)/len(dataset)
            new_entropy += prob * clac_shannon_ent(subdataset)
        info_gain = base_entropy - new_entropy
        if info_gain > best_info_gain:
            best_info_gain = info_gain
            best_feature = i
    return best_feature


def majority_cnt(class_list):
    class_count = {}
    for vote in class_list:
        if vote not in class_count.keys():
            class_count[vote] = 0
        class_count[vote] += 1
    sorted_class_count = sorted(class_count.items(), key = operator.itemgetter(1), reverse=True)
    return sorted_class_count[0][0]


def create_tree(dataset, labels):
    class_list = [example[-1] for example in dataset]
    if class_list.count(class_list[0]) == len(class_list):
        return class_list[0]
    if len(dataset[0]) == 1:
        return majority_cnt(class_list)
    best_feature = choose_best_feature2split(dataset)
    best_feat_label = labels[best_feature]
    my_tree = {best_feat_label: {}}
    del(labels[best_feature])
    feat_values = [example[best_feature] for example in dataset]
    unique_vals = set(feat_values)
    for value in unique_vals:
        sub_labels = labels[:]
        my_tree[best_feat_label][value] = create_tree(split_dataset(dataset, best_feature, value), sub_labels)
    return my_tree


def classify(input_tree, feat_labels, test_vec):
    first_str = list(input_tree.keys())[0]
    second_dict = input_tree[first_str]
    feat_index = feat_labels.index(first_str)
    for key in second_dict.keys():
        if test_vec[feat_index] == key:
            if type(second_dict[key]).__name__ == 'dict':
                class_label = classify(second_dict[key], feat_labels, test_vec)
            else:
                class_label = second_dict[key]
    return class_label


def store_tree(in_tree, filename):
    """
    使用pickle模块存储决策树
    """
    with open(filename, 'wb') as f:
        pickle.dump(in_tree, f)


def grab_tree(filename):
    with open(filename, 'rb') as f:
        return pickle.load(f)


# my_data, label = create_dataset()
# labels = label[:]
# my_tree = create_tree(my_data, labels)
# store_tree(my_tree, 'classifier_storage.txt')
# print(grab_tree('classifier_storage.txt'))

if __name__ == '__main__':
    FILE_NAME = 'E:\\学习资料\\machinelearninginaction-master\\Ch03\\lenses.txt'
    with open(FILE_NAME, 'r') as f:
        lenses = [inst.strip().split('\t') for inst in f.readlines()]
    lenses_labels = ['age', 'prescript', 'astigmatic', 'tearRate']
    lenses_tree = create_tree(lenses, lenses_labels)
    create_plot(lenses_tree)

