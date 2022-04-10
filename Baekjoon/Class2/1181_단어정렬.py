import sys
n = int(input())
word = []

for i in range(n):
    word.append(sys.stdin.readline().strip())

word = list(set(word))
result = sorted(word, key=lambda x:(len(x),x))

for i in result:
    print(i)