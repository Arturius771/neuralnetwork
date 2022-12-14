# https://www.youtube.com/watch?v=TEWy9vZcxW4

import numpy as np

np.random.seed(0) # use this to make random number same as video

X = [[1, 2, 3, 2.5],
    [2, 5, -1, 2.0],
    [-1.5, 2.7, 3.3, -0.8]]


class Layer_Dense:
  def __init__(self, n_inputs, n_neurons) -> None:
    self.weights = 0.10 *  np.random.randn(n_inputs, n_neurons)
    self.biases = np.zeros((1, n_neurons))
  def forward(self, inputs) -> None: 
    self.output = np.dot(inputs, self.weights) + self.biases


layer1 = Layer_Dense(4,5)
layer2 = Layer_Dense(5,2)

layer1.forward(X)
# print(layer1.output)
layer2.forward(layer1.output)
print(layer2.output)





# inputs = [[1, 2, 3, 2.5],
#           [2, 5, -1, 2.0],
#           [-1.5, 2.7, 3.3, -0.8]]

# weights = [[0.2, 0.8, -0.5, 1],
#            [0.5, -0.91, 0.26, -0.5],
#            [-0.26, -0.27, 0.17, 0.87]]

# biases = [2, 3, 0.5]

# output = np.dot(inputs, np.array(weights).T) + biases # Order of dot() inputs matters ( https://youtu.be/tMrbN67U9d4?t=974 )

# print(output)