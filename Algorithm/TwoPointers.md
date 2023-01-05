# 투 포인터 (Two Pointers)

- **투 포인터 알고리즘**은 <u>리스트에 순차적으로 접근해야 할 때 두 개의 점의 위치를 기록하면서 처리</u>하는 알고리즘을 의미한다.
- 리스트에 담긴 데이터에 순차적으로 접근해야 할 때는 **시작점**과 **끝점** 2개의 점으로 접근할 데이터의 범위를 표현할 수 있다.

## 특정한 합을 가지는 부분 연속 수열 찾기

```
- N개 자연수로 구성된 수열
- 합이 M인 부분 연속 수열의 개수
- 수행 시간 제한은 O(N)
```

### 💡 문제 해결 아이디어

- 투 포인터를 활용
1. 시작점(start)와 끝점(end)이 첫 번째 원소의 인덱스(0)를 가르키도록 한다. 
2. 현재 부분 합이 M과 같다면, 카운트한다.
3. 현재 부분 합이 M보다 작다면, end를 1 증가시킨다.
4. 현재 부분 합이 M보다 크거나 같다면, start를 1 증가시킨다.
5. 모든 경우를 확인할 때가지 2번부터 4번까지의 과정을 반복한다.

```py
n = 5  # 데이터의 개수
m = 5  # 찾고자 하는 부분합
data = [1, 2, 3, 4, 5]  # 전체 수열

count = 0
interval_sum = 0
end = 0

# start를 차례대로 증가시키며 반복
for start in range(n):
    # end를 가능한 만큼 이동시키기
    while interval_sum < m and end < n:
        interval_sum += data[end]
        end += 1
    # 부분합이 m일 때 카운트 증가
    if interval_sum == m:
        count += 1
    interval_sum -= data[start]

print(count)
```

### 관련 문제집
- [바킹독 투포인터](https://www.acmicpc.net/workbook/view/8709)


---

## Reference & Additional Resources

- [한빛미디어] 이것이 취업을 위한 코딩 테스트다 with 파이썬 (나동빈 저)

