print("Welcome to my quiz!")

playing = input("Would you like to play? ")

if playing.lower() != "yes":
    quit()

print("Sweet! Let's play!")
score = 0

answer = input ("What does GPU stand for? ")
if answer.lower() == "graphical processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect.")

answer = input ("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect.")

answer = input ("What does PSU stand for? ")
if answer.lower() == "power supply unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect.")

answer = input ("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect.")

print("You got " + str((score / 4) * 100) + "%")
