n = int(input("Enter number of rows "))
a = []
for i in range(n+1):
    a.append([input() for j in range(n+1)])

stages = 4
minimum = float("inf")
cost = [0 for i in range(n+1)]
distance = [0 for i in range(n+1)]
path = [0 for i in range(n+1)]
print(a,cost,distance,path)

cost[n] = 0

for i in range(n-1,-1,-1):
    minimum = float("inf")
    for k in range(i+1,n+1):
        if(a[i][k]!=0 and a[i][k]+cost[k] < minimum):
            minimum = a[i][k]+cost[k]
            distace[i] = k
    cost[i] = minimum
