for _ in range(int(input())):
    N=int(input());F=[0]*32
    for i in range(N):
        mask=0
        s=input()
        for j in s:
            if j=='a':
                mask = mask | 1<<0 #1<<0 means a digit who's 0th bit is only 1
            elif j=='e':
                mask = mask | 1<<1 #1<<0 means a digit who's 2nd bit is only 1
            elif j=='i':
                mask = mask | 1 << 2
            elif j=='o':
                mask = mask | 1 << 3
            else :
                mask = mask | 1 << 4
        F[mask]+=1
    res=0
    for i in range(1, 32):
        if F[i]>0:
            for j in range(i+1,32):
                if (i|j) == 31 and F[j]>0:
                    res=res+(F[i]*F[j])
    res=res+((F[31]*(F[31]-1))//2)
    print(res)
    
#  Logic from Code N Code L06 , DP-1 playlist.
