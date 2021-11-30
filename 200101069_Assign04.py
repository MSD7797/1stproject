#to generate a random integer between 1 and 9 to fill in that box as a computer move for the easy difficulty

import random

# sleep is used to give some time gap in showing output after our move and after computer move

from time import sleep

#board is a list whose entries from 1 to 9 store the contents of the tic-tac-toe

board=["TIC_TAC_TOE_GAME"," "," "," "," "," "," "," "," "," "]

print(board[0])

print("")

#printing position mappings of the tic-tac-toe box

print("Numbering of positions")

print("")

print(1,"|",2,"|",3,sep="")
print("-","+","-","+","-",sep="")
print(4,"|",5,"|",6,sep="")
print("-","+","-","+","-",sep="")
print(7,"|",8,"|",9,sep="")

print("")

#function to print the tic-tac-toe board after every move

def print_board():
    print("")
    print(board[1],"|",board[2],"|",board[3],sep="")
    print("-","+","-","+","-",sep="")
    print(board[4],"|",board[5],"|",board[6],sep="")
    print("-","+","-","+","-",sep="")
    print(board[7],"|",board[8],"|",board[9],sep="")
    print("")

#deciding the difficulty of the tic-tac-toe , whether easy or hard

difficulty=int(input("Enter 1 for hard difficulty and 0 for easy difficulty:"))

#checking whether valid difficulty is given as input or not

while(difficulty!=1 and difficulty!=0):
    difficulty=int(input("Invalid input. Please enter value again:"))

#deciding that which symbol is alloted to the user for the tic-tac-toe game

symbol=int(input("Enter 1 if you want to play with 'X' and 0 for 'O':"))

#deciding whether the symbol given is valid or not

while(symbol!=1 and symbol!=0):
    symbol=int(input("Invalid input. Please enter value again:"))

#creating two variables user and bot containing the symbol alloted to the user and computer respectively for the tic-tac-toe game
   
if(symbol==1):
    user="X"
    bot="O"
else:
    user="O"
    bot="X"
 
#asking from the user whether he wants to make the first move of the tic-tac-toe program or not
   
first_player_user=int(input("Do you want to go first in the game? Enter 1 for yes and 0 for no:"))

#checking the validity of the input from the user

while(first_player_user!=1 and first_player_user!=0):
    first_player_user=int(input("Invalid input. Please enter value again:"))

#this user_turn function is called whenever its the turn of the user
#it asks user the location where he wants to place his symbol in the next move in the tic-tac-toe box
#it also checks that the box number given is empty or not
# if it is not empty, then it asks for any other valid empty box

def user_turn():
    pos=int(input("Enter a number between 1 and 9 , refer to top to check the numbering:"))
    if(board[pos]==" "):
    	board[pos]=user
    	print_board()
    else:
        print("Invalid input.")
        user_turn()

#if first player is user , then asking him to make the first move.

if(first_player_user==1):
    user_turn()

#the win() function decides that whether any one of user or computer has won or not
#contains all possibility whenever any ony of them wins a game
#this functions return 1 if user has won , 2 if computer has won and 0 if none has won

def win():
    if(board[1]==user and board[2]==user and board[3]==user):
        return 1
    elif(board[4]==user and board[5]==user and board[6]==user):
        return 1
    elif(board[7]==user and board[8]==user and board[9]==user):
        return 1
    elif(board[1]==user and board[4]==user and board[7]==user):
        return 1
    elif(board[2]==user and board[5]==user and board[8]==user):
        return 1
    elif(board[3]==user and board[6]==user and board[9]==user):
        return 1
    elif(board[1]==user and board[5]==user and board[9]==user):
        return 1
    elif(board[3]==user and board[5]==user and board[7]==user):
        return 1
    elif(board[1]==bot and board[2]==bot and board[3]==bot):
        return 2
    elif(board[4]==bot and board[5]==bot and board[6]==bot):
        return 2
    elif(board[7]==bot and board[8]==bot and board[9]==bot):
        return 2
    elif(board[1]==bot and board[4]==bot and board[7]==bot):
        return 2
    elif(board[2]==bot and board[5]==bot and board[8]==bot):
        return 2
    elif(board[3]==bot and board[6]==bot and board[9]==bot):
        return 2
    elif(board[1]==bot and board[5]==bot and board[9]==bot):
        return 2
    elif(board[3]==bot and board[5]==bot and board[7]==bot):
        return 2
    else:
        return 0

#the draw() function decides whether the game has resulted in a draw or not
#it returns 1 if it is a draw , 0 otherwise

def draw():
    if((board[1]=="X" or board[2]=="X" or board[3]=="X")and(board[1]=="O" or board[2]=="O" or board[3]=="O")):
        if((board[4]=="X" or board[5]=="X" or board[6]=="X")and(board[4]=="O" or board[5]=="O" or board[6]=="O")):
            if((board[7]=="X" or board[8]=="X" or board[9]=="X")and(board[7]=="O" or board[8]=="O" or board[9]=="O")):
                if((board[1]=="X" or board[4]=="X" or board[7]=="X")and(board[1]=="O" or board[4]=="O" or board[7]=="O")):
                    if((board[2]=="X" or board[5]=="X" or board[8]=="X")and(board[2]=="O" or board[5]=="O" or board[8]=="O")):
                        if((board[3]=="X" or board[6]=="X" or board[9]=="X")and(board[3]=="O" or board[6]=="O" or board[9]=="O")):
                            if((board[1]=="X" or board[5]=="X" or board[9]=="X")and(board[1]=="O" or board[5]=="O" or board[9]=="O")):
                                if((board[3]=="X" or board[5]=="X" or board[7]=="X")and(board[3]=="O" or board[5]=="O" or board[7]=="O")):
                                    return 1
                                else:
                                    return 0
                            else:
                                return 0
                        else:
                            return 0
                    else:
                        return 0
                else:
                    return 0
            else:
                return 0
        else:
            return 0
    else:
        return 0

