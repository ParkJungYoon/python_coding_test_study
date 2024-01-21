# 복습

stick = input()
left_count = 0
answer = 0

for s in range(len(stick)):
    if stick[s] == "(":
        left_count += 1
    else:
        if stick[s-1] == "(":
            left_count -= 1
            answer += left_count
        else:
            # )) 가 나오면 하나의 스틱이 끝났다는 이야기
            left_count -= 1
            answer += 1

print(answer)


'''

# 시간복잡도 O(N)

stick = input()

left_count = 0
stick_count = 0

for i in range(len(stick)):
    if stick[i] == "(":
        left_count += 1
    else:
        if stick[i-1] == "(":
            left_count -= 1
            stick_count += left_count
        else:
            # ))가 연속으로 나왔다는건 막대가 끝났다는 의미라서 오른쪽 끝 1개만 나오고 없어져서 +1
            left_count -= 1
            stick_count += 1

print(stick_count)
'''