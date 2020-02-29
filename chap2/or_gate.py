import numpy as np


def OR(x1, x2):
  x = np.array([x1, x2])
  w = np.array([0.1, 0.1])
  b = 0
  return 1 if (np.sum([x*w]) + b) > 0 else 0


if __name__ == '__main__':
  print("x1:0 x2:0 -> " + str(OR(0, 0)))
  print("x1:0 x2:1 -> " + str(OR(0, 1)))
  print("x1:1 x2:0 -> " + str(OR(1, 0)))
  print("x1:1 x2:1 -> " + str(OR(1, 1)))
