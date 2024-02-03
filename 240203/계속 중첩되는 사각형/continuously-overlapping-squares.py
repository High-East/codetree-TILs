OFFSET = 100
arr = [[0] * (OFFSET * 2 + 1) for _ in range(OFFSET * 2 + 1)]

n = int(input())
for i in range(1, n + 1):
    x1, y1, x2, y2 = map(int, input().split())
    # 홀수면 RED
    if i % 2 != 0:
        mark = 'R'
    # 짝수면 BLUE
    else:
        mark = 'B'
    for x in range(x1, x2):
        for y in range(y1, y2):
            arr[x + OFFSET][y + OFFSET] = mark

cnt = 0
for i in range(OFFSET * 2 + 1):
    for j in range(OFFSET * 2 + 1):
        if arr[i][j] == 'B':
            cnt += 1
print(cnt)