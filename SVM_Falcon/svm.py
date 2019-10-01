import sys
from sklearn.datasets import load_digits  #
import pylab as pl
from sklearn.model_selection import train_test_split  #
from sklearn.preprocessing import StandardScaler  #
from sklearn.svm import LinearSVC
from sklearn.metrics import classification_report
from ReadImage import compressimage
import time

def compress():
    # the image will be compressed from 2048x1536 to 409x307

    start = time.time()
    train0 = compressimage('train/0')
    print(train0)

    train1 = compressimage('train/1')
    print(train1)
    valid0 = compressimage('valid/v0')
    print(valid0)
    valid1 = compressimage('valid/v1')
    print(valid1)

    test0 = compressimage('test/t0')
    print(test0)
    test1 = compressimage('test/t1')
    print(test1)
    end = time.time()
    print(end - start)

if __name__=="__main__":
    # compress()
    '''1202 t0 1856 t1
        755 v0 1179 v1
        319 test0   293 test1
        306.7839186191559'''
    # digits = load_digits()
    # print(digits.data.shape)
    #
    # # 分割数据
    # X_train, X_test, Y_train, Y_test = train_test_split(digits.data, digits.target, test_size=0.25, random_state=33)
    #
    # ss = StandardScaler()
    # X_train = ss.fit_transform(X_train)
    # X_test = ss.transform(X_test)
    #
    # lsvc = LinearSVC()
    # lsvc.fit(X_train, Y_train)
    #
    # Y_predict = lsvc.predict(X_test)