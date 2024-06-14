class Time:
  def __init__(self, h=0, m=0):
    self.__h = h
    self.__m = m

  def display(self):
    print(f'{self.__h:02d}:{self.__m:02d}')

  def add(self, obj):
    self.__h += obj.__h
    self.__m += obj.__m
    if self.__m >= 60:
      self.__h += self.__m // 60
      self.__m %= 60
    return Time(self.__h, self.__m)

  @staticmethod
  def isvalid(h, m):
    return (0 <= h < 24 and 0 <= m <60)

def main():
  t1 = Time(9)
  t2 = Time(9, 30)

  t1.display()
  t2.display()

  later = t1.add(Time(1, 15))
  later.display()

  if Time.isvalid(25, 0):
    print('유효한 시각')
  else:
    print('유효하지 않은 시각')

# main program
if __name__ == '__main__':
  main()