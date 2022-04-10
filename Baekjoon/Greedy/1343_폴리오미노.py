input_board = input().split('.')
board = []
for i in input_board:
    board.append(i)
    if len(i) > 0:
        board.append('')
board = board[:-1]
result = ''

for i in board:
    if len(i)//4 != 0:
        result += ('AAAA' * (len(i)//4))
        if (len(i)%4)%2 == 0:
            result += ('BB' * ((len(i)%4)//2))
        else:
            result = -1
            break
    elif len(i) == 2:
        result += 'BB'
    elif len(i) == 0:
        result += '.'
    else:
        result = -1
        break

print(result)