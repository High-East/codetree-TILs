N = int(input())

def draw_star(n, mode='descend'):
    print(" ".join(['*'] * n))
    if mode == 'descend':
        if n == 1:
            return draw_star(n, "ascend")
        return draw_star(n - 1, mode)
    else:
        if n == 5:
            return
        return draw_star(n + 1, mode)

draw_star(N)