b=[(8,5,13,23,29,15,23,30),(17,22,30,3,13,25,2,14),(10,15,18,28,2,18,27,6),(0,31,1,11,22,7,16,20),(12,17,24,26,3,24,25,5),(27,31,8,11,19,4,12,21),(21,20,28,4,9,26,7,14),(1,6,9,19,29,10,16,0)]
def get_square_nums(n,square_moves=0,nonsquare_moves=0):
    squares={"64":0,"49":0,"36":0,"25":0,"16":0,"9":0,"4":0,"1":0}
    for key in squares:
        squares[key]=int(key)-(n-2*square_moves-10*nonsquare_moves)
    return squares
def get_legal_moves(chess_board,x_coordinate,y_coordinate):
    legal_moves = []
    for i in range (0,7):
        legal_moves.append((i,y_coordinate,chess_board[y_coordinate][i]))
        legal_moves.append((x_coordinate,i,chess_board[i][x_coordinate]))
        if x_coordinate+i>=0 and x_coordinate+i<=7 and y_coordinate+i>=0 and y_coordinate+i<=7:
            legal_moves.append((x_coordinate+i,y_coordinate+i,chess_board[y_coordinate+i][x_coordinate+i]))
        elif x_coordinate-i>=0 and x_coordinate-i<=7 and y_coordinate-i>=0 and y_coordinate-i<=7:
            legal_moves.append((x_coordinate-i,y_coordinate-i,chess_board[y_coordinate-i][x_coordinate-i]))
        elif x_coordinate+i>=0 and x_coordinate+i<=7 and y_coordinate-i>=0 and y_coordinate-i<=7:
            legal_moves.append((x_coordinate+i,y_coordinate-i,chess_board[y_coordinate-i][x_coordinate+i]))
        elif x_coordinate-i>=0 and x_coordinate-i<=7 and y_coordinate+i>=0 and y_coordinat+i<=7:
            legal_moves.append((x_coordinate-i,y_coordinate+i,chess_board[y_coordinate+i][x_coordinate-i]))
    return legal_moves
def make_move(chess_board,x_coordinate,y_coordinate):
    squares=get_square_nums(chess_board[y_coordinate][x_coordinate])
    legal_moves=get_legal_moves(chess_board,x_coordinate,y_coordinate)
    squares
    legal_moves
    print(squares)
    print(legal_moves)
    score=0
    for i in legal_moves:
        if legal_moves[i,2] in squares:
            print(i)
    return score
