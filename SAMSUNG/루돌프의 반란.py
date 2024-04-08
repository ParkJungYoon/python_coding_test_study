import sys
input = sys.stdin.readline

'''
프로그램 요구사항
- 기절 시킨 산타는 다음 턴에 다시 살아남.
'''


n, m, p, c, d = map(int, input().split())
ruru = list(map(int, input().split()))

santa = [[0,0] for _ in range(p)]
for _ in range(p):
    num, x, y = map(int, input().split())
    santa[num-1] = [x,y]

# 기절 여부
santa_faint = [0] * p
# 생존 여부
is_live = [True] * p
# 산타 점수
score = [0] * p

san_dx, san_dy = (-1,0,1,0), (0,1,0,-1)

# 거리 계산
def calcu_dist(r1,c1,r2,c2):
    return (r1-r2) ** 2 + (c1-c2) ** 2

# 게임판 안에 존재하는지 체크
def is_range(x,y):
    return 1 <= x <= n and 1 <= y <= n


# 루돌프가 돌진한 산타 선택
# 이때 기절한 산타는 선택하면 안된다!!!! 이걸 빼먹어서 계속 틀림
def ru_choice():
    tmp = 10 ** 9
    target_santa = [0, 0]
    
    idx = -1
    for san in santa:
        idx += 1
        # 죽은 산타는 패쓰, 기절한 산타는 ㄱㅊ
        if not is_live[idx]:
            continue

        dist = calcu_dist(ruru[0],ruru[1],san[0],san[1])
        if dist < tmp:
            tmp = dist
            target_santa = san
        elif dist == tmp:
            if target_santa[0] > san[0]:
                continue
            elif target_santa[0] < san[0]:
                target_santa = san
            elif target_santa[0] == san[0]:
                if target_santa[1] > san[1]:
                    continue
                elif target_santa[1] < san[1]:
                    target_santa = san

    return target_santa

# 루돌프의 움직임
def move_ruru(target_san):
    dx, dy = 0, 0
    # dx 정하기
    if target_san[0] < ruru[0]: dx = -1
    elif target_san[0] == ruru[0]: dx = 0
    elif target_san[0] > ruru[0]: dx = 1
    # dy 정하기
    if target_san[1] < ruru[1]: dy = -1
    elif target_san[1] == ruru[1]: dy = 0
    elif target_san[1] > ruru[1]: dy = 1
    
    ruru[0] += dx
    ruru[1] += dy

    return dx, dy

# 루돌프 충돌
def ruru_crush(ru_dx, ru_dy):
    global is_live
    # 루돌프랑 같은 좌표를 가진 인덱스 다 꺼내기(존재할 수 있는 이유는 죽은 산타 자리에 산 산타가 올 수도 있어서)
    idx_list = [i for i, value in enumerate(santa) if value == ruru]

    for idx in idx_list:
        # 죽은 산타면 패쓰
        if not is_live[idx]:
            break

        # 산타 점수 얻음
        score[idx] += c
        # 산타 밀려남
        santa[idx][0] += (ru_dx*c)
        santa[idx][1] += (ru_dy*c)
        # 산타 기절
        santa_faint[idx] = round + 2
        # 1) 게임판 밖인 경우
        if not is_range(santa[idx][0],santa[idx][1]):
            is_live[idx] = False
            break
        # 2) 다른 산타가 있는 경우 - 상호작용
        interaction(idx,santa[idx][0],santa[idx][1],ru_dx,ru_dy)


# 산타 충돌
def santa_crush(idx,san_dx,san_dy):
    global is_live
    # 산타 점수 얻음
    score[idx] += d
    # 산타 밀려남(자신의 이동 반대로)
    santa[idx][0] += (san_dx*d*(-1))
    santa[idx][1] += (san_dy*d*(-1))
    # 산타 기절
    santa_faint[idx] = round + 2
    # 1) 게임판 밖인 경우
    if not is_range(santa[idx][0],santa[idx][1]):
        is_live[idx] = False
        return
    # 2) 다른 산타가 있는 경우 - 상호작용
    # 자신이 밀린 반대 방향으로 이동
    interaction(idx,santa[idx][0],santa[idx][1],-san_dx,-san_dy)


# 상호작용
 # 상호작용 받는 루돌프도 산타가 반대로 이동한 방향으로 밀림. 위에서 - 붙여서 변수 넘겨줌
