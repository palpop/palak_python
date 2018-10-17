def checkNum(num):
    iteration=1
    
    while(num!=1):
        if(num%2==0):
            num=num/2
            iteration+=1
        else:
            num=(3*num)+1
            iteration+=1
    print("Number 1 has been occured after",iteration,"iterations.")

checkNum(256)