# 정렬할 때 나이는 현재 str이라서 int로 변환한 값을 기준으로 정렬해야한다.
import sys
input = sys.stdin.readline
n = int(input())
member = []
for i in range(n):  
    member.append(list(input().split()))
    member[i].append(i)
member.sort(key=lambda x: (int(x[0]),x[2]))
for i in member:
    print(i[0], i[1])