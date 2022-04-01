class Puzzle:
  test_dir = "test/"
  matrix = []

  def __init__(self):
    self.matrix = self.fileInput("test.txt")

  def fileInput(self, filename):
    matrix = []
    try:
      file = open(Puzzle.test_dir + filename, "r")
    except:
      print("No file with the desired name found.")
    for line in file:
      line = line.strip()
      matrix.append(line.split(" "))
    return matrix
  
  def getMatrix(self):
    return self.matrix