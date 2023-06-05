import sys
input = sys.stdin.readline

'''
r번 회전 -> r번 이동
현재 자기 위치를 기준으로 몇바퀴 돌고 몇 칸 앞으로 더 가야하는지 계산
껍질 개수는 min(N, M) // 2
'''

n, m, r = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
new_graph = [[0] * m for _ in range(n)]

'''
단위를 한 칸 이동하는 회전 함수
ms, me : 한 행에서 시작점과 끝점
ns, ne : 한 열에서 시작점과 끝점
'''

def rotation(ms, me, ns, ne):
    t1, t2, t3, t4 = graph[ns][ms], graph[ns][me], graph[ne][ms], graph[ne][me]
    # 위, 아래
    for top in range(ms+1, me):
        graph[ns][top-1] = graph[ns][top]
    for down in range(me-1, ms, -1):
        graph[ne][down+1] = graph[ne][down]
    # 왼, 오
    for left in range(ne-1, ns, -1):
        graph[left+1][ms] = graph[left][ms]
    for right in range(ns+1, ne):
        graph[right-1][me] = graph[right][me]

    graph[ns+1][ms] = t1
    graph[ns][me-1] = t2
    graph[ne][ms+1] = t3
    graph[ne-1][me] = t4

total = n * 2 + m * 2 - 4
ms, me, ns, ne = 0, m-1, 0, n-1
for i in range(min(n,m)//2):
    # jump만큼 앞으로 가야함
    jump = r % total

    for _ in range(jump):
        rotation(ms, me, ns, ne)
    
    ms, me, ns, ne = ms+1, me-1, ns+1, ne-1

    # 다음 껍질의 수의 개수는 -8
    total -= 8

for g in graph:
    print(' '.join(map(str, g)))

''''
[ 각 껍질마다 숫자가 몇 개 있는지 이렇게 구했다가 장렬하게 전사함. ]
temp_width = m
temp_height = n
ms, me, ns, ne = 0, m-1, 0, n-1
for i in range(min(n,m)//2):
    # jump만큼 앞으로 가야함
    total = temp_width * 2 + temp_height * 2 - 4
    jump = r % total

    for _ in range(jump):
        rotation(ms, me, ns, ne)
    
    ms, me, ns, ne = ms+1, me-1, ns+1, ne-1

    # 다음 껍질의 길이는 반으로 준다.
    temp_width = temp_width // 2
    temp_height = temp_height // 2
'''
'''
https://velog.io/@hyebinnn/%EB%B0%B1%EC%A4%80-%EB%B0%B0%EC%97%B4-%EB%8F%8C%EB%A6%AC%EA%B8%B02-16927%EB%B2%88
다른 사람 코드 보면서 리팩토링 해보기
'''