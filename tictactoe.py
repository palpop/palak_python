import os
import time
matrix=[['_','_','_'],['_','_','_'],['_','_','_']]
p1symbol='X'
p2symbol='O'
def print_on_screen(matrix):
    for each in matrix:
        row="   ".join(each)
        row=row.strip()
        row=row+"\n"
        print(row)
def write_symbol(row,col,symbol):
    
    if(row<0 or row>2 or col<0 or col>2):
        print("NOT ON THE MATRIX!!")
        return False
    elif(matrix[row][col]!='_'):
        print('already MARKED !!, try another location')
        return False
    else:
        matrix[row][col]=symbol
        return True
    
def check_for_win(symbol):
    if(matrix[0][0]==symbol and matrix[0][1]==symbol and matrix[0][1]==symbol ):
        return True
    elif(matrix[1][0]==symbol and matrix[1][1]==symbol and matrix[1][1]==symbol ):
        return True
    elif(matrix[2][0]==symbol and matrix[2][1]==symbol and matrix[2][1]==symbol ):
        return True
    elif(matrix[0][0]==symbol and matrix[1][0]==symbol and matrix[2][0]==symbol ):
        return True
    elif(matrix[0][1]==symbol and matrix[1][2]==symbol and matrix[2][3]==symbol ):
        return True
    elif(matrix[0][0]==symbol and matrix[1][1]==symbol and matrix[2][2]==symbol ):
        return True
    elif(matrix[0][0]==symbol and matrix[1][1]==symbol and matrix[2][2]==symbol ):
        return True
    elif(matrix[0][2]==symbol and matrix[1][1]==symbol and matrix[2][0]==symbol ):
        return True
    return False
def check_for_draw():
    for each in matrix:
        for each_elem in each:
            if(each_elem=='_'):
                return False
    return True
win=1
draw=1
print_on_screen(matrix)
while(win and draw):
    print("PLAYER 1")
    row=int(input("Enter row: "))
    col=int(input("Enter col: "))
    
    
    if(write_symbol(row,col,p1symbol)):
        if(check_for_win(p1symbol)):
            print("PLAYER1 wins!!")
            win=0
        elif(check_for_draw()):
            print("--DRAW--")
            draw=0
        else:
            f=1
            os.system('cls')
            print_on_screen(matrix)
            while(f and win and draw):
            
                print("PLAYER 2")
                row=int(input("Enter row: "))
                col=int(input("Enter col: "))
                if(write_symbol(row,col,p2symbol)):
                    if(check_for_win(p2symbol)):
                        print("PLAYER2 wins!!")
                        win=0
                    elif(check_for_draw()):
                        print("--DRAW--")
                        draw=0
                    f=0
                else:
                    f=1

    print_on_screen(matrix)
print("Bye!")
time.sleep(2)