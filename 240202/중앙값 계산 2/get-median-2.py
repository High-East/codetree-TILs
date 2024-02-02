n = int(input())
arr = list(map(int, input().split()))
x = []

for i in range(n):
    x.append(arr[i])
    if i % 2 == 0:
        x.sort()
        print(x[len(x) // 2], end=' ')