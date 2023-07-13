n, m = map(int, input().split())
nums = list(set(map(int, input().split())))

nums.sort()
# 배열은 글로벌 선언 안해도 됨, 변수는 해야함.
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