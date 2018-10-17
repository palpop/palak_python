from PIL import Image
import random
end=100

print('''
  ____              _                          _   _              _     _           
 / ___| _ __   __ _| | _____    __ _ _ __   __| | | |    __ _  __| | __| | ___ _ __ 
 \___ \| '_ \ / _` | |/ / _ \  / _` | '_ \ / _` | | |   / _` |/ _` |/ _` |/ _ \ '__|
  ___) | | | | (_| |   <  __/ | (_| | | | | (_| | | |__| (_| | (_| | (_| |  __/ |   
 |____/|_| |_|\__,_|_|\_\___|  \__,_|_| |_|\__,_| |_____\__,_|\__,_|\__,_|\___|_|      
                                                                                                                                                                                     
 ''')

def show_board():
    img=Image.open('slb.jpg')
    img.show()

def check_ladder(points):
    if points==3:
        print('Ladder')
        return 20
    elif points==6:
        print('Ladder')
        return 14
    elif points==11:
        print('Ladder')
        return 28
    elif points==15:
        print('Ladder')
        return 34
    elif points==17:
        print('Ladder')
        return 74
    elif points==22:
        print('Ladder')
        return 37
    elif points==38:
        print('Ladder')
        return 59
    elif points==49:
        print('Ladder')
        return 67
    elif points==57:
        print('Ladder')
        return 76
    elif points==61:
        print('Ladder')
        return 78
    elif points==73:
        print('Ladder')
        return 86
    elif points==81:
        print('Ladder')
        return 98
    elif points==88:
        print('Ladder')
        return 91
    else:
        return points

def check_snake(points):
    if points==8:
        print('Snake')
        return 4
    elif points==18:
        print('Snake')
        return 1
    elif points==26:
        print('Snake')
        return 10
    elif points==39:
        print('Snake')
        return 5
    elif points==51:
        print('Snake')
        return 6
    elif points==54:
        print('Snake')
        return 36
    elif points==56:
        print('Snake')
        return 1
    elif points==60:
        print('Snake')
        return 23
    elif points==75:
        print('Snake')
        return 28
    elif points==83:
        print('Snake')
        return 45
    elif points==85:
        print('Snake')
        return 59
    elif points==90:
        print('Snake')
        return 48
    elif points==92:
        print('Snake')
        return 25
    elif points==97:
        print('Snake')
        return 87
    elif points==99:
        print('Snake')
        return 63
    else:
        return points

def reached_end(points):
    if points==end:
        return True
    else:
        return False


def play():
    #input player names
    p1Name=input("Player1 Name : ")
    p2Name=input("Players Name : ")
    #initial points of players
    p1=0
    p2=0
    turn=0
    while(1):
        if(turn%2==0):
            print(p1Name, " Your turn")
            c = input("Press Enter to Continue, 0 to exit : ")
            if(c=="0"):
                print(p1Name," Scored : ",p1)
                print(p2Name," Scored : ",p2)
                print("Quiting the game, bye")
                break
            #generate random number for dice
            dice = random.randint(1,6)
            print("Dice showed : ",dice)
            
            p1 = p1+dice
            p1 = check_snake(p1)
            p1 = check_ladder(p1)
            #after snake if, p1 becomes negative, make it 0,
            #as -ve is not available on board
            if(p1<0):
                p1=0
            
            if p1>end:
                p1=p1-dice  
            print(p1Name, " Your Score : ",p1)
            if(reached_end(p1)):
                print(p1Name, " won")
                break
        else:
            print(p2Name, " Your turn")
            c = input("Press Enter to Continue, 0 to exit : ")
            if(c=="0"):
                print(p1Name," Scored : ",p1)
                print(p2Name," Scored : ",p2)
                print("Quiting the game, bye")
                break
            #generate random number for dice
            dice = random.randint(1,6)
            print("Dice showed : ",dice)
            
            p2 = p2+dice
            p2 = check_snake(p2)
            p2 = check_ladder(p2) 
            #after snake if, p1 becomes negative, make it 0,
            #as -ve is not available on board
            if(p2<0):
                p2=0
            
            if p2>end:
                p2=p2-dice #same reason as mentioned above
            print(p2Name, " Your Score : ",p2)
            if(reached_end(p2)):
                print(p2Name, " won")
                break
        turn+=1
show_board()
play()