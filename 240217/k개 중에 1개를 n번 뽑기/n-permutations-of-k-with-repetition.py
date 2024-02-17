k, n = map(int, input().split())

def choose(arr=[]):
    if len(arr) == n:
        print(*arr)
        return
    for i in range(1, k + 1):
        arr.append(i)
        choose(arr)
        arr.pop()

choose()