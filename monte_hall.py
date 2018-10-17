import random
doors=[0]*3
gotdoors=[0]*2
swap=0
not_swap=0

x=random.randint(0,2)
doors[x]="BMW"

for i in range(0,3):
    if(i==x):
        continue
    else:
        doors[i]="Got"
        gotdoors.append(i)
choice=int(input("Please Enter Your Choice: "))
door_open=random.choice(gotdoors)
while(door_open==choice):
    door_open=random.choice(gotdoors)
ch=input("Do you want to swap? (Y/N): ")
if(ch=='y'):
    if(doors[choice]=='BMW'):
        print("Player Wins")
        swap=swap+1
    else:
        print("Player Lost")
else:
    if(doors[choice]=='Got'):
        print("Player lost")
    else:
        print("Player wins")
        not_swap=not_swap+1
print("swap",swap)
print("not_swap",not_swap)        