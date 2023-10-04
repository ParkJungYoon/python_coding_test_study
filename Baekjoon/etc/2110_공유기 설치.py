import sys
input = sys.stdin.readline

n, c = map(int, input().split())
home = [int(input()) for _ in range(n)]
home.sort()

'''
[문제 해결 알고리즘]
1. array라는 리스트에 집들의 좌표를 입력받은 후에 정렬
2. start: 최소 거리, end: 최대 거리
3. 앞 집부터 공유기 설치
4. 설치 공유기 개수가 c개를 넘어가면 더 넓게 설치할 수 있다는 이야기
이기 때문에 설치거리를 mid+1로 설정하여 다시 앞집부터 설치
5. c개가 넘지 않는다면 더 좁게 설치해야 한다는 이야기 이므로 mid-1로 설정
'''

'''
공유기를 설치할 거리를 이분 탐색으로 결정
'''

start = 1
end = home[-1] - home[0]

while start <= end:
    mid = (start + end) // 2
    count = 1
    current = home[0]

    for i in range(1, n):
        if home[i] >= current + mid:
            count += 1
            current = home[i]

    if count >= c:
        start = mid + 1
        answer = mid
    else:
        end = mid - 1

print(answer)