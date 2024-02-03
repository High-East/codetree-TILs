A = []
B = []

n, m = map(int, input().split())

# A 이동
cur = 0
for _ in range(n):
    d, t = input().split()
    t = int(t)
    mark = 1
    if d == 'L':
        mark = -1
    for _ in range(t):
        cur += mark
        A.append(cur)

# B 이동
cur = 0
for _ in range(m):
    d, t = input().split()
    t = int(t)
    mark = 1
    if d == 'L':
        mark = -1
    for _ in range(t):
        cur += mark
        B.append(cur)

# 비교
meet = -1
for i in range(len(A)):
    if A[i] == B[i]:
        meet = i + 1
        break
print(meet)