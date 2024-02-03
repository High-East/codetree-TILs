n, m = map(int, input().split())
arr = [[0] * m for _ in range(n)]

# 동, 남, 서 ,북
dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m

# 위치 및 방향 초기화
x, y, d = 0, 0, 0

for i in range(1, n * m + 1):
    arr[x][y] = i
    
    # 방향 회전
    if not in_range(x + dxs[d], y + dys[d]) or (arr[x + dxs[d]][y + dys[d]] != 0):
        d = (d + 1) % 4
    
    # 전진
    x += dxs[d]
    y += dys[d]

for x in arr:
    print(*x)