'''
1. 짝꿍 만들기
 몇몇 테스트 케이스 시간초과
 73.7 / 100
'''

def solution(X, Y):
    x = list(X)
    y = list(Y)
    answer = []
    x.sort(reverse=True)
    y.sort(reverse=True)

    for i in x:
        # O(N)
        if i in y:
            answer.append(i)
            # 시간..!
            y.remove(i)
    # answer.sort(reverse=True)
    if not answer:
        return "-1"
    elif set(answer) == {"0"}:
        return "0"
    else:
        return ''.join(answer)

print(solution("100", "2345")) # "-1"
print(solution("100", "203045")) # "0" # 1 0 0 / 5 4 3 2 0 0 
print(solution("100", "123450")) # "10"
print(solution("12321", "42531")) # "321"
print(solution("5525", "1255")) # "552"