from numpy import *
import os
from knn.KNN import classify0


def img2vector(file_name):
    with open(file_name, 'r') as fr:
        a = fr.readlines()
        b = ''.join([line.strip() for line in a])
        return_vec = array(list(map(int, list(b)))).reshape(1, 1024)
    return return_vec


def hand_writing_class_test(training_path, testing_path, k):
    hw_labels = []
    training_file_list = os.listdir(training_path)
    m = len(training_file_list)
    training_mat = zeros((m, 1024))
    for i in range(m):
        file_name_str = training_file_list[i]
        file_str = file_name_str.split('.')[0]
        class_num_str = int(file_str.split('_')[0])
        hw_labels.append(class_num_str)
        training_mat[i, :] = img2vector(os.path.join(training_path, file_name_str))
    test_file_list = os.listdir(testing_path)
    error_count = 0
    mtest = len(test_file_list)
    for i in range(mtest):
        file_name_str = test_file_list[i]
        file_str = file_name_str.split('.')[0]
        class_num_str = int(file_str.split('_')[0])
        test_vector = img2vector(os.path.join(testing_path, file_name_str))
        classifier_result = classify0(test_vector, training_mat, hw_labels, k)
        print("预测结果为：%d，真实结果为：%d" % (classifier_result, class_num_str))
        if classifier_result != class_num_str:
            error_count += 1
    print("总错误数为 %d" % error_count)
    print("错误率为 %f" % (error_count / mtest))


if __name__ == '__main__':
    TRAIN_FILE_NAME = 'E:\\学习资料\\machinelearninginaction-master\\Ch02\\digits\\trainingDigits'
    TEST_FILE_NAME = 'E:\\学习资料\\machinelearninginaction-master\\Ch02\\digits\\testDigits'
    hand_writing_class_test(TRAIN_FILE_NAME, TEST_FILE_NAME, 3)


