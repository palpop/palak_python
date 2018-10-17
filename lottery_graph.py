import random
import matplotlib.pyplot as plt
account=0
x=[]
y=[]

for i in range(365):
    x.append(i+1)
    bet=random.randint(1,10)
    lucky_draw=random.randint(1,10)
    
    if (bet==lucky_draw):
        account=account+1000-100
    else:
        account=account-100
    y.append(account)
    
print("amount in your game account: ",account)
plt.plot(x,y)
plt.title("Lottery")
plt.xlabel("Days")
plt.ylabel("PROFIT or LOSS")
plt.show()