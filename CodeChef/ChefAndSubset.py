t=int(input())
while t:
    s=[int(x) for x in input().split()]
    tot=1<<4
    for N in range(1,tot):
        sum=0
        for j in range(4):
            f=1<<j
            if N & f:
                sum+=s[j]
        if sum==0:
            print("Yes")
            break
    else:
        print("No")

    t-=1

#Using the concept of Subset sum . L-05 from CodeNCode , DP Part-1
#https://www.codechef.com/problems/CHEFSETC
