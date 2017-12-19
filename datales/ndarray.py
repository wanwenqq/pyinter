#coding = utf-8

import numpy as np


if __name__ == '__main__':
    # x = np.array([1,2,3,4])
    # print(x)

    # print(np.arange(10))
    # print(np.ones((3,6)))
    # print(np.zeros((3,6)))
    # print(np.eye(5))

    # x = np.ones([2,3,4])
    # print(x)
    # print(x.shape)


    # x =  np.full((2,4),5)
    # print(x)

    # x = np.linspace(1,10,4)
    # print(x)

    # x = np.ones((2,3,4),dtype=np.int32)
    # # print(x)
    # y = x.reshape((3,8))
    # # print(y)

    # z = x.resize((3,8))
    # print(x)
    # a= x.astype(np.float)
    # print(a)

    # x = np.full((2,3,4),5,dtype=np.int32)
    # print(x)
    # y= x.tolist()
    # print(y)

    # ----------------------

    # a = np.array([9,8,7,6,5])
    # # print(a[2])
    # print(a[1:4:2])


    a = np.arange(24).reshape((2,3,4))
    # print(a)
    print(a[1,2,3])
    print(a[0,1,2])
    print(a[-1,-2,-3])
    