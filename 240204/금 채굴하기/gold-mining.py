n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]


def in_range(x, y):
    return (0 <= x) and (x < n) and (0 <= y) and (y < n)


def in_rhombus(x1, y1, x2, y2, d):
    return (abs(x1 - x2) + abs(y1 - y2)) <= d


def count_golds(x, y, k):
    golds = 0
    for i in range(-k, k + 1):
        for j in range(-k, k + 1):
            nx = x + i
            ny = y + j
            if in_range(nx, ny) and in_rhombus(x, y, nx, ny, k):
                golds += arr[nx][ny]
    return golds


max_golds = 0
for i in range(n):
    for j in range(n):
        for k in range(2 * (n - 1) + 1):
            golds = count_golds(i, j, k)
            benefit = (golds * m) - (k * k + (k + 1) * (k + 1))
            if benefit >= 0:
                max_golds = max(max_golds, golds)
print(max_golds)