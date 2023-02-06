import sys
input = sys.stdin.readline

n, m = map(int, input().split())
name_dic = {}

for i in range(n):
    name = input().rstrip()
    name_dic[name] = 1

for j in range(m):
    name = input().rstrip()
    if name in name_dic.keys():
        name_dic[name] += 1

answer = []
for key, value in name_dic.items():
    if value == 2: answer.append(key)


print(len(answer))
if answer: 
    print(*sorted(answer), sep="\n")