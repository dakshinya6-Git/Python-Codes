INF = 10**9

n = int(input("Enter number of vertices: "))

print("Enter adjacency matrix (use 9999 for no edge):")
cost = []
for _ in range(n):
    row = list(map(int, input().split()))
    for j in range(n):
        if row[j] == 9999:
            row[j] = INF
    cost.append(row)

src = int(input("Enter source vertex (0-based): "))

dist = [INF] * n
visited = [False] * n

# initialize
for i in range(n):
    dist[i] = cost[src][i]

dist[src] = 0
visited[src] = True

for _ in range(n - 1):

    # find minimum unvisited vertex
    min_dist = INF
    u = -1
    for i in range(n):
        if not visited[i] and dist[i] < min_dist:
            min_dist = dist[i]
            u = i

    if u == -1:
        break

    visited[u] = True

    # update neighbors
    for v in range(n):
        if not visited[v] and dist[u] + cost[u][v] < dist[v]:
            dist[v] = dist[u] + cost[u][v]

print("\nShortest distances from vertex", src, ":")
for i in range(n):
    if dist[i] >= INF:
        print(i, "-> INF")
    else:
        print(i, "->", dist[i])
