n, t = map(int, input().split())
arr = list(map(int, input().split()))

result = 0
cnt = 0
for x in arr:
    if x <= t:
        result = max(result, cnt)
        cnt = 0
        continue
    cnt += 1
print(result)