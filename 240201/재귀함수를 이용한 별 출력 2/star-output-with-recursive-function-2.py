N = int(input())

def draw_star(n, mode='descend'):
    print(" ".join(['*'] * n))
    if mode == 'descend':
        if n == N:
            return draw_star(n, "ascend")
        return draw_star(n - 1, mode)
    else:
        if n == N:
            return
        return draw_star(n + 1, mode)

draw_star(N)