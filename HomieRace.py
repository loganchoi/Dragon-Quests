def printFunc(race):
        for x in range(0,len(race)):
                for y in range(0,len(race[x])):
                        print(race[x][y],end="")
                print()

def checkMove(race,row,col,death):
        if row == 1 or row == 7:
                return True
        if race[row][col] == "X":
                return True
        return False

if __name__ == "__main__":
        race = ["                                            ",
                "============================================",
                "       X            X            X    |     ",
                "               X                      |     ",
                ">         X                   X       |     ",
                "    X                X                |     ",
                "       X                  X           |     ",
                "============================================",
                "                                            "]
        for x in range (0, len(race)):
                race[x] = list(race[x])
        death = False
        row = 4
        col = 0
        while col != 39 and death == False:
                printFunc(race)
                move = input()
                if move == "w":
                        race[row][col] = " "
                        row = row-1
                elif move == "s":
                        race[row][col] = " "
                        row = row + 1
                else:
                        race[row][col] = " "
                col = col + 1
                death = checkMove(race,row,col,death)
                race[row][col] = ">"
        
        if col >= 39:
                print("CONGRATS")
        if death == True:
                print("YOU DEAD BITCH")
        
