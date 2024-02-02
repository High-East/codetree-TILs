n = int(input())
arr = [tuple(map(int, input().split())) + (i,) for i in range(1, n + 1)]  # (키, 몸무게, 번호)

arr.sort(key=lambda x: (x[0], -x[1]))
for x in arr:
    print(*x)