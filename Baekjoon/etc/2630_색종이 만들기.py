import sys
input = sys.stdin.readline
n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]

def check_white_blue(block):
    blue_count = len(block) * len(block)
    count = 0
    for b in block:
        count += sum(b)
    if count == 0:
        return "white"
    elif count == blue_count:
        return "blue"
    return False

white = 0
blue = 0
def divide_conquer(block):
    global white, blue
    check = check_white_blue(block)
    if check != False:
        if check == "white": white += 1
        elif check == "blue": blue += 1
        return
    n = len(block) // 2
    quadrant1 = [b[n:] for b in block[0:n]]
    quadrant2 = [b[0:n] for b in block[0:n]]
    quadrant3 = [b[0:n] for b in block[n:]]
    quadrant4 = [b[n:] for b in block[n:]]
    divide_conquer(quadrant1)
    divide_conquer(quadrant2)
    divide_conquer(quadrant3)
    divide_conquer(quadrant4)

divide_conquer(graph)
print(white)
print(blue)