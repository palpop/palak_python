p1=input("Enter the Name of 1 person:")
p1.lower()
p1.replace(" ","")

p2=input("Enter the Name of 2 Person:")
p2.lower()
p2.replace(" ","")

l1=list(p1)
l2=list(p2)

proceed=True
while proceed:
    for i in l1:
        if i in l2:
            temp=i
            l1.remove(temp)
            l2.remove(temp)
            proceed=True
            break
        else:
            proceed=False
count=len(l1)+len(l2)
results=['Friends','Love','Affection','Marriage','Enemy','Siblings']

while len(results)>1:
    split_index=(count % len(results)) -1
    if split_index >= 0:
        right = results [split_index+1 : ]
        left = results [ : split_index ]
        results = right+left
    else:
        results = results [ : len(results)-1 ]
print(results[0])