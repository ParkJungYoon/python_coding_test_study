from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
queue = deque()
for _ in range(n):
    instruction = input().split()
    if instruction[0] == 'push':
        queue.append(int(instruction[1]))
    elif instruction[0] == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
    elif instruction[0] == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])    
    elif instruction[0] == 'size':
        print(len(queue))
    elif instruction[0] == 'empty':
        if len(queue) == 0: print(1)
        else: print(0)
    elif instruction[0] == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])