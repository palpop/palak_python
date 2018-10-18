arr=[]
def counterClockspiral(m,n,arr):
    k=0
    l=0
    cnt=0
    total=m*n
    
    while(k<m and l<n):
        if (cnt==total):
            break
        for i in range(k,m):        #k=0 , m=3 i=0,1,2
            print(arr[i][l],end=" ")  #[0][0],[1][0],[2][0]
            cnt+=1
        l=l+1           #l=1
        
        if(cnt==total):
            break
        for i in range(l,n):        #l=1,n=3 i=1,2
            print(arr[m-1][i],end=" ")  #[2][1],[2][2]
            cnt+=1
        m-=1            #m=2
        
        if(cnt==total):
            break
        if(k<m):        #(0<2)
            for i in range(m-1,k-1,-1):  
                print(arr[i][n-1],end=" ")  
                cnt+=1
            n-=1        #n=2
        
        if(cnt==total):
            break
        if(l<n):        #(1<2)
            for i in range(n-1,l-1,-1): 
                print(arr[k][i],end=" ")
                cnt+=1
            k=k+1     #k=1
        
m=int(input())
n=m
for i in range(1,m+1):
    l1=list(map(int,input().split()))
    arr.append(l1)
counterClockspiral(m,m,arr)