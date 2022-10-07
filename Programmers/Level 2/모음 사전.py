# 데카르트 곱이라고도 하는 cartesian product를 표현할 때 사용하는 메소드이다(DB의 join, 관계 대수의 product를 생각하면 된다). 이 메소드의 특징은 두 개 이상의 리스트의 모든 조합을 구할 때 사용된다.
# product(iterator1, iterator2, .. , [repeat=1]) :
# 중복 순열
'''
from itertools import product

iterator = ['A','B','C','D','E']

print(list(product(iterator, repeat = 1)))

>>> [('A',), ('B',), ('C',), ('D',), ('E',)]

print(list(product(iterator, repeat = 2)))

>>> [('A', 'A'), ('A', 'B'), ('A', 'C'), ('A', 'D'), ('A', 'E'), ('B', 'A'), ('B', 'B'), ('B', 'C'), ('B', 'D'), ('B', 'E'), ('C', 'A'), ('C', 'B'), ('C', 'C'), ('C', 'D'), ('C', 'E'), ('D', 'A'), ('D', 'B'), ('D', 'C'), ('D', 'D'), ('D', 'E'), ('E', 'A'), ('E', 'B'), ('E', 'C'), ('E', 'D'), ('E', 'E')]
'''

from itertools import product

def solution(word):
    dict = []
    # 단어 길이가 1이상 5이하
    for i in range(1, 6):
        for j in product(['A', 'E', 'I', 'O', 'U'], repeat=i):
            dict.append(''.join(list(j)))

    dict.sort()
    return dict.index(word) + 1

# 6
print(solution("AAAAE"))
# 10
print(solution("AAAE"))
# 1563
print(solution("I"))
# 1189
print(solution("EIO"))
