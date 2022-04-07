## Class2

#### (1018번) 체스판 다시 칠하기

```py
import sys
n, m = map(int,input().split())
board = []

for i in range(n):
    board.append(sys.stdin.readline())
```

#### (1181번) 단어 정렬

```py
n = int(input())
word = []

for i in range(n):
    word.append(input())

word = list(set(word))

result = sorted(word, key=lambda x:(len(x),x))

for i in result:
    print(i)
```

sys.stdin.readline() 으로 input 변경

```py
import sys
n = int(input())
word = []

for i in range(n):
    word.append(sys.stdin.readline().strip())

word = list(set(word))
result = sorted(word, key=lambda x:(len(x),x))

for i in result:
    print(i)
```

#### (1259번) 팰린드롬수

```py
import sys

while True:
    num = sys.stdin.readline().strip()
    reverse_num = num[::-1]

    if int(num) == 0:
        break

    if num == reverse_num:
        print('yes')
    else:
        print('no')
```

#### (1436번) 영화감독 숌

```py
n = int(input())

for i in range(n):
```

#### (4153번) 직각삼각형

```python
while True:
    nums = list(map(int,input().split()))

    if sum(nums) == 0:
        break
    else:
        max_num = max(nums)
        nums.remove(max_num)

    if max_num**2 == (nums[0]**2 + nums[1]**2):
        print("right")
    else:
        print("wrong")
```
