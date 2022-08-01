### < heap >

- heap을 tuple로 구성했을 때 앞 숫자로 정렬하므로 정렬 기준 값은 첫번 째 원소로 하고 뒤는 원래 값 넣으면 된다. (절대값 힙 구할 때)
- 최대 힙을 구할 때는 (-num, num) 으로 저장해도 되지만 처음부터 -num으로 저장하고 pop한 다음 - 붙여주면 최대 힙 구현 완료. -> 조금 더 빠름.

### <collections.Counter를 이용한 카운팅>

- 예시

```py
from collections import Counter

Counter('hello world') # Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})
```

- `most_common()`: 데이터의 개수가 많은 순으로 정렬된 배열을 리턴

```py
from collections import Counter

Counter('hello world').most_common() # [('l', 3), ('o', 2), ('h', 1), ('e', 1), (' ', 1), ('w', 1), ('r', 1), ('d', 1)]
```

```py
from collections import Counter

Counter('hello world').most_common(1) # [('l', 3)]
```

#### 조합: from itertools import combinations

<br>

### < 리스트 컴프리헨션 >

- 리스트 안에서 for문, if문 등을 지정해서 리스트 생성 가능

- [설명블로그1](https://elvanov.com/1713)
- [설명블로그2](https://wikidocs.net/84393)

- b = [i + 5 for i in range(10) if i % 2 == 1]

<br>

### < zip() 함수 >

- [설명블로그](https://www.daleseo.com/python-zip/)

```python
numbers = [1,2,3]
letters = ['a', 'b', 'c']
for pair in zip(numbers, letters):
    print(pair)
```

### < enumerate 함수 >

```python
for idx, value in enumerate(['cc']):
    print(idx, value)
```

<br>

### < 유클리드 호제법 >

[출처](https://velog.io/@yerin4847/W1-%EC%9C%A0%ED%81%B4%EB%A6%AC%EB%93%9C-%ED%98%B8%EC%A0%9C%EB%B2%95)

: 유클리드 호제법은 **두개의 자연수에 대한 최대공약수를 구하는 알고리즘**이다.

1. 두 자연수 A, B에 대하여 (A>B) A를 B로 나눈 나머지를 R이라고 한다.
2. 이때 A와 B의 최대공약수는 B와 R의 최대공약수와 같다.

- MOD 연산: 두 값을 나눈 나머지를 구하는 연산이다.<br>
  GCD(1112,695)
  1112 mod 695 = 417<br>
  695 mod 417 = 278<br>
  417 mod 278 = 139<br>
  278 mod 139 = 0<br>
  이때, 139가 1112와 695의 최대공약수

```python
def gcd(a,b):
    if a%b == 0:
        return b
    else:
        return gcd(b,a%b)
print(gcd(190,160))
```

- 최소공배수<br>
  : 두 수 a와 b의 최소공배수는 a와 b의 곱을 a와 b의 최대공약수를 나눈 것과 같다.

<br>

### < 효율적인 소수 판별 >

- 2를 제외한 모든 소수는 홀수이다.
- $\sqrt{n}$ 미만의 자연수 중 n을 나눌 수 있는 수가 없다면, $\sqrt{n}$ 보다 큰 수는 n을 나누지 못한다. (나머지가 0이 될 수 없다.)

```python
def isPrime2(n):
    if n == 1:
        return False
    for i in range(2,int(n ** (1/2))+1):
        if n % i == 0:
            return False
    return True
```

<br>

### < 파이썬 문자열 합치기 >

- join 함수

`'구분자'.join(리스트)`

리스트의 값과 값 사이에 '구분자'에 들어온 구분자를 넣어서 하나의 문자열로 합쳐줍니다.

<br>

### < Reverse >

1. 정렬에서 사용
   - `리스트.sort(reverse=True)`
   - `sorted(리스트, reverse=True)`
2. reverse
   - `리스트.reverse()`
   - **return 값 X**, 원본 변경
3. reversed
   - `reversed(리스트)`
   - **return 값 O**, 원본 변경 X

<br>

### < 아스키 코드 >

- 공백 아스키 코드 32
- 대문자 알파벳의 아스키 코드 65(A) ~ 90(Z)
- 소문자 알파벳의 아스키 코드 97(a) ~ 122(z)
- isupper()와 islower()함수를 사용해 문자가 대문자인지 소문자인지 비교>

<br>

### < 파이썬 숫자, 문자, 알파벳 판별 >

1. **isalpha** : 알파벳인지 확인하기
   - `문자열.isalpha()`
   - 문자열에 숫자 및 공백이 포함되어 있으면 False를 리턴
2. **isdigit** : 숫자인지 확인
   - `문자열.isdigit()`
3. **isalnum** : 알파벳 또는 숫자인지 확인

<br>

### < sort >

1. sort

   - `리스트.sort()`
   - **return 값 X**, 원본 변경

2. sorted
   - `sorted(리스트)`
   - **return 값 O**, 원본 변경 X
   - 모든 iterable에 동작한다. (list, tuple, dict, 문자열 등)

<br>

### < list.count() >

: 리스트에서 특정 원소의 개수를 세기위해서 사용 가능

<br>

### < 람다식 >

```python
def square(x):
 return x * x

square = lambda x: x *
```

```python
movies = [
 "다크나이트,The Dark Knight,2008",
 "겨울왕국,Frozen,2013",
 "슈렉,Shrek,2001",
 "슈퍼맨,Superman,1978"
]

# 방법1
def get_eng_title(row):
 split = row.split(',')
 return split[1]

sorted(movies, key=get_eng_title)

# 방법2
sorted(movies,
 key=lambda row: row.split(',')[1])
```

<br>

### < 중복 제거 >

<순서 유지 O>

1. for 문

```python
my_list = ['A', 'B', 'C', 'D', 'B', 'D', 'E']
new_list = []
for v in my_list:
    if v not in new_list:
        new_list.append(v)
print(new_list)
출력된 값 ['A', 'B', 'C', 'D', 'E']
```

2. 딕셔너리

```python
list(dict.fromkeys(arr))
```

3. Sorted() 함수

```python
sorted(set(arr), key=lambda x: arr.index(x))
```

4. numpy 패키지 unique() 함수

```python
import numpy as np

A = [1,2,1,4,3,3,5,2]

result = list(np.unique(A))
```

<순서 유지 X>

1. set (집합 자료형)

: 중복을 허용하지 않는다.<br>
: 순서가 없다(Unordered).

<br>

### < 10진법 -> k진법 >

```python
answer = ''
    while n:
        answer += str(n % k)
        n = n // k
    answer = answer[::-1]
```

### < k진법 -> 10진법 >

```python
answer = int(n,k)
```
