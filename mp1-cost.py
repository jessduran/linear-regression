#!/usr/bin/python
import numpy as np

x, y, m

def load_data (file):
    dataset = []
    for line in file:
        dataset.append([x.strip() for x in line.split(',')])
    mat = np.array(dataset)
    dMat = np.ones((mat.shape[0], mat.shape[1]+1), dtype=np.int)
    dMat[:,1:] = mat
    x = dMat[:, :-1]
    y = (dMat[:,[dMat.shape[1]-1]])

    # one theta example:
    theta = np.matrix('1; 3; 4')

    # print data
    print ('x: \n', x, '\n')
    print ('y: \n', y, '\n')
    print ('theta: \n', theta, '\n')

    # get cost
    cost(x, y, theta)
    return

# def get_theta(n):
#     print ('\nSeparate columns using commas (,) and rows using semi-colons (;) \n(i.e.: 1, 2; 3, 4)')
#     theta = np.matrix(input())
#
#     while not (theta.shape[0] == n and theta.shape[1] == 1):
#         print('Not a valid hypothesis')
#         print ('\nSeparate columns using commas (,) and rows using semi-colons (;) \n(i.e.: 1, 2; 3, 4)')
#         theta = np.matrix(input())
#         if (theta.shape[0] == n):
#             return theta
#     return theta

def cost(x, y, theta):
    print ("calculating cost...")
    H = np.matmul(x, theta);
    H_y = (np.subtract(H,y))
    H_ySquared = np.power(H_y, 2, dtype='int64')
    summation = np.sum(H_ySquared)
    cost = summation / (2 * x.shape[0])
    m = x.shape[0]
    print ("Cost (J): ", cost)
    return

def gradientDescent(x, y, alpha, iters):


file = open("HousePricingRelationship.in", "r")
alpha = 1000
iters = 100

load_data(file)
gradientDescent(x, y, alpha, iters)
