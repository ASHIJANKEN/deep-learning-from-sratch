from and_gate import AND
from or_gate import OR
from nand_gate import NAND


def XOR(x1, x2):
  return AND(NAND(x1, x2), OR(x1, x2))


if __name__ == '__main__':
  print("x1:0 x2:0 -> " + str(XOR(0, 0)))
  print("x1:0 x2:1 -> " + str(XOR(0, 1)))
  print("x1:1 x2:0 -> " + str(XOR(1, 0)))
  print("x1:1 x2:1 -> " + str(XOR(1, 1)))
