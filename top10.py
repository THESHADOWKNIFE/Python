BIGGEST_COUNTRIES_ANSWERS = ["russia", "canada", "china", "us", "brazil", "australia", "india", "argentina", "kazakhstan", "algeria"]

# FUNCTIONS #

# Welcomes user and introduces the quiz
def intro():
    #Ask the user their name
    name = input("What's your name?")

    #Greet the user and introduce the quiz
    print("Welcome to this quiz,", name)
    print("This quiz is about the ten largest countries in the world. Can you name them?")

# MAIN CODE #

intro()
# Asks user for lives and confirms is valid
def getLives():
    while True:
        lives = input("How many chances do you want?")
        try:
            # Checking if vaild number
            lives = int(lives)
            if lives >= 0:
                return lives
            else:
                print("Please choose a positive number")
        except:
            print("That wasn't a number")
            
lives = getLives()