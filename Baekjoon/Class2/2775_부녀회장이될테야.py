t = int(input())

for i in range(t):
    k = int(input())
    n = int(input())
    count = [i for i in range(1,n+1)]
    for _ in range(k):
        for m in range(1,n):
            count[m] += count[m-1]
    print(count[n-1])