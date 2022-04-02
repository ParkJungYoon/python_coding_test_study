## BOJ, 그리디

#### 2022.04.01

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

#### 2022.04.02

#### (2930번) 가위 바위 보

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
