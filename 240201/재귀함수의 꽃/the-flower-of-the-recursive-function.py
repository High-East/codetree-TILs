N = int(input())

def awesome_print(n):
    if n == 0:
        return
    print(n, end=' ')
    awesome_print(n - 1)
    print(n, end=' ')

awesome_print(N)