fp=open('Traveller_output.txt','w')
t=int(input())
ans=[]
for _ in range(t):
    n=int(input())
    inp=[]
    for i in range(2):
        s=input()
        inp.append(list(s))
    # input=[['Y','N','N','Y','Y'],['Y','Y','Y','N','Y']]
    dp=[['N' for i in range(n)] for j in range(n)]
    # print(dp)
    for i in range(n):
        dp[i][i]='Y'
        for j in range(i-1,-1,-1):
            if inp[1][j+1]=='Y' and inp[0][j]=='Y':
                dp[i][j]='Y'
            else:
                break
        for j in range(i+1,n):
            if inp[1][j-1]=='Y' and inp[0][j]=='Y':
                dp[i][j]='Y'
            else:
                break

    ans.append(dp)
# print(ans[0])
for j in range(t):
    n=len(ans[j])
    print(f'Case #{j+1}:')
    fp.write(f'Case #{str(j+1)}:')
    fp.write('\n')
    for i in range(n):
        print(''.join(ans[j][i]))
        fp.write(''.join(ans[j][i]))
        fp.write('\n')
