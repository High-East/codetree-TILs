n = int(input())
arr = [input().split() for _ in range(n)]
arr.sort()
for date, week, weather in arr:
    if weather == 'Rain':
        print(date, week, weather, sep=' ')
        break