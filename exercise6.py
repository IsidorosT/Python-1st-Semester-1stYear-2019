def mainprogramm():
    print('!!!!!!! Execute the programm on fullscreen for avoiding ovelaying cells !!!!!!!')
    print('The range of the inputs is used for the best experience in fullscreen')
    length = 0
    width = 0
    MineNum = 0
    board = []
    User_data = UserConstructionInput()
    length = User_data[0]
    width = User_data[1]
    MineNum = User_data[2]
    board = MakeCells(length, width, MineNum, board)
    Construction(length, width, board)
def UserConstructionInput():
    run3 = True
    print('Mines will appear as +')
    while run3:
        run1 = True
        while run1:
            global width
            width = input('Give the width of the Minesweeper(1-23):')
            try:
                width = int(width)
                run1 = False
                if width < 1 and width > 23:
                    run1 = True
                    print('width is out of range')
            except ValueError:
                print('Please insert a number!')
                run1 =  True
        run2 = True
        while run2:
            length = input('Give the length of the Minesweeper:')
            try:
                length = int(length)
                run2 = False
                if width == length:
                    print('Minesweeper board should not be square!!')
                    run2 = True 
            except ValueError:
                print('Please insert a number!')
                run2 = True
        MineNum = input('Give the amount of bombs that you want the Minesweeper to has:')
        try:
            MineNum = int(MineNum)
            run3 = False
        except ValueError:
            print('Please insert a number!')
            run3 = True
        if width * length <= MineNum:
            print('The amount of bombs you enter is equal or greater than the avaliable shells')
            run3 = True
    return (length, width, MineNum)
def MakeCells(length, width, MineNum, board):
    import random
    Block = length * width
    board = (Block - MineNum) * [" "] + MineNum * ["+"]
    random.shuffle(board)
    return board
def Construction(length, width, board):
    for j in range(length):
        row1 = ' -------' + (width - 1) * ' --------'
        row2 = '|       |' + (width - 1) * '        |'
        if j == 0: 
            print(row1)
            print(row2)
            for i in range(width):     
                if i == 0:
                    row3 = '|   ' + board[i] + '   |'
                    print(row3,end = " ")
                else:
                    row3 = '  ' + board[i] + '    |'
                    if i < width - 1:
                        print(row3,end = " ")
                    else:
                        print(row3)
            n = 1
            print(row2)
            print(row1)
        else:
                print(row2)
                for i in range(width):     
                    if i == 0:
                        row3 = '|   ' + board[i + width * n] + '   |'
                        print(row3,end = " ")
                    else:
                        row3 = '  ' + board[i + width * n] + '    |'
                        if i < width - 1:
                            print(row3,end = " ")
                        else:
                            print(row3)
                n += 1
                print(row2)
                print(row1)
while True:
  mainprogramm()
  input('Press any key to restart!!!')

        