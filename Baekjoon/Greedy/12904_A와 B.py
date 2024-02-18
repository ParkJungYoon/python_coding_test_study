s = input()
t = input()

'''
연산 각각을 통해서 A랑 B를 추가할 수 있음.

아이디어
S -> T로 만드는게 아니라 T -> S로 만들어야 한다.
결과물을 가지고 할 수 있는 경우로 수행해서 s 길이 만큼 제거했을 때 같으면 성공, 다르면 실패.
'''

flag = False

while len(t) >= len(s):
    if s == t:
        flag = True
        break

    if t[-1] == 'A':
        t = t[:-1]
    elif t[-1] == 'B':
        t = t[:-1]
        t = t[::-1]
    
if flag:
    print(1)
else:
    print(0)