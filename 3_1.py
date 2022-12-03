sum=0
liste=[]
bokstav="0abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
with open("3.txt") as f:
    for line in f:
        line=line[:-1]
        første = line[:int(len(line)/2)]
        andre = line[int(len(line)/2):]
        print(første, andre)
        for i in første:
            if andre.find(i)!=-1:
                liste.append(i)
                break
    for i in liste:
        sum+=bokstav.index(i)
    print(sum)

        