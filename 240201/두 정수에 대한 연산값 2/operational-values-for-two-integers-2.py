a, b = map(int, input().split())

def calculate(a, b):
    if a > b:
        return a * 2, b + 10
    return a + 10, b * 2

result = calculate(a, b)
print(*result, sep=' ')