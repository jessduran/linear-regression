# linear-regression

### Instructions

##### Create a program that calculates the cost (J) given a dataset.
I
ncluded is the input file "HousePricingRelationship.in". This file contains the dataset for this problem. Each row in the file contains one training example. For each row, there are n input features followed by 1 output value. All values are separated by commas ",".

##### Inside the program should be two functions:

*load_data(filename)*: This function reads input from a file (HousePricingRelationship.in) and loads the data into its respective containers (X and y; preferably Matrix objects). Make sure the size of the container is not hard coded (i.e. if the size of the dataset changes, so does the size of the containers)

*cost(x,y,theta)*: This function accepts X: the whole input data, y: the whole output data, theta: theta values representing one hypothesis. This function should compute the cost of the given hypothesis.