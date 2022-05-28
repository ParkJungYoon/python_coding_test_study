import sys
input = sys.stdin.readline
n = int(input())
stack = []
for i in range(n):
    instruction = input().split()
    if instruction[0] == 'push':
        stack.append(instruction[1])
    elif instruction[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif instruction[0] == 'size':
        print(len(stack))
    elif instruction[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif instruction[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])