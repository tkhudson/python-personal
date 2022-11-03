print("Hello! Welcome to a Linux Command Quiz!")

playing = input("Would you like to begin? ")

if playing.lower() != "yes":
    quit()

print("Sweet! Let's play!")
score = 0

answer = input ("What is ls used for?  a) prints working directory  b) lists everything in current directory  c) takes user to root directory ")
if answer.lower() == "b":
    print("Correct!")
    score += 1
else:
    print("Incorrect.")

answer = input ("What is cd used for?  a) deletes a file  b) copy files  c) used for navigating through files ")
if answer.lower() == "c":
    print("Correct!")
    score += 1
else:
    print("Incorrect.")

answer = input ("What is pwd used for?  a) prints working directory  b) lists everything in current directory  c) changes password ")
if answer.lower() == "a":
    print("Correct!")
    score += 1
else:
    print("Incorrect.")

answer = input ("What is cd .. used for?  a) enters a directory  b) lists a directory items  c) goes backwards in a directory ")
if answer.lower() == "c":
    print("Correct!")
    score += 1
else:
    print("Incorrect.")

answer = input ("What is rm used for?  a) deletes a directory  b) deletes an item  c) deletes a folder ")
if answer.lower() == "b":
    print("Correct!")
    score += 1
else:
    print("Incorrect.")

answer = input ("What is cp used for?  a) copys files  b) enters a directory  c) copies a non-empty folder ")
if answer.lower() == "a":
    print("Correct!")
    score += 1
else:
    print("Incorrect.")

answer = input ("What is mkdir used for?  a) ceates a duplicate of a folder  b) creates a new folder  c) deletes an empty folder ")
if answer.lower() == "b":
    print("Correct!")
    score += 1
else:
    print("Incorrect.")

answer = input ("What is rmdir used for?  a) deletes a folder with items  b) deletes an empty folder  c) deletes a file ")
if answer.lower() == "b":
    print("Correct!")
    score += 1
else:
    print("Incorrect.")

answer = input ("What is rm -r used for?  a) deletes a folder with items  b) deletes an empty folder  c) deletes a file ")
if answer.lower() == "a":
    print("Correct!")
    score += 1
else:
    print("Incorrect.")

answer = input ("What is cd / used for?  a) takes user to a specific directory  b) takes user to root directory  c) changes user interface ")
if answer.lower() == "b":
    print("Correct!")
    score += 1
else:
    print("Incorrect.")

print("You got " + str((score / 10) * 100) + "%")

input('Press ENTER to exit')
