import sys
input = sys.stdin.readline
n = int(input())
time = []
for i in range(n):
    start, end = map(int,input().split())
    time.append((start, end))
time_sort = sorted(time, key=lambda x:(x[1],x[0]))
# print(time_sort)

end_time = time_sort[0][1]
count = 1
for i in range(1, n):
  if end_time <= time_sort[i][0]:
    count+=1
    end_time = time_sort[i][1]
print(count)