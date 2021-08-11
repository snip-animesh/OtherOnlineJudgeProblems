t=int(input())
while t:
    n=int(input())
    s=[int(x) for x in input().split()]
    P=int(input())
    tot=1<<n
    for N in range(1,tot):
        sum=0
        for j in range(n):
            f=1<<j
            if N & f:
                sum+=s[j]
        if sum==P:
            print("YES")
            break
    else:
        print("NO")

    t-=1
    
#   I have used the cocept of subset sum . Logic from CodeNCode L-05 . 
# https://www.hackerearth.com/practice/basic-programming/bit-manipulation/basics-of-bit-manipulation/practice-problems/algorithm/sum-of-numbers-9/
