n, h, t = map(int, input().split())
arr = list(map(int, input().split()))

result = 100 * 200
for i in range(n - t + 1):
    cost = 0
    for j in range(i, i + t):
        cost += abs(arr[j] - h)
    result = min(result, cost)
print(result)