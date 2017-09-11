#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt


x = None
y = None
m = None

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

    # get cost
    # cost(x, y, theta)
    return

def cost(x, y, theta):
    H = np.matmul(x, theta);
    H_y = (np.subtract(H,y))
    H_ySquared = np.power(H_y, 2, dtype='int64')
    summation = np.sum(H_ySquared)
    cost = summation / (2 * x.shape[0])
    global m
    m = x.shape[0]
    return cost

def gradientDescent(x, y, alpha, iters):
    n = 1
    tmp_theta = np.matrix('0;0;0')
    cost_history = np.empty((0,2))
    while n < iters:
        tmp_cost = cost(x, y, tmp_theta)
        new_cost = [n, tmp_cost]
        print (new_cost)
        cost_history = np.vstack((cost_history, new_cost))
        for j in range(0, tmp_theta.shape[0]):
            H = np.matmul(x, tmp_theta);
            H_y = (np.subtract(H,y)) 
            summation = np.sum(H_y)
            new_theta = tmp_theta[j][0] - (alpha * (summation / m))
            tmp_theta[j][0] = new_theta
            tmp_theta = np.matrix(tmp_theta)
        n = n + 1

    print (cost_history)
    graph(cost_history)
    return

def graph(cost_history):
    plt.plot(cost_history)
    plt.ylabel('cost')
    plt.xlabel('iterations')
    plt.show()


file = open("HousePricingRelationship.in", "r")
alpha = 0.5
iters = 100

load_data(file)
gradientDescent(x, y, alpha, iters)
