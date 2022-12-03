sum=0
muligheter=["A","B","C"]
with open("2.txt") as f:
    for line in f:
        if line[2]== "X":
            sum+=((muligheter.index(line[0])+2) % 3)+1
        elif line[2]=="Y":
             sum+=muligheter.index(line[0])+4
        elif line[2]=="Z":
            sum+=((muligheter.index(line[0])+1) % 3)+7
        
print(sum)