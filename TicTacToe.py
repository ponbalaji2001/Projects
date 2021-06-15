# Tic-Tac-Toe game by python3
# Computer vs user

board={ "1":"1","2":"2","3":"3","4":"4","5":"X","6":"6","7":"7","8":"8","9":"9" }

def display_board(board):

    print("+","+","+","+",sep="-------")
    print("|","|","|","|",sep="       ")
    print("|",board["1"],"|",board["2"],"|",board["3"],"|",sep="   ")
    print("|","|","|","|",sep="       ")
    print("+","+","+","+",sep="-------")
    print("|","|","|","|",sep="       ")
    print("|",board["4"],"|",board["5"],"|",board["6"],"|",sep="   ")
    print("|","|","|","|",sep="       ")
    print("+","+","+","+",sep="-------")
    print("|","|","|","|",sep="       ")
    print("|",board["7"],"|",board["8"],"|",board["9"],"|",sep="   ")
    print("|","|","|","|",sep="       ")
    print("+","+","+","+",sep="-------")

(display_board(board))

def victory_X(board):

    if board["1"] == board["2"] == board["3"] == "X" or board["4"] == board["5"] == board["6"] == "X" or \
       board["7"] == board["8"] == board["9"] == "X" or board["1"] == board["4"] == board["7"] == "X" or \
       board["2"] == board["5"] == board["8"] == "X" or board["3"] == board["6"] == board["9"] == "X":
            return True

def victory_O(board):

    if board["1"] == board["2"] == board["3"] == "O" or board["4"] == board["5"] == board["6"] == "O" or \
       board["7"] == board["8"] == board["9"] == "O" or board["1"] == board["4"] == board["7"] == "O" or \
       board["2"] == board["5"] == board["8"] == "O" or board["3"] == board["6"] == board["9"] == "O":
             return True

def enter_move(board):

        for i in range(5):
                if i==4:
                  print("MATCH DRAW")
                  break

                move = input("Enter your move :")

                if board[move] !="X" and board[move]!="O":
                    board[move] = "O"

                    if victory_O(board):
                      display_board(board)
                      print("0 WON")
                      break

                    for i in (board.keys()):

                       if board[i]!="X" and board[i]!="O":
                          board[i] = "X"
                          break

                    if victory_X(board):
                        display_board(board)
                        print("X WON")
                        break

                    display_board(board)

                else:
                    print("That place is already filled")
                    continue

enter_move(board)








