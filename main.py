QUESTION_FORMAT = "{}\nA.{} B.{} C.{} D.{}"
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
question = "What's the capital city of New Zealand?"
a = "Wellington"
b = "Auckland"
c = "London"
d = "Christchurch"
answer = input(QUESTION_FORMAT.format(question, a, b, c, d)).lower()
# Tell the user the answerL
if answer == a or answer == "a":
    print("Correct!")
    score += 5
elif answer != a and answer != "a" and answer != b and answer != "b" and answer != c and answer != "c":
    print("That wasn't an option!")
elif answer == "":
    print("Not sure?")
else:
    print("Wrong!")
print("The capital city of New Zealand is Wellington.")
# End the quiz
print("Well done {}. You finished the quiz. Your final score was {}".format(name, score))