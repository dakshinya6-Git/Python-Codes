INF = 9999

def multistage(cost, n):
    d = [0]*n
    d[n-1] = 0

    for i in range(n-2, -1, -1):
        m = INF
        for j in range(i+1, n):
            if cost[i][j] != INF and cost[i][j] + d[j] < m:
                m = cost[i][j] + d[j]
        d[i] = m

    return d[0]


n = int(input("Enter number of vertices: "))

print("Enter cost matrix (9999 for no edge):")
cost = []
for i in range(n):
    row = list(map(int, input().split()))
    cost.append(row)

ans = multistage(cost, n)

print("Minimum cost from source to destination:", ans)
