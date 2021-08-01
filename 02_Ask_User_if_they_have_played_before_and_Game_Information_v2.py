#Ask the User if they have Played Before Yes/No Component version 2
#Version 2 of this Component includes the Game Information of the Quiz Quest Game

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
def game_information():
    print("*****Quiz Quest Game information*****")
    "The Quiz Quest Game is a mathematics game where you answer either addition, subtraction, multiplication or division questions\n"
    "As soon as the game starts you will be asked how many questions you want to answer where you choose the number of questions you want to answer or\n" \
    "you can press <ENTER> to answer a continuos number of questions. You then will have the option to choose one of the four Game Modes (addition, subtraction, multiplication or division)" \
    "previosly mentioned. After each given question you will be asked if you want to continue playing the game or not." \
    "To continue playing you press <ENTER> and to stop answering questions you input 'xxx'."
    "This is a lot to take in but the game is very intuitive and there should be clear instructions for you to play"
    "OK! Go have some fun! Let the Questions begin!"

    return ""

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