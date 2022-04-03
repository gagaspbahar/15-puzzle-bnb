from puzzle import *

if __name__ == '__main__':
    print('''
  __   _____     _____                        _        
 /_ | | ____|   |  __ \                      | |       
  | | | |__     | |__) |  _   _   ____  ____ | |   ___ 
  | | |___ \    |  ___/  | | | | |_  / |_  / | |  / _ \\
  | |  ___) |   | |      | |_| |  / /   / /  | | |  __/
  |_| |____/    |_|       \__,_| /___| /___| |_|  \___|
                                                       
                                                       ''')
    print("Choose your input option: ")
    print("1. File input")
    print("2. Console input")
    option = int(input())
    if(option == 1):
        filename = input("Enter your desired filename: ")
        startingMatrix = fileInput(filename)
    elif(option == 2):
        print("Enter your 4x4 matrix (valid values only 0 to 15): ")
        startingMatrix = consoleInput()
    else:
        print("Invalid input.")
        quit()
    print("INITIAL MATRIX: ")
    printMatrix(startingMatrix)
    print("=================")
    solve(startingMatrix)
    