import numpy as np


def NAND(x1, x2):
  x = np.array([x1, x2])
  w = np.array([-0.5, -0.5])
  b = 0.8
  return 1 if (np.sum([x*w]) + b) > 0 else 0


if __name__ == '__main__':
  print("x1:0 x2:0 -> " + str(NAND(0, 0)))
  print("x1:0 x2:1 -> " + str(NAND(0, 1)))
  print("x1:1 x2:0 -> " + str(NAND(1, 0)))
  print("x1:1 x2:1 -> " + str(NAND(1, 1)))
