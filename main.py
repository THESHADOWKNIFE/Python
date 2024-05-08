score = 0
# Get user's name
name = input("What's your name?")
# Greet the user and introduce the quiz
if name == "Lorenzo":
    print("That's cool.")
    print("My name is Vegeta.")
print("Let's play a game.")
print("Welcome to the quiz,", name)
print("This quiz is about capital cities of the world.")
# Ask the user a question
answer = input("What's the capital city of New Zealand?").lower()
# Tell the user the answer
if answer == "Wellington".lower():
    print("Correct!")
    score += 5
elif answer == "":
    print("Not sure?")
else:
    print("Wrong!")
print("The capital city of New Zealand is Wellington.")
# End the quiz
print("Well done {}. You finished the quiz. Your final score was {}".format(name, score))