import string
dict={}
data=""
for i in range(len(string.ascii_letters)):
    dict[string.ascii_letters[i]]=string.ascii_letters[i-1]
print(dict)
file=open("op_file.txt","w")
with open("ip_file.txt") as f:
    while True:
        c=f.read(1)
        if not c:
            print("End of File")
            break
        if c in dict:
            data=dict[c]
        else:
            data=c
        file.write(data)
        print(data)
file.close()
f.close()