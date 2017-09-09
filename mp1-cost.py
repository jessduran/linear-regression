#!/usr/bin/python

import numpy as np

def load_data (file):
    dataset = []
    for line in file:
        dataset.append([x.strip() for x in line.split(',')])
    # convert dataset to a matrix
    mat = np.array(dataset)

    # add a bias column
    dMat = np.ones((mat.shape[0], mat.shape[1]+1), dtype=np.int)
    dMat[:,1:]=mat

    # load data to respective containers
    x = dMat[:, :-1]
    y = (dMat[:,[dMat.shape[1]-1]])

    # one theta example:
    theta = np.matrix('1; 3; 4')

    # get theta
    # theta = get_theta(x.shape[1]);

    # print data
    print ('x: \n', x, '\n')
    print ('y: \n', y, '\n')
    print ('theta: \n', theta, '\n')

    # get cost
    cost(x, y, theta)
    return

def get_theta(n):
    print ('\nSeparate columns using commas (,) and rows using semi-colons (;) \n(i.e.: 1, 2; 3, 4)')
    theta = np.matrix(input())

    while not (theta.shape[0] == n and theta.shape[1] == 1):
        print('Not a valid hypothesis')
        print ('\nSeparate columns using commas (,) and rows using semi-colons (;) \n(i.e.: 1, 2; 3, 4)')
        theta = np.matrix(input())
        if (theta.shape[0] == n):
            return theta
    return theta

def cost(x, y, theta):
    print ("calculating cost...")
    # cross multiply x and theta
    H = np.matmul(x, theta);

    # subtract y from H
    H_y = (np.subtract(H,y))

    # square the result
    H_ySquared = np.power(H_y, 2, dtype='int64')

    # get the summation of H
    summation = np.sum(H_ySquared)

    # compute cost
    cost = summation / (2 * x.shape[0])
    print ("Cost (J): ", cost)
    return

file = open("HousePricingRelationship.in", "r")
load_data(file);
