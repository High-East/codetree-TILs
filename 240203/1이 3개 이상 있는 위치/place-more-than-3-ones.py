n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n


def count_one(x, y):
    num = 0
    for dx, dy in zip(dxs, dys):
        nx = x + dx
        ny = y + dy
        if in_range(nx, ny) and arr[nx][ny] == 1:
            num += 1
    return num

cnt = 0
for i in range(n):
    for j in range(n):
        if count_one(i, j) >= 3:
            cnt += 1
print(cnt)