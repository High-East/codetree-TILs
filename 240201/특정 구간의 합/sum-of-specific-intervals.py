n, m = map(int, input().split())
A = list(map(int, input().split()))
for _ in range(m):
    i, j = map(int, input().split())
    print(sum(A[i - 1 : j]))