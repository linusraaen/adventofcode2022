import re
sum=0

en=[]
to=[]
tre=[]
fire=[]
fem=[]
seks=[]
sju=[]
åtte=[]
ni=[]
stacks=[en,to,tre,fire,fem,seks,sju,åtte,ni]

with open("5.txt") as f:
    for line in f:
       
        if line[0]==' ' or line[0]=='[':
            for j in range(9):
                if line[j*4+1]!=' ':
                    if line[j*4+1].isdigit():
                        continue
                    stacks[j].append(line[j*4+1]) 
            continue    
        line=(re.split(r'[movefrt ]',line))
        line= list(filter(None, line))
        if line!=['\n']: 
            for i in range(int(line[0])):
                (stacks[int(line[2])-1]).insert(0,stacks[int(line[1])-1].pop(0))
            
            stacks[int(line[2])-1]=temp
    for i in stacks:
        print(i.pop(0))
        

        