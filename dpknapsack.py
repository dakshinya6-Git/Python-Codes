n = int(input("Enter number of items: "))

wt = list(map(int, input("Enter weights: ").split()))
val = list(map(int, input("Enter values: ").split()))

w = int(input("Enter capacity: "))

dp = [[0]*(w+1) for i in range(n+1)]

for i in range(1, n+1):
    for j in range(1, w+1):
        if wt[i-1] <= j:
            dp[i][j] = max(val[i-1] + dp[i-1][j-wt[i-1]], dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]

print("Maximum profit =", dp[n][w])

j = w
print("Selected items:")

for i in range(n, 0, -1):
    if dp[i][j] != dp[i-1][j]:
        print("Weight:", wt[i-1], "Value:", val[i-1])
        j = j - wt[i-1]
