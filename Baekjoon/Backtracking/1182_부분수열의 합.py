import sys
input = sys.stdin.readline

n, s = map(int, input().split())
nums = list(map(int, input().split()))
count = 0
current = 0

def dfs(start):
    global count, current
    
    if start != 0:
        if current == s:
            count += 1
    
    for num in range(start, n):
        current += nums[num]
        dfs(num+1)
        current -= nums[num]

dfs(0)
print(count)

'''
nums.sort()

start, end = 0, n-1
current = sum(nums)
count = 0

while True:
    if start > end:
        break
  

print(count)
'''