import random
account=0
for i in range(30):
    bet=random.randint(1,10)
    lucky_draw=random.randint(1,10)
    #print(bet)
    #print(lucky_draw)
    
    if(bet==lucky_draw):
        account=account+1000-100
    else:
        account=account-100
print("Amount in our game account after on month=",account)