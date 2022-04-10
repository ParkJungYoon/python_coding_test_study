## BOJ, 그리디

#### 2022.04.05 ~ 22.04.

#### (1343번) 폴리오미노

```python
input_board = input().split('.')
board = []
for i in input_board:
    board.append(i)
    if len(i) > 0:
        board.append('')
board = board[:-1]
result = ''

for i in board:
    if len(i)//4 != 0:
        result += ('AAAA' * (len(i)//4))
        if (len(i)%4)%2 == 0:
            result += ('BB' * ((len(i)%4)//2))
        else:
            result = -1
            break
    elif len(i) == 2:
        result += 'BB'
    elif len(i) == 0:
        result += '.'
    else:
        result = -1
        break

print(result)
```

#### (1417번) 국회의원 선거 (미해결)

```py
n = int(input())
candidate = []
for i in range(n):
    candidate.append(int(input()))
```

#### (1439번) 뒤집기

```py
s = input()

only_one = s.split('0')
only_zero = s.split('1')

count_one = len([i for i in only_one if len(i) != 0])
count_zero = len([i for i in only_zero if len(i) != 0])

print(min(count_one,count_zero))
```

#### (1789번) 수들의 합

```py
s = int(input())
num = 1
count = 0

while s != 0:
    s -= num
    num += 1
    count += 1
    if s < 0:
        count -= 1
        s = 0

print(count)
```

#### (1817번) 짐 챙기는 숌

```python
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
```

#### (2828번) 사과 담기 게임

```python
n, m = map(int,input().split())
j = int(input())
move = 0
now = [i for i in range(1,m+1)]
for _ in range(j):
    apple = int(input())
    if apple not in now:
        if apple < now[0]:
            distance = apple - now[0]
            move += abs(distance)
            now = list(map(lambda x:x+distance,now))
        else:
            distance = apple - now[-1]
            move += distance
            now = list(map(lambda x:x+distance,now))

print(move)
```

#### (1026번) 보물

```py
n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
s = 0

for i in range(n):
    min_num = min(a)
    max_num = max(b)
    s += (min_num * max_num)
    a.remove(min_num)
    b.remove(max_num)

print(s)
```

#### (1049번) 기타줄

```py
n, m = map(int,input().split())
p_list = []
pp_list = []
result = []
for i in range(m):
    p, pp = map(int,input().split())
    p_list.append(p)
    pp_list.append(pp)

if n%6 == 0:
    result.append(min(p_list)*(n//6))
    result.append(min(pp_list)*n)
else:
    result.append(min(p_list)*(n//6)+min(pp_list)*(n%6))
    result.append(min(pp_list)*n)
    result.append(min(p_list)*(n//6+1))

print(min(result))
```

#### (1213번) 팰린드롬 만들기

```py
name = input()

if name%2 == 0:
```

#### (1246번) 온라인 판매

```py
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
```

#### (1448번) 삼각형 만들기

```py
n = int(input())
leng = [int(input()) for _ in range(n)]
leng.sort(reverse=True)
c = leng[0]

for i in range(1,len(leng)):
    a = leng[i]
    for j in range(i+1,len(leng)):
        b = leng[j]
        if a+b > c:
            result = a+b+c
            break
        else:
            result = -1

print(result)
```

#### (1449번) 수리공 항승

```py
n, l = map(int,input().split())
place = list(map(int,input().split()))
```
