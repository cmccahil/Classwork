# hw3-neuralnets
HW3: Neural Networks
Research Questions
Note: since we were unable to get our neural network to work correctly, we used the tensorflow nn.py implementation from class.
1. Seed: 12345 Training Percent: 0.6
   a: The accuracy was 90.74%.
   b: The logistic accuracy was 63.22%.
   c: For the neural network, the confidence interval is [0.8527, 0.9621] and for the logistic regression it is [0.5309, 0.7335]. This means the neural network with just one more neuron than the logistic regression is more accurate by a wide margin.
2. Seed: 12345
   a: see accuracy_chart.jpg
   b: The accuracy increased until 10 neurons but then it decreased. This is probably because with more neurons, the network can start overfitting and learn specific trends in the training set which don't continue in the validation set.
   
This assignment contains four data sets that are based on four publicly available benchmarks, each representing a binary classification task:

1. monks1.csv: A data set describing two classes of robots using all nominal attributes and a binary label.  This data set has a simple rule set for determining the label: if head_shape = body_shape ∨ jacket_color = red, then yes (1), else no (0). Each of the attributes in the monks1 data set are nominal.  Monks1 was one of the first machine learning challenge problems (http://www.mli.gmu.edu/papers/91-95/91-28.pdf).  This data set comes from the UCI Machine Learning Repository:  http://archive.ics.uci.edu/ml/datasets/MONK%27s+Problems

2. seismic.csv: A data set of measurements describing seismic activity in the earth, measured from a wall in a Polish coal mine.  The task in this data set is to predict whether there will be a high energy seismic event within the next 8 hours.  The 18 attributes have a mix of types of values: 4 are nominal attributes, and the other 14 are continuous.  The label is a 0 if there was no high energy seismic event in the next 8 hours, and a 1 if there was such an event.  This data set comes the UCI Machine Learning Repository: https://archive.ics.uci.edu/ml/datasets/seismic-bumps

3. mnist_5v8.csv: A data set of optical character recognition of numeric digits from images.  The task in this data set is to predict whether a handwritten number is a “5” or an “8”.  Each instance represents a different grayscale 28x28 pixel image of a handwritten numeric digit.  The attributes are the intensity values of the 784 pixels. Each attribute is ordinal (treat them as continuous for the purpose of this assignment).  The label is a 0 if the handwritten number is a “5”, and a 1 if the handwritten number is an “8”.  This version of MNIST contains 100 instances of the handwritten numeric digits “5” and “8”, randomly sampled from the original training data for MNIST.  The overall MNIST data set is one of the main benchmarks in machine learning: http://yann.lecun.com/exdb/mnist/.  It was converted to CSV file using the python code provided at: https://quickgrid.blogspot.com/2017/05/Converting-MNIST-Handwritten-Digits-Dataset-into-CSV-with-Sorting-and-Extracting-Labels-and-Features-into-Different-CSV-using-Python.html
