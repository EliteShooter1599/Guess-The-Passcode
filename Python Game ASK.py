# RNG (Random Number Generator)
import random

# Title and instructions.
print("")
print("  -- Guess the passcode -- ")
print("")
print("[ Instructions ]")
print("  ~ You will have to guess 3 seperate numbers correctly to win. ")
print("  ~ If you run out of tries, you will lose, so be careful! ")
print("  ~ Don't worry, it will tell you whether its bigger, smaller, or the correct number.")

# Elaboration :
# Guess the (first/second/third) number - [3 seperate lines]
# (First/Second/Third) number - (Too low/Too high/Correct)  [3 seperate lines]
# _ tries left.
# (if tries = 0, game lost)
# (if all numbers correct , game win)
# Continue? (type 1 if yes)

print("")
print("")


# 'While' gameloop - ( Repeats the game until user inputs 1 to stop the game. )
gameloop = 0
games = 0
while gameloop != 1 :
    games = games + 1
    # Numbers of games user has played.
    print(" -| Game [",games,"] |-")
    print("")
    # Difficulty choices.
    print("[ Selecting the difficulty ] ")
    print("  ~ Easy = Numbers are in range of (1 - 10).  5 tries. ")
    print("  ~ Medium = Numbers are in range of (1 - 100). 10 tries. ")
    print("  ~ Hard = Numbers are in range of (1 - 1000). 15 tries. ")
    print("")
    # Selecting difficulty .
    difficulty_check = 0
    while difficulty_check != 1 :
        difficulty = str(input("  || - What difficulty would you like? ( Easy, Medium, Hard ) - "))
        if difficulty == ("Easy") :
            tries = 5
            first_number = random.randint(1,10)
            second_number = random.randint(1,10)
            third_number = random.randint(1,10)
            difficulty_check = 1
            
        elif difficulty == ("Medium") :
            tries = 10
            first_number = random.randint(1,100)
            second_number = random.randint(1,100)
            third_number = random.randint(1,100)
            difficulty_check = 1
            
        elif difficulty == ("Hard") :
            tries = 15
            first_number = random.randint(1,1000)
            second_number = random.randint(1,1000)
            third_number = random.randint(1,1000)
            difficulty_check = 1
            
        else :
             print("    * Couldn't read that, so we'll try again. Do make sure you have the spellings correct.")
             print("")

    print("")
    print(" Difficulty selected - ",difficulty)
    print(" Good luck! ")
    print("")
    # Loop until tries = 0.
    while tries > 0 :
        first_guess = int(input(" Guess the first number - "))
        second_guess = int(input(" Guess the second number - "))
        third_guess = int(input(" Guess the third number - "))
                          
        # First number check.
        if first_guess == first_number :
            print(" - Nice! Your first guess is correct.")
        elif first_guess > first_number :
            print(" - Your first guess was too high. Try guessing lower.")
        elif first_guess < first_number :
            print(" - Your first guess was too low. Try guessing higher.")
            
        # Second number check.
        if second_guess == second_number :
            print(" - Nice! Your second guess is correct.")
        elif second_guess > second_number :
            print(" - Your second guess was too high. Try guessing lower.")
        elif second_guess < second_number :
            print(" - Your second guess was too low. Try guessing higher.")
            
        # Third number check.
        if third_guess == third_number :
            print(" - Nice! Your third guess is correct.")
        elif third_guess > third_number :
            print(" - Your third guess was too high. Try guessing lower.")
        elif third_guess < third_number :
            print(" - Your third guess was too low. Try guessing higher.")

        # Tries left.
        print("")
        if (first_guess == first_number) and (second_guess == second_number) and (third_guess == third_number) : 
            tries = 0
        else :
            tries = tries - 1
            print("You have",tries,"tries left.")
        print("")
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
        print("")
            
    # Game ended. Showing answers.
    print(" The game has ended! ")
    print("")
    print(" -| The answer was... |- ")
    print(" First number =",first_number)
    print(" Second number =",second_number)
    print(" Third number =",third_number)
    print("")
    
    # Checking win or lose
    if (first_guess == first_number) and (second_guess == second_number) and (third_guess == third_number) :
        print("Congratulations, you cracked the passcode and won the game!")
    else :
        print("You ran out of tries and lost the game!")
    print("")
    
    # Continue game? (1 stops the game loop, while anything else will continue it)
    gameloop = int(input("Would you like to continue the game? (Type '0' to continue, and '1' to stop.) - "))
    print("")
    
# Ending process
print("Thank you for your time!")
print("Ending game..")
    
