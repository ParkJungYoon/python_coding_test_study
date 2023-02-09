import math

n = int(input())
zero_count = 0
stack = []

for i in str((math.factorial(n))):
    stack.append(i)

for _ in range(len(stack)):
    if stack.pop() != "0":
        print(zero_count)
        break
    zero_count += 1
