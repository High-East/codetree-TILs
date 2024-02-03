def run(num):
    pos = [0]
    for _ in range(num):
        v, t = map(int, input().split())
        for _ in range(t):
            pos.append(pos[-1] + v)
    return pos


n, m = map(int, input().split())
pos_a = run(n)
pos_b = run(m)

diff = []
for i in range(1, len(pos_a)):
    if pos_a[i] > pos_b[i]:
        diff.append(1)
    elif pos_a[i] < pos_b[i]:
        diff.append(2)
    else:
        diff.append(3)

cnt = 0
for i in range(len(diff)):
    if i == 0 or diff[i - 1] != diff[i]:
        cnt += 1
print(cnt)