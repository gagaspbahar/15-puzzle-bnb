class Tree:
  def __init__(self):
    self

class Puzzle:
  test_dir = "test/"
  matrix = []

  def __init__(self, level, cost, matrix):
    self.level = level
    self.matrix = matrix
  
  def getMatrix(self):
    return self.matrix

  def getLevel(self):
    return self.level
  
  def getCost(self):
    return self.cost

  def fileInput(self, filename):
    self.matrix = []
    try:
      file = open(Puzzle.test_dir + filename, "r")
    except:
      print("No file with the desired name found.")
    for line in file:
      line = line.strip()
      self.matrix.append(line.split(" "))
    for i in range(len(self.matrix)):
      for j in range(len(self.matrix[i])):
        self.matrix[i][j] = int(self.matrix[i][j])
        if(self.matrix[i][j] == 16):
          self.matrix[i][j] = 0
    return self.matrix

  def moveUp(self):
    for i in range(len(self.matrix)):
      for j in range(len(self.matrix[i])):
        if(self.matrix[i][j] == 0):
          if(i == 0):
            return -1
          else:
            self.matrix[i][j] = self.matrix[i-1][j]
            self.matrix[i-1][j] = 0
            return 0

  def moveDown(self):
    for i in range(len(self.matrix)):
      for j in range(len(self.matrix[i])):
        if(self.matrix[i][j] == 0):
          if(i == len(self.matrix)-1):
            return -1
          else:
            self.matrix[i][j] = self.matrix[i+1][j]
            self.matrix[i+1][j] = 0
            return 0

  def moveLeft(self):
    for i in range(len(self.matrix)):
      for j in range(len(self.matrix[i])):
        if(self.matrix[i][j] == 0):
          if(j == 0):
            return -1
          else:
            self.matrix[i][j] = self.matrix[i][j-1]
            self.matrix[i][j-1] = 0
            return 0

  def moveRight(self):
    for i in range(len(self.matrix)):
      for j in range(len(self.matrix[i])):
        if(self.matrix[i][j] == 0):
          if(j == len(self.matrix[i])-1):
            return -1
          else:
            self.matrix[i][j] = self.matrix[i][j+1]
            self.matrix[i][j+1] = 0
            return 0

  def move(self, direction):
    if(direction == "up"):
      status = self.moveUp()
    elif(direction == "down"):
      status = self.moveDown()
    elif(direction == "left"):
      status = self.moveLeft()
    elif(direction == "right"):
      status = self.moveRight()
    else:
      print("Invalid direction.")
    return status

  def printMatrix(self):
    for i in range(len(self.matrix)):
      for j in range(len(self.matrix[i])):
        print(self.matrix[i][j], end=" ")
      print()

  def cost(self):
    # using manhattan distance
    ans = 0
    for i in range(4):
      for j in range(4):
        num = getAbsolute(i,j)
        temp = getPosition(self.matrix, num)
        i1 = temp[0]
        j1 = temp[1]
        ans += abs(i1-i) + abs(j1-j)
    return ans

def findX(matrix):
  for i in range(4):
    for j in range(4):
      if(matrix[i][j] == 0):
        if((i%2 == 0 and j%2 == 1) or (i%2 == 1 and j%2 == 0)):
          return 1
        else:
          return 0

def getAbsolute(i, j):
  return i*4 + j

def getPosition(matrix, n):
  for i in range(4):
    for j in range(4):
      if(matrix[i][j] == n):
        return [i, j]

def findKurang(matrix):
  # Banyaknya ubin bernomor j sedemikian sehingga j < i dan POSISI(j) > POSISI(i)
  kurang = 0
  for n in range(16):
    for i in range(4):
      for j in range(4):
        # n itu i
        # getabsolute i j itu j
        m = getAbsolute(i, j)
        check = 16 if n == 0 else n
        temp = getPosition(matrix, n)
        checkI = temp[0]
        checkJ = temp[1]
        tempM = getPosition(matrix, m)
        checkMI = tempM[0]
        checkMJ = tempM[1]
        m = 16 if m == 0 else m
        if((m < check) and (getAbsolute(checkMI, checkMJ) > getAbsolute(checkI, checkJ))):
          kurang += 1
    print(n, kurang)
  return kurang

def isReachable(matrix):
  reach = findKurang(matrix) + findX(matrix)
  return reach % 2 == 0