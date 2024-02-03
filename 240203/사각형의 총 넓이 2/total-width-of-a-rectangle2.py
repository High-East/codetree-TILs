OFFSET = 100
arr = [[0] * (OFFSET * 2 + 1) for _ in range(OFFSET * 2 + 1)]

n = int(input())
for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            arr[i + OFFSET][j + OFFSET] += 1

cnt = 0
for i in range(OFFSET * 2 + 1):
    for j in range(OFFSET * 2 + 1):
        if arr[i][j] != 0:
            cnt += 1
print(cnt)