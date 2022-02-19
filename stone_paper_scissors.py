import random

query=str(input("Click yes below if you want to learn the rules of this game.\n"))

if query == "yes":
    Rule1=input("Rule1: This game consists stone, paper, scissors. Type Yes if got it:   ")
    Rule2=input("Rule2: If computer chooses stone and you chose paper,you won .Type yes if got it :  ")
    Rule3=input("Rule3: If computer chooses scissors and you chose stone ,computer won.Type yes if got it:  ")
    

print("Comp's turn: Computer is choosing.... ")
comp=random.randint(1,3)
if comp==1:
    comp="scissors"
elif comp==2:
    comp="stone"
elif comp==3:
    comp=="paper"

you=input(" Your turn: Scissors  or Paper or Stone?\n")

def gameWin(comp,you):
    #all possibilities for the game to tie
    if comp =="stone" and you =="stone":
        print("This is a tie")
        print( "Computer chose: ",comp)
        print("You chose: ", you )
    elif comp=="paper" and you=="paper":
        print("This game is a tie! ")
        print( "Computer chose: ",comp)
        print("You chose: ", you )
    elif comp=="scissors" and you=="scissors":
        print("This game is a tie! ")
        print( "Computer chose: ",comp)
        print("You chose: ", you )


    #all possibilities for the comp to win
    if comp=="scissors" and you=="paper":
        print("Computer Won! ")
        print( "Computer chose: ",comp)
        print("You chose: ", you )
    
    
    elif comp=="stone" and you=="scissors":
        print("Computer Won! ")
        print( "Computer chose: ",comp)
        print("You chose: ", you )
    
    elif comp=="paper" and you=="stone":
        print("Comp Won!")
        print( "Computer chose: ",comp)
        print("You chose: ", you )
  

    #all possibilities for the user to win
    if you =="scissors" and comp=="paper":
        print("Congrats! YOU Won! ")
        print( "Computer chose: ",comp)
        print("You chose: ", you )

    
    
    elif you=="paper" and comp=="stone":
        print("Congrats! You Won!")


        print( "Computer chose: ",comp)
        print("You chose: ", you )
    
    elif you=="stone" and comp=="scissors":
        print("Congrats! You won!")
        print( "Computer chose: ",comp)
        print("You chose: ", you )
   


gameWin(comp,you)
