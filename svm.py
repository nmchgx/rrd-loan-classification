#! python2
# coding: utf-8
import numpy as np
import pandas as pd
from sklearn import svm
from sklearn.model_selection import train_test_split


def run(x, y, test_size=0.6):
    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=test_size, random_state=1)

    clf = svm.SVC(C=0.8, kernel='rbf', gamma=20, decision_function_shape='ovr')
    clf.fit(x_train, y_train.ravel())

    temp_x = pd.DataFrame(x_train)
    temp_y = pd.DataFrame(y_train)

    train_score = clf.score(x_train, y_train)
    test_score = clf.score(x_test, y_test)
    a_score = clf.score(temp_x[temp_y[0] == 1], y_train[temp_y[0] == 1])
    b_score = clf.score(temp_x[temp_y[0] == 0], y_train[temp_y[0] == 0])
    c_score = clf.score(temp_x[temp_y[0] == 2], y_train[temp_y[0] == 2])
    return train_score, test_score, a_score, b_score, c_score
