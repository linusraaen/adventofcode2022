sum=0
check=[]
with open("6.txt") as f:
    text=f.read()
    for i in text:
        sum+=1
        check.append(i)
        if len(check)==14:
            if len(check)==len(set(check)):
                print(sum)
            else:
                check.pop(0)