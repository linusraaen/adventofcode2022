sum=1
count=0
check=[20,60,100,140,180,220]
full_sum=0
sum_list=[]
 
with open("10.txt") as f:
    for line in f:
        line=line.strip()
        if(line[:4])=='addx':
            count+=1
            if check.count(count)!=0:
                full_sum+=sum*count
                sum_list.append(sum*count)
            count+=1
            if check.count(count)!=0:
                full_sum+=sum*count
                sum_list.append(sum*count)
            sum+=int(line[5:])
        else: 
            count+=1
            if check.count(count)!=0:
                full_sum+=sum*count
                sum_list.append(sum*count)
    print(full_sum)
    print(sum_list)