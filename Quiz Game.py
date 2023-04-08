print("Welcome to the Quiz Game!")

playing = input("Do you want to play :")

if playing.lower() == "yes":
    print("starting the game")
    score = 0
else:
    quit()

question = (input("who is the founder of tesla ?"))

if question.lower() == "elon musk":
    print("Correct Answer! ✔")
    score += 1
else:
    print("Incorrect answer")

question = (input("who is the founder of Microsoft ?"))

if question.lower() == "bill gates":
    print("Correct Answer! ✔")
    score += 1
else:
    print("Incorrect answer")

question = (input("CPU stands for what ?"))

if question.lower() == "central processing unit":
    print("Correct Answer! ✔")
    score += 1
else:
    print("Incorrect answer")

question = (input("what is the title of this game ?"))

if question.lower() == "quiz game":
    print("Correct Answer! ✔")
    score += 1
else:
    print("Incorrect answer")

print("You have scored " +str(score),"/4")
print("Thank you 💖")