import sys
input = sys.stdin.readline

a, b = map(int, input().split())
n, m = map(int, input().split())

direction_mode = ["N", "E", "S", "W"]
# 위에 모드랑 같은 방향 순서대로
dx, dy = (0,1,0,-1), (1,0,-1,0)
robot = [[0,0,0]]

for _ in range(n):
    x, y, direction = input().split()
    # direction이 0이면 "N"
    robot.append([int(x), int(y), direction_mode.index(direction)])

commands = []
for _ in range(m):
    idx, command, number = input().split()
    commands.append((int(idx), command, int(number)))


def excute_command():
    if command == "L":
        if robot[idx][2] - 1 < 0:
            robot[idx][2] = 3
        else:
            robot[idx][2] -= 1
    elif command == "R":
        robot[idx][2] = (robot[idx][2] + 1) % 4
    elif command == "F":
        direc = robot[idx][2]
        robot[idx][0] += dx[direc]
        robot[idx][1] += dy[direc]

def check_error():
    cur_robot = robot[idx]

    if cur_robot[0] <= 0 or cur_robot[0] > a or cur_robot[1] <= 0 or cur_robot[1] > b:
        return (1, 0)

    for i in range(1, n+1):
        if i != idx:
            if cur_robot[0] == robot[i][0] and cur_robot[1] == robot[i][1]:
                return (2, i)
    return (0, 0)

for idx, command, number in commands:
    if command == "L" or command == "R": number %= 4

    for _ in range(number):
        excute_command()
        result = check_error()
        # print(robot)
        if result[0] == 1:
            print("Robot {} crashes into the wall".format(idx))
            exit()
        elif result[0] == 2:
            print("Robot {} crashes into robot {}".format(idx, result[1]))
            exit()

print("OK")