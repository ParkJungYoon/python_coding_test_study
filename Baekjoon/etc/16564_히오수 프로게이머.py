import sys
input = sys.stdin.readline

n, k = map(int, input().split())
levels = [int(input()) for _ in range(n)]

start = min(levels)
end = start + k

'''
k: 레벨 올릴 수 있는 총합
start: 올릴 수 있는 레벨 k 중에 0 올리는 시점이 시작
start를 올릴 수 있는 레벨이 k개면 k개 안으로 올리면 된다.
그래서 0개 올리는 start(가장 작은 값 부터), end(최대로 올린) 사이에서 최소 값을 몇으로 할 지 mid를
조절하면서 이분탐색!
'''

max_answer = 0
while start <= end:
    # 최소를 최대 몇까지 올릴 지 mid로 정함
    mid = (start + end) // 2

    # temp는 얼마나 레벨 업을 시켜야하는지 총합
    temp = 0
    for level in levels:
        # mid가 최소가 될 값이니깐 그 값보다 작은 값은 다 올려줘야함.
        if mid > level:
            temp += (mid - level)

    # K개 만큼만 레벨 상승이 가능하기 때문에 if문
    if temp <= k:
        # 이 안에 있으면 start를 높여보기
        start = mid + 1
        max_answer = max(mid, max_answer)
    else:
        # 범위 안에 안들면 end 값을 줄여야함
        end = mid - 1

print(max_answer)