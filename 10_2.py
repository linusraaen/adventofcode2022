sum=1
count=0
indexer=0
canvas=[[],[],[],[],[],[],]
 
with open("10.txt") as f:
    for line in f:
        line=line.strip()
        if count>40:
            count-=40
            indexer+=1   
        if(line[:4])=='addx':
            if sum==count or sum+1==count or sum-1==count:
                canvas[indexer].append('#')
            else:
                canvas[indexer].append('.')
            count+=1
            if count>40:
                count-=40
                indexer+=1   
            if sum==count or sum+1==count or sum-1==count:
                canvas[indexer].append('#')
            else:
                canvas[indexer].append('.')
            count+=1
            sum+=int(line[5:])
        else: 
            if sum==count or sum+1==count or sum-1==count:
                canvas[indexer].append('#')
            else:
                canvas[indexer].append('.')
            count+=1
    text=''.join(canvas.pop(0))
    print(text)
    for i in canvas:
        text=''.join(i)
        print('#'+text)
  