from collections import deque
test_num = int(input())

for i in range(test_num):
    n, m = map(int,input().split())
    rate = deque(map(int,input().split()))
    rate2 = deque((rate[i],i) for i in range(n))
    rate = sorted(list(rate),reverse=True)
    count = 0
    while rate2:
        cur = rate2[0][0]
        if cur == rate[0]:
            count += 1
            if rate2[0][1] == m:
                break
            else:
                rate2.popleft()
                rate = rate[1:]
        else:
            rate2.append(rate2.popleft())
    print(count)