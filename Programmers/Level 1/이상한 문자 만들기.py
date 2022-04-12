def solution(s):
    answer = []
    string = s.split(' ')
    for i in string:
        a = ''
        for j in range(len(i)):
            if j % 2 == 0:
                 a += i[j].upper()
            else:
                 a += i[j].lower() 
        answer.append(a)
    return ' '.join(answer)