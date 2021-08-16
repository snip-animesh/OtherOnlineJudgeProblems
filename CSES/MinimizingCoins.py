# https://cses.fi/problemset/task/1634/
n,sum=map(int,input().split())
coins=sorted([int(x) for x in input().split()])

inf=100000000
dp=[0]+[inf]*sum
for i in range(1,sum+1):
    for j in range(n):
        if (i-coins[j])>=0:
            dp[i]=min(dp[i],dp[i-coins[j]]+1)
        else:
            break
if dp[sum] !=inf:
    print(dp[sum])
else:
    print(-1)
    
# Logic from CodeNCode 
