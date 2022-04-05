## BOJ, 그리디

#### 2022.04.01 ~ 22.04.04

#### (10162번) 전자레인지

```python
T = int(input())

times = [300,60,10]
answer = []

for time in times:
    answer.append(T//time)
    T = T % time

if T != 0:
    print(-1)
else:
    for i in answer:
        print(i, end=' ')
```

불필요한 반복 제거

```python
t = int(input())

a = t // 300
t = t % 300

b = t // 60
t = t % 60

c = t // 10
t = t % 10

if t != 0:
    print(-1)
else:
    print(a, b, c)
```

#### (2720번) 세탁소 사장 동혁

```python
t = int(input())
coin = [25, 10, 5, 1]

for i in range(t):
    money = int(input())
    a = money // 25
    money = money % 25
    b = money // 10
    money = money % 10
    c = money // 5
    money = money % 5
    d = money // 1
    money = money % 1

    print(a,b,c,d)
```

#### (11034번) 캥거루 세마리2

```python
while True:
    try:
        count = 0
        a, b, c = map(int,input().split())
        while (c-b) != 1 or (b-a) != 1:
            if (b-a) < (c-b):
                count += 1
                a = b
                b = b+1
            else:
                count += 1
                c = b
                b = b-1
        print(count)
    except:
        break
```

#### (14720번) 우유 축제

```python
n = int(input())
store = list(map(int, input().split()))
count = 0

store = store[store.index(0):]

now = 0
for i in store:
    if now == i:
        count += 1
        now += 1
        if now == 3:
            now = 0
print(count)
```

이런 생각은 어떻게 하는걸까

```python
n = int(input())
milk = list(map(int,input().split()))

count = 0

for i in range(n):
    if milk[i] == count % 3:
        count += 1

print(count)
```

#### (22864번) 피로도

```python
a, b, c, m = map(int,input().split())

tired = 0
work = 0

for i in range(24):
    if (tired + a) > m:
        tired -= c
        if tired < 0:
            tired = 0
    elif a > m:
            tired = 0
    else:
        tired += a
        work += b
print(work)
```

#### (2864번) 5와 6의 차이

```python
a, b = input().split()

max = sum([int(a.replace('5','6')), int(b.replace('5','6'))])
min = sum([int(a.replace('6','5')), int(b.replace('6','5'))])

print(min, end=' ')
print(max)
```

#### (2930번) 가위 바위 보 (미해결)

```python
r = int(input())
dog = input()
n = int(input())

score = 0
for i in range(n):
    friend = input()
    for i in range(r):
        if dog[i] == friend[i]:
            score += 1
        elif (dog[i]=='S' and friend[i]=='P') or (dog[i]=='P' and friend[i]=='R') or (dog[i]=='R' and friend[i]=='S'):
            score += 2

print(score)
print(r*n*2)
```

#### (5585번) 거스름돈

```python
price = int(input())
money = [500,100,50,10,5,1]
change = 1000 - price
count = 0

for i in money:
    if change != 0:
        count += change // i
        change = change % i

print(count)
```

#### (14471번) 포인트 카드

```python
n, m = map(int,input().split())

# 일단 비용 다 넣고
cost = []

for i in range(m):
    a, b = map(int,input().split())

    # 성공 도장 이미 n개 이상이면 비용 0
    if a >= n:
        cost.append(0)
    else:
        cost.append(b - n)

cost.remove(max(cost))
print(sum(cost))
```

#### (14487번) 욱제는 효도쟁이야!!

```python
village = int(input())
cost = list(map(int,input().split()))

cost.remove(max(cost))

print(sum(cost))
```

#### (14659번) 한조서열정리하고옴ㅋㅋ

```python
n = int(input())
height = list(map(int,input().split()))
count = 0
winner_count = 0

for i in range(n):
    for j in range(i+1,n):
        if height[j] > height[i]:
            break
        count += 1

    if count > winner_count:
        winner_count = count
    count = 0

print(winner_count)
```

#### (21313번) 문어

```python
n = int(input())
L = [1,2]

if n % 2 == 0:
    result = L * (n//2)
else:
    result = L * (n//2)
    result.append(3)

for i in result:
    print(i,end=' ')
```

#### (2810번) 컵홀더

```python
n = int(input())
seat = input()

count_L = seat.count('LL')
count_S = seat.count('S')
count_holder = count_L + count_S + 1

if count_holder >= n:
    print(n)
else:
    print(count_holder)
```

더 간단하게 작성

```python
N = int(input())
seats = input()
holder = seats.count('LL')
if holder <= 1:
    print(N)
else:
    print(N - holder + 1)
```

#### (2839번) 설탕 배달

```python
n = int(input())

a = n // 5
b = 0
n1 = n % 5

for i in range(n//5):
    if n1 % 3 != 0:
        a -= 1
        n1 += 5
        b += n1 // 3
        n1 = n1 % 3
        if n1 == 0:
            break
    else:
        b = n1 // 3
        n1= n1 % 3
        break
if n1 == 0:
    print(a+b)
elif n1 == 3:
    print(1)
else:
    print(-1)
```

- 또 다른 풀이

```python
sugar = int(input())

bag = 0
while sugar >= 0 :
    if sugar % 5 == 0 :  # 5의 배수이면
        bag += (sugar // 5)  # 5로 나눈 몫을 구해야 정수가 됨
        print(bag)
        break
    sugar -= 3
    bag += 1  # 5의 배수가 될 때까지 설탕-3, 봉지+1
else :
    print(-1)
```

#### (14655번) 욱제는 도박쟁이야!!

```python
n = int(input())

round1 = list(map(int,input().split()))
round1 = [abs(n) for n in round1]

round2 = list(map(int,input().split()))
round2 = [n if n<0 else -n for n in round2]

print(sum(round1)-sum(round2))
```

#### (17224번) APC는 왜 서브태스크 대회가 되었을까?

```python
n, l, k = map(int,input().split())
score = []

for i in range(n):
    sub1, sub2 = map(int,input().split())
    if l >= sub2:
        score.append(140)
    elif l  >= sub1:
        score.append(100)
    else:
        score.append(0)

print(sum(sorted(score, reverse=True)[:k]))
```

#### (19564번) 반복

```python
sentence = input()
head = ord(sentence[0])
count = 0

for i in range(1,len(sentence)):
    if head >= ord(sentence[i]):
        count += 1
    head = ord(sentence[i])

print(count+1)
```
