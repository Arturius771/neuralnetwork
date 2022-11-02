# https://www.youtube.com/watch?v=tMrbN67U9d4

import numpy as np

inputs = [1, 2, 3, 2.5]

weights = [[0.2, 0.8, -0.5, 1],
          [0.5, -0.91, 0.26, -0.5],
          [-0.26, -0.27, 0.17, 0.87]]

biases = [2, 3, 0.5]

output = np.dot(weights, inputs) + biases # Order of dot() inputs matters ( https://youtu.be/tMrbN67U9d4?t=974 )

print(output)


# layer_outputs = []

# for neuron_w, neuron_b in zip(weights, biases):
#   neuron_output = 0
#   for input, weight in zip(inputs, neuron_w):
#     neuron_output += input * weight
#   neuron_output += neuron_b
#   layer_outputs.append(neuron_output)

# print(layer_outputs)