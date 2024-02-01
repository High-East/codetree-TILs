import math

n, m = map(int, input().split())

print(abs(n * m) // math.gcd(n, m))