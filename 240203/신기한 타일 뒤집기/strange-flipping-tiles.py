OFFSET = 1000 * 10
arr = [0] * (OFFSET * 2 + 1)

segments = []
cur = 0

n = int(input())
for _ in range(n):
    x, direction = input().split()
    x = int(x)

    if direction == 'R':
        start = cur
        end = cur + x - 1
        cur = end
        marked = 'B'
    else:
        start = cur - x + 1
        end = cur
        cur = start
        marked = 'W'
    segments.append((start + OFFSET, end + OFFSET, marked))

for x1, x2, y in segments:
    for i in range(x1, x2 + 1):
        arr[i] = y

white_cnt = arr.count("W")
black_cnt = arr.count("B")
print(white_cnt, black_cnt)