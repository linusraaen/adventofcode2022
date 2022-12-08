sum=0
count=0
check=[[]]
 
with open("7.txt") as f:
    for line in f:
        line=line.strip()
        if(line[:4])=='$ cd':
            if(line[5:])!='..':
                check.append(list(str(line[5:])))
            else:
                count+=1
        if(line[0]).isdigit():
            temp=[]
            for i in line:
                if i.isdigit():
                    temp.append(i)
            check[count]=check[count]+temp
    print(check)