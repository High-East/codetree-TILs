n, t = map(int, input().split())
cmds = input()
arr = [list(map(int, input().split())) for _ in range(n)]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

# 동, 남, 서, 북
dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]

# 초기화
x, y, d = n // 2, n // 2, 3
result = arr[x][y]

# 진행
for cmd in cmds:
    if cmd == 'L':
        d = (d - 1 + 4) % 4
    elif cmd == 'R':
        d = (d + 1) % 4
    else:
        nx = x + dxs[d]
        ny = y + dys[d]
        if in_range(nx, ny):
            result += arr[nx][ny]
            x, y = nx, ny

print(result)