import puzzle

if __name__ == '__main__':
    p = puzzle.Puzzle()
    filename = input("Enter your desired filename: ")
    p.fileInput(filename)
    print(p.getMatrix())