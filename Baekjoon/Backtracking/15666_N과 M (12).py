n, m = map(int, input().split())
nums = list(set(map(int, input().split())))

nums.sort()
nums_temp  = []

def backtracking(current):
    if len(nums_temp) == m:
        print(*nums_temp)
        return
    
    for i in range(current, len(nums)):
        nums_temp.append(nums[i])
        backtracking(i)
        nums_temp.pop()

backtracking(0)