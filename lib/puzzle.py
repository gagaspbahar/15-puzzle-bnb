import copy
import heapq as hq
import time

class PuzzleNode:
  test_dir = "test/"

  def __init__(self, level, cost, matrix):
    self.level = level
    self.matrix = matrix
    self.cost = cost
    self.moves = []
  
  def getMatrix(self):
    return self.matrix

  def getLevel(self):
    return self.level
  
  def getCost(self):
    return self.cost

  def getFunction(self):
    return self.level + self.cost

  def getMoves(self):
    return self.moves
  
  def appendMoves(self, direction):
    self.moves.append(direction)

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

  def calcCost(self):
    # using manhattan distance
    ans = 0
    for i in range(4):
      for j in range(4):
        num = getAbsolute(i,j) + 1
        if(num == 16):
          num = 0
        temp = getPosition(self.matrix, num)
        i1 = temp[0]
        j1 = temp[1]
        ans += abs(i1-i) + abs(j1-j)
    self.cost = ans
  
  def incrementLevel(self):
    self.level += 1

  def getChild(self):
    direction = ["up", "down", "left", "right"]
    children = []
    for i in range(4):
      temp = copy.deepcopy(self)
      status = temp.move(direction[i])
      if(status == 0):
        temp.incrementLevel()
        temp.calcCost()
        temp.appendMoves(direction[i])
        children.append(temp)
    return children
  
  def __lt__(self, other):
    return self.getFunction() <= other.getFunction()

def printMatrix(matrix):
  print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in matrix]))


def fileInput(filename):
  matrix = []
  try:
    file = open(PuzzleNode.test_dir + filename, "r")
  except:
    print("No file with the desired name found.")
    quit()
  for line in file:
    line = line.strip()
    matrix.append(line.split(" "))
  for i in range(len(matrix)):
    for j in range(len(matrix[i])):
      matrix[i][j] = int(matrix[i][j])
      if(matrix[i][j] == 16):
        matrix[i][j] = 0
  return matrix

def consoleInput():
  matrix = [list(map(int, input().split(" "))) for j in range(4)]
  return matrix


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
    currentKurang = 0
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
          currentKurang += 1
    print("kurang(" + str(n) + "):", currentKurang)
  return kurang

def reach(matrix):
  reachConst = findKurang(matrix) + findX(matrix)
  return reachConst
  
def isReachable(matrix):
  reachConst = reach(matrix)
  print("Reach constant is:", str(reachConst))
  if(reachConst % 2 == 1):
    print("The puzzle is not solvable.")
    return False
  else:
    return True

def solve(initialMatrix):
  if(isReachable(initialMatrix)):
    initialNode = PuzzleNode(0, 0, initialMatrix)
    initialNode.calcCost()
    queue = []
    hq.heapify(queue)
    hq.heappush(queue, initialNode)
    explored = []
    nodeCount = 0
    exploredNodeCount = 0
    now = time.time()
    while(queue):
      currentNode = hq.heappop(queue)
      if(currentNode.getCost() == 0):
        ans = currentNode.getMoves()
        break
      explored.append(currentNode)
      exploredNodeCount += 1
      children = currentNode.getChild()
      for child in children:
        hq.heappush(queue, child)
        nodeCount += 1
    done = time.time()
    printSolution(initialMatrix, ans)
    print("Number of nodes generated:", nodeCount)
    print("Explored nodes:", exploredNodeCount)
    print("Time taken:", str(done-now), "s")
    print("Solution:", ans)
    print("Number of steps:", len(ans))

def printSolution(initialMatrix, moves):
  matrix = PuzzleNode(0, 0, initialMatrix)
  for move in moves:
    print("Step:", move)
    if(move == "up"):
      matrix.moveUp()
    elif(move == "down"):
      matrix.moveDown()
    elif(move == "left"):
      matrix.moveLeft()
    elif(move == "right"):
      matrix.moveRight()
    printMatrix(matrix.getMatrix())
    print("=================")