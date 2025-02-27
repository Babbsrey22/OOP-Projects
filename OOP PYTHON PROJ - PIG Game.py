# Eunice Q. Reyes
# BSCPE 1-2

# Changes: Main Menu selection, Computer-generated rolls, Added dialogue.
# Main menu: 1vBot, Multiplayer, How to, Credits, Exit.

import random
import time

def menu():
    print("\nWelcome to the classic game of PIG!\n")
    print("[1] How to play?")
    print("[2] 1vBOT")
    print("[3] Multiplayer")
    print("[4] Credits")
    print("[5] Exit")

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll

# INSTRUCTIONS
def option_1():
    while True:
        print("\nInstructions:")
        print("\nYou are given a choice to roll the dice. If you roll a '1', your turn is forfeited and the other player gets a turn.")
        print("If not, you are free to roll how many times you want, and you may HOLD your turn to save your score.")
        print("The first player to accumulate a total of more than 50 POINTS wins the game!")
        time.sleep(5) # dialogue delay
        print("\nYARR HARR HARR HARRR")
        time.sleep(1.5)
        print("\nOne day the PIGs will rule the world... one DICE ROLL at a time.")
        time.sleep(2)
        
        repeat = input("\nReturn to main menu?\nChoice is yours (y/n): ")
        if repeat.lower() == 'n':
            continue
        elif repeat.lower() == 'y':
            break
            
# 1VBOT (Computer-generated rolls)       
def option_2():
    max_score = 50
    player_score = 0
    computer_score = 0
    
    def computer_turn():
        nonlocal computer_score
        current2_score = 0
        print("\nComputer is thinking...")

        while current2_score < 15:  # rolls until 1 or 15 points
            time.sleep(1)
            value = roll()
            print("Computer rolls a", value)

            if value == 1:
                print("TURN FORFEITED... Back to you!")
                return  # turn ends with no added points

            current2_score += value
            print(f"Computer's current score is: {current2_score}")

        print("Computer decides to HOLD")
        computer_score += current2_score 
        print(f"\n\t\t\tCOMPUTER'S TOTAL SCORE: {computer_score}")

    def player_turn():
        nonlocal player_score
        current1_score = 0
        print("\nYour turn has started!")

        while True:
            should_roll = input("Would you like to roll (y/n)? ")
            if should_roll.lower() != "y":
                print("You decided to HOLD")

                player_score += current1_score  
                print(f"\n\t\t\tYOUR TOTAL SCORE: {player_score}")
                return 

            value = roll()
            print("You rolled a", value)

            if value == 1:
                print("TURN FORFEITED... Back to Computer!")
                return  # turn ends with no added points

            current1_score += value
            print(f"Your current score is: {current1_score}")

    # Main game loop
    while max(player_score, computer_score) < max_score:
        player_turn()
        if player_score >= max_score:
            print(f"\nYOU WIN WITH {player_score} POINTS!! CONGRATULATIONS YIPPEEEE!!")
            time.sleep(1.5)
            print("A win a day keeps the PIGs away")
            time.sleep(3)
        
            repeat = input("\nReturn to main menu?\nChoice is yours (y/n): ")
            if repeat.lower() == 'n':
                continue
            elif repeat.lower() == 'y':
                break

        computer_turn()
        if computer_score >= max_score:
            print(f"\nCOMPUTER WINS WITH {computer_score} POINTS!! Awwww... Try again next time :(")
            time.sleep(1.5)
            print("They're coming...")
            time.sleep(3)

            repeat = input("\nReturn to main menu?\nChoice is yours (y/n): ")
            if repeat.lower() == 'n':
                continue
            elif repeat.lower() == 'y':
                break


# MULTIPLAYER
def option_3():
    while True:
        players = input("Enter the number of players (2-4): ") # limits multiplayer to 4 people
        if players.isdigit():
            players = int(players)
            if 2 <= players <= 4:
                break
            else:
                print("Must be between 2-4 players")
        else:
            print("Invalid input. Numbers only!")

    max_score = 50
    players_score = [0 for _ in range(players)]
    
    while max(players_score) < max_score:
        for player_idx in range(players):
            print("\nPlayer", player_idx + 1, "'s turn has just started!\n")
            current2_score = 0

            while True:
                should_roll = input("Would you like to roll (y/n)? ")
                if should_roll.lower() != "y":
                    print(f"\nPlayer {player_idx + 1} has decided to HOLD\n")
                    break
                        
                value = roll()
                if value == 1:
                    print(f"Player {player_idx + 1} rolled a 1! TURN FORFEITED...")
                    current2_score = 0
                    break
                else:
                    current2_score += value
                    print("You rolled a", value)
                        
                print("Your current score is:", current2_score)

            players_score[player_idx] += current2_score
            print(f"\n\t\t\tTOTAL SCORE FOR PLAYER {player_idx + 1}: ", players_score[player_idx])
            
            if players_score[player_idx] >= 50:
                print(f"\n\t\t\tPLAYER {player_idx+1} WINS WITH {players_score[player_idx]} POINTS!! CONGRATULATIONS RAAAHHHHHHH!!!!")
                
                repeat = input("\nReturn to main menu?\nChoice is yours (y/n): ")
                if repeat.lower() == 'n':
                    option_3()
                elif repeat.lower() == 'y':
                    break

def creds():
    time.sleep(2)
    print("\tDeveloper: Eunice Q. Reyes")
    print("\tCreated on 25 February, 2025")
    print("\tReleased on 26 February, 2025")
    print("\tIdea by: Tech with Tim (Youtube)")
    time.sleep(5)

def exit_sequence():
    time.sleep(1)
    print("Awwww....")
    time.sleep(1)
    print("I guess this is goodbye then....")
    time.sleep(1.5)
    print("So long and goodnight....")
    time.sleep(3)
    print("The PIGs will remember you for this.")
    time.sleep(3)
    exit()


menu()
option = int(input("\nSelect a game mode: "))

while option != 0:
    if option == 1:
        option_1()
    elif option == 2:
        print("Loading 1vBOT game mode\n ....")
        option_2()
    elif option == 3:
        print("Loading MULTIPLAYER game mode\n ....")
        option_3()
    elif option == 4:
        creds()
    else:
        exit_sequence()

    menu()
    option = int(input("\nSelect a game mode: "))

