INF = 10**9
n = int(input("Enter number of vertices: "))
print("Enter adjacency matrix (use 999 or -1 for INF):")
dist = []
for _ in range(n):
    row = list(map(int, input().split()))
    for j in range(n):
        if row[j] == 999 or row[j] == -1:
            row[j] = INF
    dist.append(row)
for k in range(n):
    for i in range(n):
        for j in range(n):
            if dist[i][k] + dist[k][j] < dist[i][j]:
                dist[i][j] = dist[i][k] + dist[k][j]
print("\nShortest distance matrix:")
for i in range(n):
    for j in range(n):
        if dist[i][j] >= INF//2:
            print("INF", end=" ")
        else:
            print(dist[i][j], end=" ")
    print()
