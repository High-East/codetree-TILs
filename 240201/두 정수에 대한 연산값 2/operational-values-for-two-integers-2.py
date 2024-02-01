a, b = map(int, input().split())

def cal(a, b):
    return min([a, b]) + 10, max([a, b]) * 2

print(*cal(a, b), sep=' ')