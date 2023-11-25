import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dic = {}

for _ in range(n):
    address, password = input().split()
    dic[address] = password

for _ in range(m):
    address = input().rstrip()
    print(dic[address])