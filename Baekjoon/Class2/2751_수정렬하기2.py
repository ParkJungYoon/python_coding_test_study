import sys
import heapq
input = sys.stdin.readline
n = int(input())
# 1차 시도 (안될줄 알았다~)
# nums = [int(input()) for _ in range(n)]
# nums.sort()
# for i in nums:
#     print(i)
# 2차 시도 : 힙 (성공)
nums = []
for i in range(n):
    heapq.heappush(nums,int(input()))
for i in range(n):
    print(heapq.heappop(nums))
# 3차 시도
# def quick_sort(array):
#     if len(array) <= 1: return array
#     pivot, tail = array[0], array[1:]

#     left = [i for i in tail if i<=pivot]
#     right = [i for i in tail if i>pivot]
#     return quick_sort(left) + [pivot] + quick_sort(right)

# print(*quick_sort(nums),sep='\n')