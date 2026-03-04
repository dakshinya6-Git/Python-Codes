INF = 9999
def multistage(cost, n):
    d = [0]*n
    p = [0]*n

    d[n-1] = 0

    for i in range(n-2, -1, -1):
        m = INF
        for j in range(i+1, n):
            if cost[i][j] != INF and cost[i][j] + d[j] < m:
                m = cost[i][j] + d[j]
                p[i] = j
        d[i] = m

    print("Minimum cost:", d[0])

    print("Path:", end=" ")
    v = 0
    print(v+1, end=" ")
    while v != n-1:
        v = p[v]
        print("->", v+1, end=" ")
    print()


n = int(input("Enter number of vertices: "))

print("Enter cost matrix (9999 for no edge):")
cost = []
for i in range(n):
    row = list(map(int, input().split()))
    cost.append(row)
multistage(cost, n)
