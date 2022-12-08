sum=0
horizontal=[]
vertical=[]

def checking(lists):
    count=0
    check=-1
    seen=[]
    for i in lists:
        if len(i)==2:
            if int(i[0])>check:
                check=int(i[0])
            continue
        elif i==9:
            seen.append(i)
            break
        elif int(i)>check:
            check=int(i)
            seen.append(i)
    for i in seen:
        if len(i)==1:
            lists[lists.index(i)]=str(i)+'s'
            count+=1
    return count, lists


with open("8.txt") as f:
    for line in f:
        temp=[]
        line=line.strip()
        for i in line:
            temp.append(i)
        tall, temp=checking(temp)
        sum+=tall
        temp.reverse()
        tall, temp=checking(temp)
        sum+=tall
        horizontal.append(temp)
    vertical.append(list(zip(*horizontal)))
    for i in vertical[0]:
        lists=list(i)
        tall, temp=checking(lists)
        sum+=tall
        lists.reverse()
        tall, temp=checking(lists)
        sum+=tall
    print(sum)


