import puzzle

if __name__ == '__main__':
    filename = input("Enter your desired filename: ")
    p = puzzle.Puzzle(0, 0, [])
    p.fileInput(filename)
    p.printMatrix()
    reach = puzzle.isReachable(p.matrix)

    if(not reach):
        print("The puzzle is not solvable.")
    