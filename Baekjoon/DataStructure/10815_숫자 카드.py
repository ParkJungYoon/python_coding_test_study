n = int(input())
card = list(map(int, input().split()))
m = int(input())
problem = list(map(int, input().split()))

card.sort()

def binary_search(start, end, check):
    if start > end:
        return 0
    mid = (start+end) // 2

    if card[mid] == check:
        return 1
    elif card[mid] > check:
        return binary_search(start, mid-1, check)
    else:
        return binary_search(mid+1, end, check)

result = []
for p in problem:
    result.append(binary_search(0, n-1, p))

print(*result)