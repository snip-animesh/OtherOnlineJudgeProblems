# Input file should be saved and output file should be created at the same directory where the program file is created. I haved read the input from file. 

from collections import Counter
fp=open('Alchemy_output.txt','w')
fpi=open('alchemy_input.txt','r')
ans=[]
t=fpi.readline()
for i,line in enumerate(fpi):
    if i % 2 == 1:
        s=line
        d=Counter(s)
        if abs(d['A']-d['B'])==1:
            ans.append('Y')
        else:
            ans.append('N')
for i in range(int(t)):
    fp.write(f'Case #{i+1}: {ans[i]}\n')
fp.close()
