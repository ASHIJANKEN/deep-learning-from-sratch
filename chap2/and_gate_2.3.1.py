def AND(x1, x2):
  w1, w2, theta = 0.5, 0.5, 0.8
  tmp = x1 * w1 + x2 * w2
  return 1 if tmp > theta else 0


if __name__ == '__main__':
  print("x1:0 x2:0 -> " + str(AND(0, 0)))
  print("x1:0 x2:1 -> " + str(AND(0, 1)))
  print("x1:1 x2:0 -> " + str(AND(1, 0)))
  print("x1:1 x2:1 -> " + str(AND(1, 1)))
