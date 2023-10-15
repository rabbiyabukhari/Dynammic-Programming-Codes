x=int(input())
h=list(map(int,input().split()))
DP=[2**31-1]*x
DP[0]=0
for i in range(x):
    for j in range(i+1,i+3):
        if j<x:
            DP[j]=min(DP[j],DP[i]+abs(h[i]-h[j]))
print(DP[x-1])
