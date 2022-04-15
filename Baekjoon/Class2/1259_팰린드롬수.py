import sys

while True:
    num = sys.stdin.readline().strip()
    reverse_num = num[::-1]

    if int(num) == 0:
        break

    if num == reverse_num:
        print('yes')
    else:
        print('no')