#the game_proceeding_easy() function decides how the game will proceed if easy difficulty is chosen
#in this function , computer makes a move first by generating a random number until its a valid move
#and then user makes a move and so on until the game has resulted in a draw or anyone has won.
#prints the output of the game

def game_proceeding_easy():
    wins=win()
    draws=draw()
    i=0
    while((not wins) and (not draws)):
        if(i%2==0):
            index=random.randint(1,9)
            if(board[index]==" "):
                board[index]=bot
                i+=1
                print("Computer's Turn:")
                sleep(2)
                print_board()
        else:
            user_turn()
            i+=1
        wins=win()
        draws=draw()
    if(wins==1):
        print("YOU WON")
    if(wins==2):
        print("COMPUTER WON")
    if(draws==1):
        print("DRAW")     

#the minimax function implements the minimax algorithm for hard difficulty
#it takes two parametres as input
#it is a recursive algorithm
#it returns a maximum value when the computer has won and helps computer in making an optimal move

def minimax(depth,ismaximized):
    winss=win()
    drawss=draw()
    if(winss==1):
        return -100
    if(winss==2):
        return 100
    if(drawss==1):
        return 0
    if(ismaximized):
        best_score=-1000
        for index in range(1,10):
            if(board[index]==" "):
                board[index]=bot
                score=minimax(depth+1,False)
                board[index]=" "
                if(score>best_score):
                    best_score=score
        return best_score
    else:
        best_score=1000
        for index in range(1,10):
            if(board[index]==" "):
                board[index]=user
                score=minimax(depth+1,True)
                board[index]=" "
                if(score<best_score):
                    best_score=score
        return best_score

#the function game_proceeding_hard() contains how the game proceeds if hard difficulty is chosen
#in this function , computer makes a move first which is the optimal move and increase the chances of the computer winning
#and then user makes a move and so on until the game has resulted in a draw or anyone has won.
#theoritically , in the hard diffculty , you can at max. manage a draw but can't win
#because the computer doesn't let you do so
#prints the output of the game

def game_proceeding_hard():
    wins=win()
    draws=draw()
    i=0
    while((not wins) and (not draws)):
        if(i%2==0):
            best_score=-1000
            best_move=0
            for index in range(1,10):
                if(board[index]==" "):
                    board[index]=bot
                    score=minimax(0,False)
                    board[index]=" "
                    if(score>best_score):
                        best_score=score
                        best_move=index
            board[best_move]=bot
            i+=1
            print("Computer's Turn:")
            sleep(1)
            print_board()
        else:
            user_turn()
            i+=1
        wins=win()
        draws=draw()
    if(wins==1):
        print("YOU WON")
    if(wins==2):
        print("COMPUTER WON")
    if(draws==1):
        print("DRAW")
 
#deciding which function to call based on the difficulty chosen earlier on by the user
  
if(difficulty==0):
    game_proceeding_easy()
elif(difficulty==1):
    game_proceeding_hard() 

#asking whether the user wants to play another game or not

want_to_play_more=int(input("Enter 1 to play again and 0 if you want to exit:"))  

#checking for validity of the input

while(want_to_play_more!=1 and want_to_play_more!=0):
    want_to_play_more=int(input("Invalid input. Please enter value again:"))

#as functions to decide the win , draw and printing board are the same
#so this loop just takes input again of diffculty , symbol taken by user and whether he wants the first move or not
# and hence another game begins
#and at the end of the loop , it again asks whether you want to play another game or not
#it will continue until user denies to further play any game.
#The program ends when the user does not want to play any further game.

while(want_to_play_more==1):
    board=["TIC_TAC_TOE_GAME"," "," "," "," "," "," "," "," "," "]
    print(board[0])
    print("")
    print("Numbering of positions")
    print("")
    print(1,"|",2,"|",3,sep="")
    print("-","+","-","+","-",sep="")
    print(4,"|",5,"|",6,sep="")
    print("-","+","-","+","-",sep="")
    print(7,"|",8,"|",9,sep="")
    print("")    
    difficulty=int(input("Enter 1 for hard difficulty and 0 for easy difficulty:"))
    while(difficulty!=1 and difficulty!=0):
        difficulty=int(input("Invalid input. Please enter value again:"))
    symbol=int(input("Enter 1 if you want to play with 'X' and 0 for 'O':"))
    while(symbol!=1 and symbol!=0):
        symbol=int(input("Invalid input. Please enter value again:"))
    if(symbol==1):
        user="X"
        bot="O"
    else:
        user="O"
        bot="X"
    first_player_user=int(input("Do you want to go first in the game? Enter 1 for yes and 0 for no:"))
    while(first_player_user!=1 and first_player_user!=0):
        first_player_user=int(input("Invalid input. Please enter value again:"))
    if(first_player_user==1):
        user_turn()
    if(difficulty==0):
        game_proceeding_easy()
    elif(difficulty==1):
        game_proceeding_hard() 
    want_to_play_more=int(input("Enter 1 to play again and 0 if you want to exit:"))  
    while(want_to_play_more!=1 and want_to_play_more!=0):
        want_to_play_more=int(input("Invalid input. Please enter value again:"))

