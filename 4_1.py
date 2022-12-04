import re
sum=0
with open("4.txt") as f:
    for line in f:
        line=line.strip()
        line=(re.split(r'[-,]',line))
        line=[int(x) for x in line]
        if ((line[1]>=line[3]) and (line[0]<=line[2])) or ((line[1]<=line[3]) and (line[0]>=line[2])):
            sum+=1
    print(sum) 