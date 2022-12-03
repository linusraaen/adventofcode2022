import re
sum=0
liste=[]
lineliste=[]
bokstav="0abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
with open("3.txt") as f:
    lines = f.readlines()
    
    for sub in lines:
        lineliste.append(re.sub('\n', '', sub))
    
    lines=list(zip(*[iter(lineliste)]*3))
   
    for i in lines:
        for j in i[0]:
            if i[1].find(j)!=-1:
                if i[2].find(j)!=-1:
                    liste.append(j)
                    break
    for i in liste:
        sum+=bokstav.index(i)
    print(sum)
