nisse=[]
sum=0
with open("1.txt") as f:
    for line in f:
        if line == '\n':
            nisse.append(sum)
            sum=0
        else:
            sum+=int (line[:-1])
        

nisse.sort()
print(nisse[-3]+nisse[-2]+nisse[-1])