def interaction(i,x,y,san_dx,san_dy):
    global is_live
    for idx in range(len(santa)):
        if i == idx or not is_live[idx]:
            continue
        if santa[idx][0] == x and santa[idx][1] == y:
            # 원래 있던 산타가 밀려남
            nx = santa[idx][0] + san_dx
            ny = santa[idx][1] + san_dy
            # 1) 게임판 밖인 경우
            if not is_range(nx,ny):
                is_live[idx] = False
                continue
            # 2) 다른 산타가 있는 경우 - 상호작용
            santa[idx][0], santa[idx][1] = nx, ny
            interaction(idx,nx,ny,san_dx,san_dy)

# 산타 1명 이동
# 기절하지 않았고 살아있는 산타만 움직임
# 산타는 다른 산타가 있는 칸이나 게임판 밖으로는 움직일 수 없습니다. 다른 산타가 있는 칸에 못가는걸 빼먹음.
def move_santa_one(x,y):
    tmp = 10 ** 9
    dx, dy = 0, 0

    for i in range(4):
        nx, ny = x + san_dx[i], y + san_dy[i]
        if is_range(nx, ny) and [nx,ny] not in santa:
            dist = calcu_dist(ruru[0],ruru[1],nx,ny)
            if dist < tmp:
                tmp = dist
                dx, dy = san_dx[i], san_dy[i]

    return [x + dx, y + dy, dx, dy]

# 산타 전체 이동 (충돌, 상호작용, 기절)
def move_santa_all():
    for i in range(p):
        if not is_live[i] or santa_faint[i] > round:
            continue
        santa[i][0], santa[i][1], san_dx, san_dy = move_santa_one(santa[i][0], santa[i][1])
        if ruru == [santa[i][0], santa[i][1]]:
            # 산타 충돌
            santa_crush(i,san_dx,san_dy)


for round in range(m):
    # 1. 루돌프의 움직임
    target_san = ru_choice()
    ru_dx, ru_dy = move_ruru(target_san)
    # 2. 루돌프 움직임으로 충돌, 상호작용, 기절
    if ruru in santa:
        ruru_crush(ru_dx, ru_dy)
    # 3. 산타 움직임으로 충돌, 상호작용, 기절
    move_santa_all()
    # 4. 살아있는 산타 점수 1점씩 더하기
    for i in range(p):
        if is_live[i]:
            score[i] += 1

    if sum([1 for i in is_live if i]) == 0:
        break

print(*score)

