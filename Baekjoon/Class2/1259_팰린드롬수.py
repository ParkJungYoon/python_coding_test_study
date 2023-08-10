import sys

def check(num):
    if len(num) == 1:
        return True
    for i in range(len(num)//2):
        if num[i] != num[-(i+1)]:
            return False
    return True

# 그냥 뒤집는거 보다 빠름
while True:
    num = sys.stdin.readline().strip()
    # reverse_num = num[::-1]

    if int(num) == 0:
        break

    if check(num):
        print('yes')
    else:
        print('no')