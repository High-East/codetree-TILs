# 동, 남, 서, 북
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

cmd = input()

x, y = 0, 0
cur = 3

for c in cmd:
    if c == 'L':
        cur = (cur -1 + 4) % 4
    elif c == 'R':
        cur = (cur + 1) % 4
    else:
        x += dx[cur]
        y += dy[cur]
print(x, y)