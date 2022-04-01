import puzzle

if __name__ == '__main__':
    filename = input("Enter your desired filename: ")
    p = puzzle.Puzzle(0, 0, [])
    p.fileInput(filename)
    p.printMatrix()
    print(puzzle.isReachable(p.matrix))