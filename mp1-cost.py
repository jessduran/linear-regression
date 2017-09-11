#!/usr/bin/python
import numpy as np

x = None
y = None
m = None
cost_history = np.matrix

def load_data (file):
    dataset = []
    for line in file:
        dataset.append([x.strip() for x in line.split(',')])
    mat = np.array(dataset)
    dMat = np.ones((mat.shape[0], mat.shape[1]+1), dtype=np.int)
    dMat[:,1:] = mat
    global x
    global y
    x = dMat[:, :-1]
    y = (dMat[:,[dMat.shape[1]-1]])

    # one theta example:
    theta = np.matrix('1; 3; 4')

    # print data
    # print ('x: \n', x, '\n')
    # print ('y: \n', y, '\n')
    # print ('theta: \n', theta, '\n')

    # get cost
    # cost(x, y, theta)
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
    global m
    m = x.shape[0]
    print ("Cost (J): ", cost)
    return

def gradientDescent(x, y, alpha, iters):
    n = 1
    tmp_theta = np.matrix('0;0;0')
    global cost_history

    while n < iters:
        tmp_cost = cost(x, y, tmp_theta)
        new_cost = [n, tmp_cost]
        # cost_history = np.vstack([cost_history, new_cost])
        for j in range(0, tmp_theta.shape[0]):
            H = np.matmul(x, tmp_theta);
            H_y = (np.subtract(H,y))
            summation = np.sum(H_y)
            new_theta = tmp_theta[j][0] - alpha * (1/m) * summation
            tmp_theta[j][0] = new_theta
            tmp_theta = np.matrix(tmp_theta)

        n = n + 1
        print(tmp_theta)

#
#
#
# def graph(cost_history):
#     # graph
#     # y = cost
#     pass


file = open("HousePricingRelationship.in", "r")
alpha = 0.34
iters = 100

load_data(file)
gradientDescent(x, y, alpha, iters)
