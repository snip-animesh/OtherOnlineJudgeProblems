def isvalid(lst,n,N,C):
    j=0;cnt=1
    for i in range(1,N):
        if lst[i]-lst[j]>=n:
            cnt+=1;j=i
        if cnt==C:
            return True
    return False


def getans(lst,N,C):
    l=0;h=lst[N-1]-lst[0];ans=0
    while l<=h:
        mid=(l+h)//2
        if isvalid(lst,mid,N,C):
            l=mid+1
            ans=mid
        else:
            h=mid-1
    return ans


for _ in range(int(input())):
    N,C=map(int,input().split())
    lst=[]
    for i in range(N):
        lst.append(int(input()))
    lst.sort()
    print(getans(lst,N,C))
    
    
# Logic from https://www.youtube.com/watch?v=fjcpZbEDslE&list=PL2q4fbVm1Ik5HC7D3gUwc8cqwDtvOaqke&index=5
