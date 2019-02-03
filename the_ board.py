place = ["topl", "topm", "topr",
         "midl", "midm", "midr",
         "lowl", "lowm", "lowr"]

the_board = {"topl": ' ', "topm": ' ', "topr": ' ',
             "midl": ' ', "midm": ' ', "midr": ' ',
             "lowl": ' ', "lowm": ' ', "lowr": ' '}

def print_board(board):
    print(board["topl"] + '|' + board["topm"] + '|' + board["topr"])
    print("-+-+-")
    print(board["midl"] + '|' + board["midm"] + '|' + board["midr"])
    print("-+-+-")
    print(board["lowl"] + '|' + board["lowm"] + '|' + board["lowr"])

turn = 'X'
for i in range(9):
    print_board(the_board)
    print(turn + "の番です．どこに打つ？")
    while True:
        move = input()
        if move not in place:
            pass
        else:
            break
    the_board[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'

print_board(the_board)
