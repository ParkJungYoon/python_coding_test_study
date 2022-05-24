from collections import deque
a, b = map(int,input().split())
queue = deque()
queue.append((a,1))

while queue:
    now, cnt = queue.popleft()
    if now == b:
        print(cnt)
        break
    if now*2 <= b or int(str(now)+'1') <= b:
        queue.append((now*2,cnt+1))
        queue.append((now*10+1,cnt+1))
else:
    print(-1)

# from collections import deque
# import math 
# a, b = map(int,input().split())
# count = 0
# queue = deque([a])

# while 1:
#     now = queue.popleft()
#     if now == b:
#         break
#     queue.append(now*2)
#     queue.append(int(str(now)+'1'))
#     count += 1
#     test = [i for i in queue if i < b]
#     if len(test) == 0:
#         count = -1
#         break
# if count == -1:
#     print(-1)
# else:
#     result = math.trunc(math.sqrt(count))
#     print(result+1)