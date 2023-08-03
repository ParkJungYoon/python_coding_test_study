import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
sensor = list(map(int, input().split()))
sensor.sort()

difference = []
for i in range(n-1):
    difference.append(sensor[i+1]-sensor[i])
difference.sort(reverse=True)

print(sum(difference[k-1:]))

'''
비슷한 유형
[13164] 행복 유치원 https://www.acmicpc.net/problem/13164

https://journeytosth.tistory.com/16

각 센서의 숫자는 좌표이기 때문에 좌표 순으로 먼저 정렬.
그리고 센서 간의 거리를 확인해서 가장 거리가 먼 센서 간의 집중국 다른거 쓰도록 함.

1--4--7
이렇게 한 집중국으로 수신하기로 했으면, 집중국이 어떤 위치에 있어도 거리합 구할 거니깐 어디에 있든 각각의 센서간의 간격만큼

'''