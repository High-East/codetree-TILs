n, s = map(int, input().split())
arr = list(map(int, input().split()))

result = s

for i in range(n - 1):
    for j in range(i + 1, n):
        num = 0
        for k in range(n):
            if (k != i) and (k != j):
                num += arr[k]
        result = min(result, abs(s - num))

print(result)