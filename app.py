from puzzle import *

if __name__ == '__main__':
    filename = input("Enter your desired filename: ")
    startingMatrix = fileInput(filename)
    # p = PuzzleNode(0,0,startingMatrix)
    # p.calcCost()
    # p.printMatrix()
    solve(startingMatrix)
    