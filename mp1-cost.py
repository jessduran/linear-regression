#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt


x = None
y = None

def load_data (file):
    dataset = []
    for line in file:
        dataset.append([x.strip() for x in line.split(',')])
    mat = np.array(dataset)
    dMat = np.ones((mat.shape[0], mat.shape[1]+1), dtype='int64')
    dMat[:,1:] = mat
    global x
    global y
    x = dMat[:, :-1]
    y = (dMat[:,[dMat.shape[1]-1]])

    return

def cost(x, y, theta):
    H = np.power((np.subtract(np.matmul(x, theta),y)), 2)
    summation = np.sum(H)
    cost = summation / (2 * x.shape[0])
    return cost

def gradientDescent(x, y, alpha, iters):
    n = 0
    tmp_theta = np.matrix('0;0;0')
    cost_history = []

    for i in range(0, iters):
        H = (np.subtract(np.matmul(x, tmp_theta),y))
        tmp_theta = tmp_theta - (alpha / float(x.shape[0])) * x.T * (H)
        cost_history.append(cost(x, y, tmp_theta))

    print(tmp_theta)
    return cost_history

def graph(cost_history):
    plt.plot(np.arange(0,len(cost_history)), cost_history)
    plt.ylabel('cost')
    plt.xlabel('iterations')
    plt.show()


file = open("HousePricingRelationship.in", "r")
alpha = 0.00000005
iters = 100

load_data(file)
cost_history = gradientDescent(x, y, alpha, iters)
graph(cost_history)

