import numpy as np
import matplotlib.pylab as plt


def step_function(x):
  y = x > 0
  return y.astype(np.int)


def sigmoid(x):
  return 1 / (1 + np.exp(-x))


def relu(x):
  return np.maximum(0, x)


def identity_function(x):
  return x


def softmax(x):
  max = np.max(x)
  tmp = np.exp(x - max)
  return tmp / np.sum(tmp)


if __name__ == '__main__':
  x = np.arange(-5, 5, 0.1)
  y = step_function(x)
  z = sigmoid(x)
  w = relu(x)
  u = identity_function(x)
  v = softmax(x)
  plt.plot(x, y, label="step")
  plt.plot(x, z, linestyle="--", label="sigmoid")
  plt.plot(x, u, linestyle="dashdot", label="identity")
  plt.plot(x, v, label="softmax")
  plt.plot(x, w, linestyle=":", label="relu")
  plt.ylim(-2.1, 2.1)
  plt.legend()
  plt.show()
