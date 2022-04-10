n, m = map(int,input().split())
if n == 0:
    print(0)
else:
    book = map(int,input().split())
    box = 0
    count = 1
    for i in book:
        box += i
        if box > m:
            count += 1
            box = i
    print(count)