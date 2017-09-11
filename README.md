# Linear Regression

### Instructions

##### Create a program that calculates the cost (J) given a dataset.
Included is the input file "HousePricingRelationship.in". This file contains the dataset for this problem. Each row in the file contains one training example. For each row, there are n input features followed by 1 output value. All values are separated by commas ",".

##### Inside the program should be two functions:

*load_data(filename)*: This function reads input from a file (HousePricingRelationship.in) and loads the data into its respective containers (X and y; preferably Matrix objects). Make sure the size of the container is not hard coded (i.e. if the size of the dataset changes, so does the size of the containers)

*cost(x,y,theta)*: This function accepts X: the whole input data, y: the whole output data, theta: theta values representing one hypothesis. This function should compute the cost of the given hypothesis.

# Gradient Descent

### Instructions

###### In this MP, you should implement gradient descent in a linear regression algorithm. Inside your MP should the functions:

*gradientDescent(X,y,alpha,iters)*: this function should calculate the best theta values (theta values with the smallest cost) given the values X and y from the dataset and the values alpha and iters chosen by you. The gradient descent should run for iters number of iterations. Remember that if you choose incorrect values (too big or too small) for alpha the function will not be able to reach the best theta values. While the gradient descent iterates, you should keep a record for the cost for each iteration. This record (cost_history) will be used in the function graph(cost_history).

*graph(cost_history)*: this function should graph cost (y-axis) versus iterations (x-axis). It should show how the cost changes as the gradient descent progresses with more iteration (see attached files for more details).
