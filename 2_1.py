sum=0
muligheter=["niks","A","B","C"]
muligheter2=["nada","X","Y","Z"]
with open("2.txt") as f:
    for line in f:
        mitt_resultat=muligheter2.index(line[2])
        resultat=mitt_resultat-muligheter.index(line[0])
        if resultat==0:
            sum+=mitt_resultat+3
        elif resultat==1 or resultat==-2:
            sum+=mitt_resultat+6
        elif resultat==-1 or resultat==2:
            sum+=mitt_resultat
print(sum)