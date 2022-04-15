import sys
input = sys.stdin.readline

k, n = map(int,input().split())
data = [int(input()) for _ in range(k)]

def binary_search(data,start,end):
    mid = (start+end)//2
    count = 0
    if start > end:
        return end
    for i in data:
        count += i // mid
    if count >= n:
        return binary_search(data,mid+1,end)
    else:
        return binary_search(data,start,mid-1)

start = 1
end = max(data)
print(binary_search(data,start,end))

# 재성 풀이

# import sys

# n, k = map(int, input().split())
# lan = []
# for i in range(n):
#     lan.append(int(sys.stdin.readline().strip()))
# length = max(lan)
# def binary_search(array, start, end, k):
#     count = 0
#     if start > end:
#         return end
#     mid = (start + end) // 2
#     for i in array:
#         count += i // mid

#     if count == k:
#         return binary_search(array, mid+1, end, k)
#     elif count > k:
#         return binary_search(array, mid+1, end, k)
#     else:
#         return binary_search(array, start, mid -1, k)


# print(binary_search(lan, 1, length, k))