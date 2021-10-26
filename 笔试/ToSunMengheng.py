# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, roc_auc_score, precision_score
import os

os.getcwd()
os.chdir('/Users/rqz233/Downloads/')
df1 = pd.read_excel('data3.xlsx')
df2 = df1.copy(deep='True')

df2['grade'] = df2['grade'].astype(str)
df2['board'] = df2['board'].astype(str)


def encoder(df, int_col, cate_col):
    contain_column = len(df.columns) - len(cate_col)
    new_df = pd.get_dummies(data=df, columns=cate_col, dummy_na=True)
    digit_data = df[int_col]
    df_new = pd.concat([digit_data, new_df.iloc[:, contain_column:]], axis=1)
    return df_new


def encoder1(df, int_col, cate_col):
    contain_column = len(df.columns) - len(cate_col)
    new_df = pd.get_dummies(data=df, columns=cate_col, dummy_na=True)
    digit_data = df[int_col]
    new_digit = StandardScaler().fit(digit_data).transform(digit_data)
    new_digit = pd.DataFrame(new_digit, columns=digit_data.columns)
    df_new = pd.concat([new_digit, new_df.iloc[:, contain_column:]], axis=1)
    return df_new


int_cols = ['search_cnt', 'hit_cnt', 'hit_item_cnt', 'video_cnt',
            'comment_cnt', 'comment_good_cnt', 'comment_bad_cnt', 'bookmark_cnt',
            'share_cnt', 'exercise_cnt', 'finish_cnt', 'comment_ordinary_cnt',
            'avg_finish_ratio', 'item_bad_cnt', 'item_good_cnt', 'quiz_finish_cnt',
            'quiz_start_cnt', 'is_ret']
cate_cols = ['grade', 'board', 'device_brand', 'media_source', 'activation_adset', 'true_state']
cate_cols2 = ['grade', 'board', 'media_source']

df_ready = encoder(df2, int_cols, cate_cols2)
del df_ready['grade_nan']
del df_ready['board_nan']
# model part


y = df_ready['is_ret']
x = df_ready.drop(['is_ret'], axis=1)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

lr = LogisticRegression(random_state=42, penalty='l2')

lr.fit(x_train, y_train)
y_pred = lr.predict(x_test)
print(classification_report(y_test, y_pred))

print('auc=', accuracy_score(y_test, y_pred))
print('roc_auc=', roc_auc_score(y_test, y_pred))
print('confusion', confusion_matrix(y_test, y_pred))
print('precision=', precision_score(y_test, y_pred))
##need to scale


feature_importance = pd.DataFrame(np.abs(lr.coef_), columns=x_train.columns)

##model2
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

dt = DecisionTreeClassifier(max_depth=4, random_state=42, max_features='sqrt')

dt.fit(x_train, y_train)
y_pred = dt.predict(x_test)

feat_importance = dt.tree_.compute_feature_importances(normalize=False)
result = np.transpose(pd.DataFrame(feat_importance))
result.columns = x_train.columns

print("feat importance = " + str(feat_importance))

print(classification_report(y_test, y_pred))

print('auc=', accuracy_score(y_test, y_pred))
print('roc_auc=', roc_auc_score(y_test, y_pred))
print('confusion', confusion_matrix(y_test, y_pred))
print('precision=', precision_score(y_test, y_pred))

##importance  = dt.feature_importance_
##feat_importance = pd.Serise(importance,index=x_train.columns)


from sklearn.tree.export import export_graphviz
from IPython.display import Image
import pydotplus
from io import StringIO

##feat_importance = dt.tree_.compute_feature_importances(normalize=False)
##print("feat importance = " + str(feat_importance))


dot_data = StringIO()
export_graphviz(
    dt, feature_names=x_train.columns,
    out_file=dot_data,
    filled=True,
    rounded=True,
    special_characters=True
)
graph_1 = pydotplus.graph_from_dot_data(dot_data.getvalue())
Image(graph_1.create_png())

graph_1.write_png("out1.png")

########

rf = RandomForestClassifier(max_depth=4, random_state=42, max_features='sqrt')

rf.fit(x_train, y_train)
y_pred = rf.predict(x_test)

importance = rf.feature_importances_
importance1 = pd.DataFrame(importance, index=x_train.columns, columns=["Importance"])

print("feat importance = " + str(feat_importance))

print(classification_report(y_test, y_pred))

print('auc=', accuracy_score(y_test, y_pred))
print('roc_auc=', roc_auc_score(y_test, y_pred))
print('confusion', confusion_matrix(y_test, y_pred))
print('precision=', precision_score(y_test, y_pred))
