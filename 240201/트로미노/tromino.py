n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
max_sum = 0

# check first block
for i in range(n - 1):
    for j in range(m - 1):
        block = [arr[i][j], arr[i + 1][j], arr[i][j + 1], arr[i + 1][j + 1]]
        max_sum = max(max_sum, sum(block) - min(block))

# check horizontal block
for i in range(n):
    for j in range(m - 2):
        block = arr[i][j: j + 2]
        max_sum = max(max_sum, sum(block))

# check vertical block
for i in range(n - 2):
    for j in range(m):
        block = [arr[i][j], arr[i + 1][j], arr[i + 2][j]]
        max_sum = max(max_sum, sum(block))

print(max_sum)