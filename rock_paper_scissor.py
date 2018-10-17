def rock_paper_scissors(num1,num2,bit1,bit2):
    p1=int(num1[bit1])%3
    p2=int(num2[bit2])%3
    if(player_one[p1]==player_two[p2]):
        print("Draw")
    elif(player_one[p1]=='rock' and player_two[p2]=='paper'):
        print("player two wins")
    elif(player_one[p1]=='rock' and player_two[p2]=='scissor'):
        print("player one wins")
    elif(player_one[p1]=='paper' and player_two[p2]=='rock'):
        print("player one wins")
    elif(player_one[p1]=='paper' and player_two[p2]=='scissor'):
        print("player two wins")
    elif(player_one[p1]=='scissor' and player_two[p2]=='paper'):
        print("player one wins")
    elif(player_one[p1]=='scissor' and player_two[p2]=='rock'):
        print("player two wins")
player_one={0:'rock', 1:'paper',2:'scissors'}
player_two={0:'scissors', 1:'rock',2:'paper'}
while(1):
    num1=input("Player one, please enter the number: ")
    num2=input("Player two, please enter the number: ")
    bit1=int(input("Player one, please enter the bit: "))
    bit2=int(input("Player two, please enter the bit: "))
    rock_paper_scissors(num1,num2,bit1,bit2)
    ch=input("Do you want to play again? (Y/N): ")
    if ch=='n':
       break