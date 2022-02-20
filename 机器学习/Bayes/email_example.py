import re
from Bayes.bayes import *
import random
import numpy as np


def text_parse(big_string):
    list_of_tokens = re.split(r'\W*', big_string)
    return [tok.lower() for tok in list_of_tokens if len(tok) > 2]


def spam_test():
    doc_list = []
    class_list = []
    full_text = []
    for i in range(1, 26):
        try:
            filename = 'E:\\学习资料\\machinelearninginaction-master\\Ch04\\email\\spam\\%d.txt' % i
            with open(filename, encoding='utf-8') as f:
                a = f.read()
                word_list = text_parse(a)
                doc_list.append(word_list)
                full_text.extend(word_list)
                class_list.append(1)
            filename = 'E:\\学习资料\\machinelearninginaction-master\\Ch04\\email\\ham\\%d.txt' % i
            with open(filename, encoding='utf-8') as f:
                a = f.read()
                word_list = text_parse(a)
                doc_list.append(word_list)
                full_text.extend(word_list)
                class_list.append(0)
        except:
            print(i)
    vocab_list = create_vocab_list(doc_list)
    training_set = list(range(50))
    test_set = []
    for i in range(10):
        rand_index = int(random.uniform(0, len(training_set)))
        test_set.append(training_set[rand_index])
        del(training_set[rand_index])
    train_mat = []
    train_classes = []
    for doc_index in training_set:
        train_mat.append(set_of_words2vec(vocab_list, doc_list[doc_index]))
        train_classes.append(class_list[doc_index])
    p0v, p1v, p_spam = train_nb0(np.array(train_mat), np.array(train_classes))
    error_count = 0
    for doc_index in test_set:
        word_vector = set_of_words2vec(vocab_list, doc_list[doc_index])
        if classify_nb(np.array(word_vector), p0v, p1v, p_spam) != class_list[doc_index]:
            error_count += 1

    print('The error rate is :', error_count/len(test_set))


spam_test()