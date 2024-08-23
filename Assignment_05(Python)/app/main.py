from random import randint



def game() -> None:

    round = 1
    point = 0
    print("Welcome to the High-Low Game!")
    print("--------------------------------")


    while round <= 5:
        computer_num: int = randint(1,100)
        human_num: int = randint(1,100)
        
        
        print("Round",round)
        print("The Computer Number is:",computer_num)
        print("your number is :",human_num)
        
        value = input("Do you think your number is higher or lower than the computer's?:")
        
        
        if value == "higher":
            if human_num > computer_num:
                print(f"You were right! The computer's number was {computer_num}")
                point += 1
                
            if  human_num < computer_num :
                print(f"Aww, that's incorrect. The computer's number was {computer_num}")
                
        if value == "lower":
            if human_num < computer_num :
                print(f"You were right! The computer's number was {computer_num}")
                point += 1
                
            if human_num > computer_num:
                print(f"Aww, that's incorrect. The computer's number was {computer_num}")
        
        if value != "higher" and value != "lower":
            print("Please enter a valid value")
        else:
            round += 1
            print("Your score is now",point)    
        print("\n")
    


    if point == 5:
        print("Your score is now",point)
        print(f"Wow! You played perfectly!")
    if point >= 3: 
        print("Your score is now",point)
        print("You are a genius!")
    if point == 2:
        print("Your score is now",point)
        print("You are a decent player")
    if point <= 1:
        print("Your score is now",point)
        print("Better luck next time!")
        

            

                
        
        

    print("Thanks for playing game")


if __name__ == "__main__":
    game()
