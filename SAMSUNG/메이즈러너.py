import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
miro = [list(map(int, input().split())) for _ in range(n)]
# 회전 구현을 위한 2차원 배열
new_miro = [[0]*n for _ in range(n)]

parti = []
for i in range(m):
    x, y = map(int, input().split())
    parti.append((x-1,y-1))

temp_x, temp_y = list(map(int, input().split()))
exit = (temp_x-1, temp_y-1)
answer = 0
# 회전 최소 정사각형
sx, sy, s_size = 0, 0, 0

# 모든 참가자 이동
def move_all_parti():
    global exit, answer
    
    for i in range(m):
        if parti[i] == exit:
            continue
        
        x, y = parti[i][0], parti[i][1]
        exit_x, exit_y = exit

        # 참가자가 다른 행에 서있는 경우
        if exit_x != x:
            nx, ny = x, y
            if nx < exit_x:
                nx += 1
            else:
                nx -= 1
            
            if not miro[nx][ny]:
                parti[i] = (nx, ny)
                answer += 1
                continue
        # 다른 열에 서있는 경우
        if exit_y != y:
            nx, ny = x, y
            if ny < exit_y:
                ny += 1
            else:
                ny -= 1

            if not miro[nx][ny]:
                parti[i] = (nx, ny)
                answer += 1
                continue

# 한 명 이상의 참가자와 출구를 포함한 가장 작은 정사각형 찾기
def find_min_square():
    global exit, sx, sy, s_size
    exit_x, exit_y = exit

    # 정사각형 크기
    '''
    000
    000
    000
    '''
    for size in range(2, n+1):
        # 좌상단의 행,열 좌표 정하기
        for x in range(0, n-size+1):
            for y in range(0, n-size+1):
                # 출구가 해당 범위 안에 있는지 체크
                if not (x <= exit_x < x + size and y <= exit_y < y + size):
                    continue
                
                is_traveler_in = False
                for i in range(m):
                    tx, ty = parti[i]
                    if x <= tx < x + size and y <= ty < y + size:
                        # 출구에 있는 참가자 제외
                        if (tx, ty) != exit:
                            is_traveler_in = True
                            break
                
                if is_traveler_in:
                    sx, sy, s_size = x, y, size
                    return

'''
이때 회전이 일반 회전이랑 다른건 (0,0)부터 회전이 아니라 특정 구역에서 회전하는거라 (0,0)으로 옮기고 회전하고 다시 더해줘야함.
'''

# 정사각형 내부의 벽 회전
def rotate_square():
    # 내구성 -1
    for x in range(sx, sx + s_size):
        for y in range(sy, sy + s_size):
            if miro[x][y]:
                miro[x][y] -= 1
    
    # 시계방향으로 90도 회전
    '''
    90도 회전 규칙
    - 회전한 후 행 번호: 회전하기 전 열 번호
    - 회전한 후 열 번호: N-1-회전하기 전 행 번호
    - (0,0) -> (0,3)
    '''
    for x in range(sx, sx + s_size):
        for y in range(sy, sy + s_size):
            # Step 1. (sx, sy)를 (0, 0)으로 변환
            ox, oy = x - sx, y - sy
            # Step 2. 변환된 상태에서는 회전 이후의 좌표가 (x, y) . (y, square_n - x - 1)
            rx, ry = oy, s_size-1-ox
            # Step 3. 다시 (sx, sy)를 더해줍니다.
            new_miro[rx+sx][ry+sy] = miro[x][y]

    for x in range(sx, sx + s_size):
        for y in range(sy, sy + s_size):
            miro[x][y] = new_miro[x][y]

# 정사각형에 포함된 참가자와 출구를 회전
def rotate_parti_and_exit():
    global exit

    for i in range(m):
        x, y = parti[i]
        # 정사각형 범위에 있으면
        if sx <= x < sx + s_size and sy <=  y < sy + s_size:
            ox, oy = x - sx, y - sy
            rx, ry = oy, s_size-1-ox
            parti[i] = (rx+sx, ry+sy)
    
    exit_x, exit_y = exit
    if sx <= exit_x < sx + s_size and sy <= exit_y < sy + s_size:
        # (2,2)일 때 -> (2,0) -> (0,0)
        ox, oy = exit_x - sx, exit_y - sy
        rx, ry = oy, s_size-1-ox
        exit = (rx+sx, ry+sy)


for _ in range(k):
    # 1. 참가자들 이동
    move_all_parti()

    # 2. 모든 참가자가 출구로 탈출했는지 확인
    is_all_escaped = True
    for i in range(m):
        if exit != parti[i]:
            is_all_escaped = False
            break
    if is_all_escaped:
        break
    
    # 3. 한 명 이상의 참가자와 출구를 포함한 가장 작은 정사각형 찾기
    find_min_square()

    # 4. 벽과 출구 회전
    rotate_square()
    rotate_parti_and_exit()

print(answer)
print(exit[0]+1, exit[1]+1)