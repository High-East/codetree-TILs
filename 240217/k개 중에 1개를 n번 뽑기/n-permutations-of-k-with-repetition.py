k, n = map(int, input().split())
arr = []

def choose(num):
    if len(arr) == num:
        print(*arr)
        return

    for i in range(1, k + 1):
        arr.append(i)
        choose(num)
        arr.pop()

choose(n)