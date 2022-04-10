n, m = map(int,input().split())
p = [int(input()) for i in range(m)]
p.sort(reverse=True)
list = []
price = []

for i in range(len(p)):
    n -= 1
    list.append((i+1)*p[i])
    price.append(p[i])
    if n == 0:
        break

print(price[list.index(max(list))],max(list))