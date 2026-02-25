INF = 10**9

n = int(input("Enter number of cities: "))

print("Enter cost matrix (use 999 for no path):")
cost = []
for _ in range(n):
    row = list(map(int, input().split()))
    for j in range(n):
        if row[j] == 999:
            row[j] = INF
    cost.append(row)

dp = [[INF] * n for _ in range(1 << n)]
par = [[-1] * n for _ in range(1 << n)]  

dp[1][0] = 0  

for mask in range(1 << n):
    if not (mask & 1): 
        continue
    for u in range(n):
        if not (mask & (1 << u)):
            continue
        if dp[mask][u] >= INF:
            continue
        for v in range(n):
            if mask & (1 << v):
                continue
            if cost[u][v] >= INF:
                continue
            new_mask = mask | (1 << v)
            new_cost = dp[mask][u] + cost[u][v]
            if new_cost < dp[new_mask][v]:
                dp[new_mask][v] = new_cost
                par[new_mask][v] = u

final_mask = (1 << n) - 1
min_cost = INF
last = -1
for i in range(1, n):
    if dp[final_mask][i] < INF and cost[i][0] < INF:
        tour_cost = dp[final_mask][i] + cost[i][0]
        if tour_cost < min_cost:
            min_cost = tour_cost
            last = i

if last == -1:
    print("\ncannot complete a full tour.")
else:
    path_rev = [last]
    mask = final_mask
    cur = last
    while cur != 0:
        prev = par[mask][cur]
        mask ^= (1 << cur)
        cur = prev
        path_rev.append(cur)

    path = list(reversed(path_rev)) + [0]

    print("\nMinimum travelling cost:", min_cost)
    print("Best path:", " -> ".join(map(str, path)))
