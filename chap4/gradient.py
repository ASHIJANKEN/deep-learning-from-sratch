# coding: utf-8
import sys
import os
sys.path.append(os.pardir)  # 親ディレクトリのファイルをインポートするための設定
import numpy as np
import matplotlib.pyplot as plt
# from dataset.mnist import load_mnist
from numerical_gradient import numerical_gradient
# from two_layer_net import TwoLayerNet


def gradient_decent(f, init_x, lr=0.01, step_num=100):
  x = init_x
  for i in range(step_num):
    grad = numerical_gradient(f, x)
    # print(grad)
    x -= lr * grad

  return x


def function_2(x):
  return x[0]**2 + x[1]**2


if __name__ == '__main__':
  min_point = gradient_decent(function_2, np.array([5.0, 5.0]), lr=0.1)

  print("min: " + str(min_point))
  print("min value is " + str(function_2(min_point)))