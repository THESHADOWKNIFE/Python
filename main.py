import random

QUESTION_FORMAT = "{}\nA.{} B.{} C.{} D.{}"
GOOD_COMMENTS = ["Way to go!", "Keep it up!", "Fantastic!"]
BAD_COMMENTS = ["Keep trying", "Maybe next time", "Don't give up"]
QUESTIONS = ["What is the capital of New Zealand?",
              "What is the most common pet in NZ?",
                "What is the highest mountain in NZ?"]
OPTIONS = [["Auckland", "Wellington", "Christchurch", "Dunedin"],
           ["mouse", "dog", "bird", "cat"],
           ["Mt. Taranaki", "Mt. Eden", "Mt. Aoraki", "Mt. Ruapehu"]]
SHORT_OPTIONS = ["a", "b", "c", "d"]
ANSWERS = [1,2,3]

play = "yes"

# Ask the user their name
name = input("What's your name?")

# Greet the user and introduce the quiz
print("Welcome to the quiz,", name)
print("This quiz is about capital cities of the world.")

# Check number of question attempts
while True:
    try:
        tries = input("How many attempts do you want at each question? 1-4")
        tries = int(tries)
        break
    except:
        print("That's not a number!")

# Start the quiz
while play == "yes":
    score = 0

    # Loop through each question/answers
    for i in range(len(QUESTIONS)):
        question_attempts = tries
        while question_attempts > 0:
            # Ask the user a question
            answer = input(QUESTION_FORMAT.format(QUESTIONS[i], OPTIONS[i][0],
                                                OPTIONS[i][1], OPTIONS[i][2], OPTIONS[i][3])).lower()
            
            # Check the user's answer
            if answer == OPTIONS[i][ANSWERS[i]] or answer == SHORT_OPTIONS[ANSWERS[i]]:
                print("Correct!")
                score += 5
                print(random.choice(GOOD_COMMENTS))
                break
            elif answer == "":
                print("Not sure?")
            elif answer in SHORT_OPTIONS or answer in OPTIONS[i]:
                print("Wrong!")
                print(random.choice(BAD_COMMENTS))
            else:
                print("That wasn't an option")


            question_attempts -= 1
        print("The answer is Wellington.")

    # End the quiz
    print("Well done {}. You finished the quiz. Your final score was {}".format(name, score))

    # Replay
    play = input("Do you want to play again?").lower()