def spiral(m,n,a):                         # m - row, n - column and a- matrix to print
    k=0                                    # k = index of starting row
    l=0                                    # l = index of starting column 
    while(k<m and l<n):
        for i in range(l,n):              #print first row (k) from the remaining rows, varying the columns l to n
            print(a[k][i], end=" ")
        k+=1                              # kth row printed. point k to next row
        for i in range(k,m):              #print last column (n-1) from the remaining columns, varying the row k to m
            print(a[i][n-1],end=" ")
        n-=1                               # nth column printed. reduce the matrix column n by one
        if(k<m):                           # is row exhausted?
             for i in range(n-1,l-1, -1):  #printing the last row from remaining rows
                print(a[m-1][i],end=" ")
        m-=1                              # reduce the matrix row m by one
        if(l<n):                          # is column exhausted?
            for i in range(m-1,k-1,-1):    #printing the first column from the remaining columns   
                print(a[i][l],end=" ")
        l+=1
a=[]
r,c = input().split()
count=1
r = int(r)
c = int(c)
for i in range(r):
    l=[]
    for j in range(c):
        l.append(count)
        count+=1
    a.append(l)

spiral(r,c,a)