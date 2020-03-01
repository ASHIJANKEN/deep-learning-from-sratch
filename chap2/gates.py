import numpy as np


def AND(x1, x2):
  x = np.array([x1, x2])
  w = np.array([0.5, 0.5])
  b = -0.8
  return 1 if (np.sum([x*w]) + b) > 0 else 0


def NAND(x1, x2):
  x = np.array([x1, x2])
  w = np.array([-0.5, -0.5])
  b = 0.8
  return 1 if (np.sum([x*w]) + b) > 0 else 0


def OR(x1, x2):
  x = np.array([x1, x2])
  w = np.array([0.1, 0.1])
  b = 0
  return 1 if (np.sum([x*w]) + b) > 0 else 0


def XOR(x1, x2):
  return AND(NAND(x1, x2), OR(x1, x2))


if __name__ == '__main__':
  print("AND gate---------------------")
  print("x1:0 x2:0 -> " + str(AND(0, 0)))
  print("x1:0 x2:1 -> " + str(AND(0, 1)))
  print("x1:1 x2:0 -> " + str(AND(1, 0)))
  print("x1:1 x2:1 -> " + str(AND(1, 1)))
  print("")

  print("NAND gate---------------------")
  print("x1:0 x2:0 -> " + str(NAND(0, 0)))
  print("x1:0 x2:1 -> " + str(NAND(0, 1)))
  print("x1:1 x2:0 -> " + str(NAND(1, 0)))
  print("x1:1 x2:1 -> " + str(NAND(1, 1)))
  print("")

  print("OR gate---------------------")
  print("x1:0 x2:0 -> " + str(OR(0, 0)))
  print("x1:0 x2:1 -> " + str(OR(0, 1)))
  print("x1:1 x2:0 -> " + str(OR(1, 0)))
  print("x1:1 x2:1 -> " + str(OR(1, 1)))
  print("")

  print("XOR gate---------------------")
  print("x1:0 x2:0 -> " + str(XOR(0, 0)))
  print("x1:0 x2:1 -> " + str(XOR(0, 1)))
  print("x1:1 x2:0 -> " + str(XOR(1, 0)))
  print("x1:1 x2:1 -> " + str(XOR(1, 1)))
  print("")
