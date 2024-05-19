score = 0
play = "yes"
# Get user's name
name = input("What's your name?")
# Greet the user and introduce the quiz
if name == "Lorenzo":
    print("That's cool.")
    print("My name is Vegeta.")
print("Let's play a game.")
print("Welcome to the quiz,", name)
print("This quiz is about capital cities of the world.")
# Check number of question attempts
while True:
    try:
        tries = input("How many attempts do you want at each question? 1-5")
        tries = int(tries)
        break
    except:
        print("That's not a number!")
# Start the quiz
while play == "yes":

    question_attempts = tries
    while question_attempts > 0:
        # Ask the user a question
        question = "What's the capital city of New Zealand?"
        a = "Wellington"
        b = "Auckland"
        c = "London"
        d = "Christchurch"
        answer = input("{}\nA.{} B.{} C.{} D.{}".format(question, a, b, c, d)).lower()
        # Check the user the answer
        if answer == a or answer == "a":
            print("Correct!")
            score += 5
            break
        elif answer != a and answer != "a" and answer != b and answer != "b" and answer != c and answer != "c" and answer != d and answer != "d":
            print("That wasn't an option!")
        elif answer == "":
            print("Not sure?")
        else:
            print("Wrong!")

        question_attempts -= 1
    print("The capital city of New Zealand is Wellington.")
    # End the quiz
    print("Well done {}. You finished the quiz. Your final score was {}".format(name, score))
    # Replay
    play = input("Do you want to play again?").lower()