import sys
input = sys.stdin.readline

def solution():
    n, q = map(int,input().split())
    nums = sorted(list(map(int,input().split())))
    
    sum_value = 0
    prefix_sum = [0]
    for i in nums:
        sum_value += i
        prefix_sum.append(sum_value)

    for i in range(q):
        l, r = map(int,input().split())
        print(prefix_sum[r] - prefix_sum[l-1])

if __name__ == '__main__':
    solution()