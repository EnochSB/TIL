# 세로 읽기
board = [['']*15 for _ in range(5)]

for i in range(5):
    string = input()
    for j in range(len(string)):
        board[i][j] = string[j]
        
for j in range(15):
    for i in range(5):
        print(board[i][j], end='')