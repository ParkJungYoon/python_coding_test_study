# 이진 탐색 알고리즘 (Binary Search)

- 탐색(Search): 많은 양의 데이터 중에서 원하는 데이터를 찾는 과정 <br>
  ex) 선형 검색, 이진 검색, 너비우선탐색(BFS), 깊이우선탐색(DFS)

- 이진 탐색: 정렬되어 있는 리스트에서 **탐색 범위를 절반씩 좁혀가며 데이터를 탐색**하는 방법
  <br>
  - 이진 탐색은 시작점, 끝점, 중간점을 이용하여 탐색 범위를 설정한다.

<br>

## 시간 복잡도

- 단계마다 탐색 범위를 2로 나누는 것과 동일하므로 연산 횟수는 $\log_2 N$에 비례한다.
- 이진 탐색은 탐색 범위를 절반씩 줄이며, 시간 복잡도는 O(log N)를 보장한다.

<br>

## 소스코드 : 재귀적 구현

```py
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start+end) // 2
    # 찾은 경우 중간점 인덱스 반환
    if array[mid] == target:
        return mid
    # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    else:
        return binary_search(array, target, mid+1, end)
# n(원소의 개수)과 target(찾고자 하는 값)을 입력 받기
n, target = list(map(int,input().split()))
# 전체 원소 입력 받기
array = list(map(int,input().split()))

# 이진 탐색 수행 결과 출력
result = binary_search(array, target, 0, n-1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)
```

## 파이썬 이진 탐색 라이브러리

- bisect_left(a, x): 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 왼쪽 인덱스를 반환
- bisect_right(a, x): 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 오른쪽 인덱스를 반환

```py
from bisect import bisect_left, bisect_right

a = [1, 2, 4, 4, 8]
x = 4

print(bisect_left(a, x))
print(bisect_right(a, x))
```

### 라이브러리 활용

< 값이 특정 범위에 속하는 데이터 개수 구하기 >

```py
from bisect import bisect_left, bisect_right

def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

# 배열 선언
a = [1,2,3,3,3,3,4,4,8,9]

# 값이 4인 데이터 개수 출력
print(count_by_range(a, 4, 4))

# 값이 [-1,3] 범위에 있는 데이터 개수 출력
print(count_by_range(a, -1, 3))
```

<br>

## 파라메트릭 서치 (Parametric Search)

- 파라메트릭 서치: <u>최적화 문제를 결정 문제('예' 혹은 '아니오')로 바꾸어 해결하는 기법</u>

<br>

### 문제 해결

- 큰 탐색 범위를 (ex)0부터 10억까지의 정수) 보면 가장 먼저 **이진 탐색**을 떠올려야 한다.

---

## Reference & Additional Resources

- [한빛미디어] 이것이 취업을 위한 코딩 테스트다 with 파이썬 (나동빈 저)
- [사진 출처](https://github.com/HyeminNoh/Tech-Stack)
