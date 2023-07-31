import sys
import math
input = sys.stdin.readline

def calculate_distance(nx, ny):
    return math.sqrt(abs(xs-nx)**2 + abs(ys-ny)**2)

xs, ys = map(int, input().split())
xe, ye, dx, dy = map(int, input().split())

if dx == 0 and dy == 0:
    print(xe, ye)
else:
    # 몇 초에 내리는지 제한 없어서 1초 아닌 0.5초 등에 뛰어내릴 수 있다.
    gcd = math.gcd(dx,dy)
    dx, dy = dx // gcd, dy // gcd

    answer_x, answer_y = xe, ye
    distance = calculate_distance(xe, ye)
    while True:
        xe += dx
        ye += dy
        current = calculate_distance(xe,ye)
        if distance <= current:
            print(answer_x, answer_y)
            break
        else:
            answer_x, answer_y = xe, ye
            distance = current

'''
반례

50 72
0 0 7 3
ans: 70 30
'''