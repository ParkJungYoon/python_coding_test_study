'''
(1 ≤ E ≤ 15, 1 ≤ S ≤ 28, 1 ≤ M ≤ 19)

'''
e, s, m = map(int, input().split())
e2, s2, m2 = 1, 1, 1
time = 1
while True:
    if e2 % 16 == 0: e2 += 1
    if s2 % 29 == 0: s2 += 1
    if m2 % 20 == 0: m2 += 1

    if e2 % 16 == e and s2 % 29 == s and m2 % 20 == m:
        break
    time += 1
    e2 += 1
    s2 += 1
    m2 += 1

print(time)