n, m = list(map(int,input().split()))
card = list(map(int,input().split()))
result = 0
while len(card) > 2:
    for i in range(1,len(card)-1):
        for j in range(i+1,len(card)):
            card_sum = card[0] + card[i] + card[j]
            if card_sum <= m:
                result = max(result, card_sum)
    card = card[1:]
print(result)