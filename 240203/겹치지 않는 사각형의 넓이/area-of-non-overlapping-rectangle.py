OFFSET = 1000
arr = [[0] * (OFFSET * 2 + 1) for _ in range(OFFSET * 2 + 1)]

A = tuple(map(int, input().split()))
B = tuple(map(int, input().split()))
M = tuple(map(int, input().split()))

for i, (x1, y1, x2, y2) in enumerate([A, B, M]):
    mark = 1
    if i == 2:
        mark = 0
    for x in range(x1, x2):
        for y in range(y1, y2):
            arr[x + OFFSET][y + OFFSET] = mark

cnt = 0
for i in range(OFFSET * 2 + 1):
    for j in range(OFFSET * 2 + 1):
        if arr[i][j]:
            cnt += 1
print(cnt)