arr = list(map(int, input().split()))
result = 5000

for i in range(5):
    for j in range(5):
        if j == i:
            continue
        for k in range(5):
            if (k == i) or (k == j):
                continue
            team_1 = arr[i]
            team_2 = arr[j] + arr[k]
            team_3 = sum(arr) - (team_1 + team_2)
            if (team_1 == team_2) or (team_1 == team_3) or (team_2 == team_3):
                continue
            diff = max([team_1, team_2, team_3]) - min([team_1, team_2, team_3])
            result = min(result, diff)
if result == 5000:
    result = -1
print(result)