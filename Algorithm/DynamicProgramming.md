# 다이나믹 프로그래밍 (Dynamic Programming)

다이나믹 프로그래밍(=동적 계획법)은 메모리를 적절히 사용하여 수행 시간 효율성을 비약적으로 향상시키는 방법이다.
<br>

### 조건

1. **최적 부분 구조 (Optimal Substructure)**
   - 큰 문제를 작은 문제로 나눌 수 있으며 작은 문제의 답을 모아서 큰 문제를 해결할 수 있다.
2. **중복되는 부분 문제 (Overlapping Subproblem)**
   - 동일한 작은 문제를 반복적으로 해결해야 한다.

## 1. 피보나치 수열

### > 비효율적 해법 : 재귀

- 점화식: <u>인접한 항들 사이의 관계식</u>

$$a_{n} = a_{n-1} + a_{n-2}, a_{1} = 1, a_{2} = 1 $$

- 재귀 소스 코드

```py
def fibo(x):
    if x == 1 or x == 2:
        return 1
    return fibo(x-1) + fibo(x-2)

print(fibo(4))
```

```java
import java.util.*;

public class Main {
    public static int fibo(int x) {
        if (x == 1 || x ==2) {
            return 1;
        }
        return fibo(x-1) + fibo(x-2);
    }

    public static void main(String[] args) {
        System.out.println(fibo(4));
    }
}
```

- 시간 복잡도 분석
  - 단순 재귀 함수로 피보나치 수열을 해결하면 지수 시간 복잡도
  - 여러 번 호출 => **중복되는 부분 문제**
  - **O((2<sup>N</sup>)**

<br>

### > 효율적인 해법: 다이나믹 프로그래밍

1. 조건 확인
   1. **최적 부분 구조** : 큰 문제를 작은 문제로 나눌 수 있다.
   2. **중복되는 부분 문제** : 동일한 작은 문제를 반복적으로 해결한다.
2. 구현

### 1) 하향식 : 메모이제이션

한 번 계산한 결과를 메모리 공간에 메모하는 기법

- 캐싱

<br>

---

## Reference & Additional Resources

- [한빛미디어] 이것이 취업을 위한 코딩 테스트다 with 파이썬 (나동빈 저)

```

```
