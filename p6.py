# https://www.youtube.com/watch?v=omz_NdFgWyU

import math
import numpy as np
import nnfs

nnfs.init()

layer_outputs = [[4.8, 1.21, 2.385],
                [5, -1, 2.0],
                [-1.5, 3.3, -0.8]]

E = math.e

exp_values = np.exp(layer_outputs)

print(np.sum(layer_outputs, axis=1, keepdims=True))

norm_values = exp_values / np.sum(exp_values, axis=1, keepdims=True)

print(norm_values)


# layer_outputs = [[4.8, 1.21, 2.385],
#                 [5, -1, 2.0],
#                 [-1.5, 3.3, -0.8]]

# E = math.e

# exp_values = np.exp(layer_outputs)

# print(exp_values)

# norm_base = sum(exp_values)

# norm_values = exp_values / np.sum(exp_values)

# print(norm_values)
# print(sum(norm_values))









# Non numpy normalisation and exponentiation values

# layer_outputs = [4.8, 1.21, 2.385]

# E = math.e

# exp_values = []

# for output in layer_outputs:
#   exp_values.append(E**output)

# print(exp_values)

# norm_base = sum(exp_values)

# norm_values = []

# for value in exp_values:
#   norm_values.append(value / norm_base)

# print(norm_values)
# print(sum(norm_values))