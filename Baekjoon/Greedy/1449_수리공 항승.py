# 처음 0.5는 여유분으로 남기고 나머지 테이프 만큼 오른쪽으로 붙인다.
# 그러면 그 길이 범위 안에 있는 파이프는 수리완! 이니깐 continue

n, l = map(int, input().split())
leak = list(map(int, input().split()))

leak.sort()
count = 0
end = 0
l -= 0.5

for i in range(n):
    if leak[i] <= end:
        continue
    count += 1
    end = leak[i] + l

print(count)