'''
# 산타와 루돌프의 위치를 좌표로만 가지고 해서 로직이 꼬였음.

n, m, p, c, d = map(int, input().split())
ruru = list(map(int, input().split()))

# 산타가 탈락할 때 점수를 result에 저장하고 3가지 리스트에서 산타 인덱스 번째 값을 제거한다.
# 위치
santa = [[0,0] for _ in range(p)]
# 기절 여부
santa_faint = [False] * p
# 산타 점수
score = [0] * p
# 최종 점수
result = [0] * p
out_santa = 0

for _ in range(p):
    num, x, y = map(int, input().split())
    santa[num-1][0] = x
    santa[num-1][1] = y

san_dx, san_dy = (0,1,0,-1), (1,0,-1,0)

# 거리 계산
def calcu_dist(r1,c1,r2,c2):
    return (r1-r2) ** 2 + (c1-c2) ** 2


# 루돌프가 돌진한 산타 선택
def ru_choice():
    tmp = 10 ** 9
    target_santa = [0, 0]

    for san in santa:
        dist = calcu_dist(ruru[0],ruru[1],san[0],san[1])
        if dist < tmp:
            tmp = dist
            target_santa = san
        elif dist == tmp:
            if target_santa[0] > san[0]:
                continue
            elif target_santa[0] < san[0]:
                target_santa = san
            elif target_santa[0] == san[0]:
                if target_santa[1] > san[1]:
                    continue
                elif target_santa[1] < san[1]:
                    target_santa = san
    return target_santa


# (2) 루돌프의 움직임
def move_ruru(target_san):
    dx, dy = 0, 0
    # dx 정하기
    if target_san[0] < ruru[0]: dx = -1
    elif target_san[0] == ruru[0]: dx = 0
    elif target_san[0] > ruru[0]: dx = 1
    # dy 정하기
    if target_san[1] < ruru[1]: dy = -1
    elif target_san[1] == ruru[1]: dy = 0
    elif target_san[1] > ruru[1]: dy = 1
    
    ruru[0] += dx
    ruru[1] += dy

    return dx, dy


# 산타 아웃
def santa_out(idx):
    global out_santa

    result[idx] = score[idx]
    del santa[idx]
    del santa_faint[idx]
    del score[idx]
    out_santa += 1


# (4) 루돌프 충돌
def ruru_crush(ru_dx, ru_dy):
    while ruru in santa:
        idx = santa.index(ruru)
        if santa[idx][0] == ruru[0] and santa[idx][1] == ruru[1]:
        # 산타 점수 얻음
            score[idx] += c
        # 산타 밀려남
        santa[idx][0] += (ru_dx*c)
        santa[idx][1] += (ru_dy*c)
        # 산타 기절
        santa_faint[idx] = True
        # 1) 게임판 밖인 경우
        if santa[idx][0] < 1 or santa[idx][0] > n or santa[idx][1] < 1 or santa[idx][1] > n:
            santa_out(idx)
            continue
        # 2) 다른 산타가 있는 경우 - 상호작용
        interaction(idx,santa[idx][0],santa[idx][1],ru_dx,ru_dy)


# (4) 산타 충돌
def santa_crush(idx,san_dx,san_dy):
    # 산타 점수 얻음
    score[idx] += d
    # 산타 밀려남
    santa[idx][0] += (san_dx*d*(-1))
    santa[idx][1] += (san_dy*d*(-1))
    # 산타 기절
    santa_faint[idx] = True
    # 1) 게임판 밖인 경우
    if santa[idx][0] < 1 or santa[idx][0] > n or santa[idx][1] < 1 or santa[idx][1] > n:
        santa_out(idx)
    # 2) 다른 산타가 있는 경우 - 상호작용
    interaction(idx,santa[idx][0],santa[idx][1],san_dx,san_dy)


# (5) 상호작용       
def interaction(i,x,y,ru_dx,ru_dy):
    for idx in range(len(santa)):
        if i == idx:
            continue
        if santa[idx][0] == x and santa[idx][1] == y:
            # 원래 있던 산타가 밀려남
            nx = santa[idx][0] + ru_dx
            ny = santa[idx][1] + ru_dy
            # 1) 게임판 밖인 경우
            if nx < 1 or nx > n or ny < 1 or ny > n:
                santa_out(idx)
                continue
            # 2) 다른 산타가 있는 경우 - 상호작용
            santa[idx][0], santa[idx][1] = nx, ny
            interaction(idx,nx,ny,ru_dx,ru_dy)

# (3) 산타 1명 이동
# 기절하지 않은 산타만 움직임
def move_santa_one(i,x,y):
    tmp = 10 ** 9
    dx, dy = 0, 0

    if santa_faint[i]:
        santa_faint[i] = False
        return [x, y, 0, 0]

    for i in range(4):
        nx, ny = x + san_dx[i], y + san_dy[i]
        if 1 <= nx <= n and 1 <= ny <= n:
            dist = calcu_dist(ruru[0],ruru[1],nx,ny)
            if dist < tmp:
                tmp = dist
                dx, dy = san_dx[i], san_dy[i]

    return [x + dx, y + dy, dx, dy]

# (3) 산타 전체 이동 (충돌, 상호작용, 기절)
def move_santa_all():
    for i in range(len(santa)):
        i -= out_santa
        santa[i][0], santa[i][1], san_dx,san_dy = move_santa_one(i,santa[i][0], santa[i][1])
        if ruru == [santa[i][0], santa[i][1]]:
            # 산타 충돌
            santa_crush(i,san_dx,san_dy)



for _ in range(m):
    # 1. 루돌프의 움직임
    target_san = ru_choice()
    ru_dx, ru_dy = move_ruru(target_san)
    print(ruru)
    # 2. 루돌프 움직임으로 충돌, 상호작용, 기절
    if ruru in santa:
        ruru_crush(ru_dx, ru_dy)

    # 3. 산타 움직임으로 충돌, 상호작용, 기절
    move_santa_all()
    out_santa = 0

    print(santa)
'''