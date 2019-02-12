#coding=utf-8
def mainprogramm(board):
  print('A Tic Tac Toe Game')
  print('')
  print3x3(board)
  print('')
  while not(Blank(board)):
    if not(winningcondition(board,'O')):
      if not(Blank(board)):
        PlayerMove()
        print3x3(board)
        print('')
      else:
         print('Tie Game!')
    else:
      print('Computer won this time')
      break
    if not(winningcondition(board,'X')):
      if not(Blank(board)):
        move = ComputerMove(board)
        InsertChoice('O', move, board)
        k = "Computer placed an 'O' in position " + str(move)
        print (k)
        print3x3(board)
        print('')
      else:
        print('Tie Game!')
    else:
      print3x3(board)
      print('')
      print('Congratulation!!!!You won this time')
      break
def print3x3(board):
  l1 = "     " + " " + " " + board[0]+ " " + " " + " " + "|" + " " + " " + " " + " " + " " + board[1] + " " + " " + " " + "|" + " " + " " + " " + board[2]
  l2 = "     " + " " + " " + board[3]+ " " + " " + " " + "|" + " " + " " + " " + " " + " " + board[4] + " " + " " + " " + "|" + " " + " " + " " + board[5]
  l3 = "     " + " " + " " + board[6]+ " " + " " + " " + "|" + " " + " " + " " + " " + " " + board[7] + " " + " " + " " + "|" + " " + " " + " " + board[8]
  print(l1)
  print("    -------+---------+-------")
  print(l2)
  print("    -------+---------+-------")
  print(l3)
def Blank(board):
  if board.count([" "]) > 1:
    return True
  else:
    return False
def winningcondition(board, player):
  return (board[0] == board[1] == board[2] == player) or (board[3] == board[4] == board[5] == player) or (board[6] == board[7] == board[8] == player) or (board[0] == board[3] == board[6] == player) or (board[1] == board[4] == board[7] == player) or (board[2] == board[5] == board[8] == player) or (board[0] == board[4] == board[8] == player) or (board[2] == board[4] == board[6] == player)
def PlayerMove():
  run = True
  while run:
     move = input('Please select a position to place X (0-8):')
     print('')
     try: 
      move = int(move)
      if move >= 0 and move < 9:
        if isspacefree(move):
          run = False
          InsertChoice('X', move, board)
        else:
          print('Sorry, this space is occupied!')
      else:
        print('Please type a number within the range!')
     except  ValueError:
      print('Please type a number!')
def InsertChoice(Choice, pos, board):
  board[pos] = Choice
def isspacefree(pos):
  return board[pos] == ' '
def avaliable(board):
  positions = [s for s in range(9) if board[s] == " "]
  return positions
def random(board):
  import random
  if avaliable(board):
    return random.choice(avaliable(board))
def ComputerMove(board):
  position = random(board)
  return position
board = 9 * [" "]
while True:
  mainprogramm(board)
  input('Press any key to restart!!!')
  board = 9 * [" "]

  


