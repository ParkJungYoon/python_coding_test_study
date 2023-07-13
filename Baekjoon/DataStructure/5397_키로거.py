import sys
from collections import deque
input = sys.stdin.readline

# 데크 사용
def find_password(input_password):
    left = deque([])
    right = deque([])
    
    for word in input_password:
        if word == "<":
            if left:
                temp = left.pop()
                right.appendleft(temp)
        elif word == ">":
            if right:
                temp = right.popleft()
                left.append(temp)
        elif word == "-":
            if left:
                left.pop()
        else:
            left.append(word)

    answer = []
    for l in list(left):
        answer.append(l)
    for r in list(right):
        answer.append(r)
    return ''.join(answer)

# 스택 사용
def find_password2(input_password):
    left = []
    right = []
    
    for word in input_password:
        if word == "<":
            if left:
                temp = left.pop()
                right.append(temp)
        elif word == ">":
            if right:
                temp = right.pop()
                left.append(temp)
        elif word == "-":
            if left:
                left.pop()
        else:
            left.append(word)

    right.reverse()
    answer = left + right
    return ''.join(answer)


t = int(input())
for _ in range(t):
    # print(find_password(input().rstrip()))
    print(find_password2(input().rstrip()))