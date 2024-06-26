'''
* 병든 나이트가 여행하면서 방문한 칸의 수를 최대로
1) 세로 N = 1 -> 없음
2) 세로 N = 2 -> 가로 M이 3이상일 때랑 일단 최대는 3칸 이동임
3) 세로 N = 3 
'''
n, m = map(int, input().split())

count = 0

if n == 1:
    count = 1
elif n == 2:
    if m <= 6:
        count = (m+1) // 2
    else:
        count = 4
# 이제 모든 방법으로 이동이 가능하고, (모든 조합 다 하면 가로는 6일 때)
# 가로가 7일 때부터는 오른쪽으로 한칸씩 가야지 최대 칸 방문함.
elif n >= 3:
    if m <= 6:
        count = min(m, 4)
    else:
        count = m - 2

'''
m = 1일 때 1
m = 2일 때 2
m = 3일 때 3
m = 4일 때 4
m = 5일 때 4
m = 6일 때 4
m = 7일 때 5
m = 8일 때 5 + 1 = 6
'''


print(count)