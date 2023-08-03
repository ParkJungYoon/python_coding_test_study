from collections import defaultdict

t = int(input())

for _ in range(t):
    w = input()
    k = int(input())
    alphabet = defaultdict(list)
    three_condition = 10**9
    four_condition = 0

    for i in range(len(w)):
        # 현재 문자가 k개 이상이면 인덱스 value로
        if w.count(w[i]) >= k:
            alphabet[w[i]].append(i)
    # print(alphabet)

    if not alphabet: 
        print(-1)
        continue

    for v in alphabet.values():
        for vv in range(len(v)-k+1):
            if v[vv+k-1] - v[vv] + 1 < three_condition:
                three_condition = v[vv+k-1] - v[vv] + 1

            if v[vv+k-1] - v[vv] + 1 > four_condition:
                four_condition = v[vv+k-1] - v[vv] + 1
    print(three_condition, four_condition)

    # dp = [0] * 26
    # start = 0
    # three_condition = 10**9
    # four_condition = 0
    
    # for end in range(len(w)):
    #     dp[ord(w[end])-97] += 1
    #     if dp[ord(w[end])-97] == k:
    #         three_condition = min(three_condition, end-start+1)

'''
{'u': [1, 7], 'r': [4, 11], 'a': [5, 8, 13], 'o': [10, 15]}
'''