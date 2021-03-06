#Ask User if they have played before Yes/No Component version 1
#Version 1 of this Component does not include the Game Information for the Quiz Quest Game

#Yes/No Checker
#Check If the User's input is valid
def yes_no_checker(question):
    valid = False
    while not valid:
        #The User response will be lowercased
        response = input(question).lower()

        #If user response is either 'yes' or 'y' the response will be outputed as yes.
        if response == "yes" or response == "y":
            response = "yes"
            return response

        #If user response is either 'no' or 'n' the response will be outputed as no.
        elif response == "no" or response == "n":
            response = "no"
            return response

        #If user response is anything other than yes or no, User will be asked to answer yes or no.
        else:
            print("<error> please answer Yes/No (Y/N). ")
            print()

#Game information
#Instructs the User on how the Quiz Quest Game works and how to play the Quiz Quest Game
def game_information():
    print("*****Game information*****")
    return""

#Looped for testing purposes
#Looped to make it easier to get test cases
#The 'xxx' is the exit code to stop the loop
for item in range(1,20):

    #Main Routine
    #The User will be asked if they have played the game before
    played_before = yes_no_checker("Have you played this game before? ")

    if played_before == "no":
        game_information()
        print()

    elif played_before == "yes":
        print("program continues")
        print()

