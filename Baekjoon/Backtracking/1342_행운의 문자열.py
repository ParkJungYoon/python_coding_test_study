s = input()

'''
아이디어 : 문자열을 딕셔너리로 가지고 있으면서 이전 문자열과 다른 문자열로 하나씩 써감.
백트래킹으로 하다가 마지막에 주어진 문자열 개수만큼 완성했을 때 +1
'''

alphabet = {}
for ss in s:
    if ss in alphabet.keys():
        alphabet[ss] += 1
    else:
        alphabet[ss] = 1

count = 0
def backtracking(pre_alpha, idx):
    global count

    if len(s) == idx:
        count += 1
        return

    for key in alphabet.keys():
        if pre_alpha != key and alphabet[key] > 0:
            alphabet[key] -= 1
            backtracking(key, idx + 1)
            alphabet[key] += 1
    
backtracking('', 0)
print(count)