# 1stproject
Python program to play tic-tac-toe using minimax algo and using random function of python.
Mukul Lakra
200101069
------------------------------------------------------------------------------------------------------------------------------------
Command to run the python program:

python3 200101069_Assign04.py
------------------------------------------------------------------------------------------------------------------------------------
Explanation:

Then the program will run and as soon as it will run , it will firstly ask you that which difficulty level you want to play.
Press 1 for hard difficulty and 0 for easy difficulty.
Then it will ask you that which symbol you want to take for that tic-tac-toe game.
Press 1 for 'X' and 0 for 'O'
Then it will ask you whether you want to go first or not.
Press 1 if you want to go first and 0 if you want to go second.
Then it will run computer's move and ask you to place your move by entering a integer between 1 and 9 based on the ordering printed
at the beginning of the output.
In easy level , computer's move is made by generating a random integer between 1 and 9 and playing that move if that box is empty
or else generate any other number.
In hard level , computer only makes the optimal or best possible move and it is implemented using minimax algorithm.
The board is printed after every move so that user can see that which place is empty.
Finally computer decides that who has won or whether its a draw.
As the game gets over , the program asks you whether you want to play another game or not.
Press 1 if you want to play another game , 0 otherwise.
And then it will again ask you about the difficulty level and so on.
-----------------------------------------------------------------------------------------------------------------------------------
Warning:
When it will ask you to choose difficulty or symbol or whether you want to go first or whether you want to play again , just enter
an integer because if you enter a string and as I have used int(input()) and as string is not convertible to integer , an error
will be raised and the program will terminate unexpectedly.
-----------------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------------
