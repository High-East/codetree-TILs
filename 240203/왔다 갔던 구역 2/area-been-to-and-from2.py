OFFSET = 1000
n = int(input())
arr = [0] * (OFFSET * 2 + 1)
segments = []
current = 0

for _ in range(n):
    x, direction = input().split()
    x = int(x)
    if direction == 'R':
        start = current
        end = current + x
        current = end
    else:
        start = current - x
        end = current
        current = start
    segments.append((start + OFFSET, end + OFFSET))

for start, end in segments:
    for i in range(start, end):
        arr[i]+= 1

count = 0
for x in arr:
    if x >= 2:
        count += 1
print(count)