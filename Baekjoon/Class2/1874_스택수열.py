import sys
input = sys.stdin.readline
n = int(input())
input_num = [int(input()) for _ in range(n)]
stack = [i+1 for i in range(input_num[0])]
result = ['+' for i in range(input_num[0])]

num = input_num[0]+1
for i in input_num:
    if len(stack) == 0:
        stack.append(num)
        result.append('+')
        num += 1
    if stack[-1] == i:
        stack.pop()
        result.append('-')
    elif i > stack[-1]:
        while i != stack[-1]:
            stack.append(num)
            result.append('+')
            num += 1
        stack.pop()
        result.append('-')
    else:
        result.append('NO')

if 'NO' in result:
    print("NO")
else:
    print(*result,sep='\n')
