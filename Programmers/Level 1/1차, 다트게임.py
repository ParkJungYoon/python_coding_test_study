import math

def solution(dartResult):
    
    dartResult = dartResult.replace('10', 'A')
    
    score = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A']
    bonus = ['S', 'D', 'T']
    
    scores = []
    
    for i in dartResult:
        if i in score:
            scores.append(10 if i == 'A' else int(i))
        elif i in bonus:
            scores[-1] = math.pow(scores[-1], bonus.index(i) + 1)
        elif i == "*":
            scores[-1] *= 2
            scores[-2:-1] *= 2
        elif i == "#":
            scores[-1] *= -1

    return sum(scores)