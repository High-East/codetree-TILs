n, m = map(int, input().split())
arr = [[0] * m for _ in range(n)]

# 동, 남, 서 ,북
dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m

# 위치 및 방향 초기화
x, y, d = 0, 0, 0

# 초기값
arr[x][y] = 1

for i in range(2, n * m + 1):
    nx = x + dxs[d]
    ny = y + dys[d]
    
    # 방향 회전
    if not in_range(nx, ny) or (arr[nx][ny] != 0):
        d = (d + 1) % 4
    
    # 전진
    x += dxs[d]
    y += dys[d]

    # 채우기
    arr[x][y] = i

for x in arr:
    print(*x)