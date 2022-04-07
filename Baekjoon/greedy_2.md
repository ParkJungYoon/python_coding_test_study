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
