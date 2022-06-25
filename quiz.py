print("Welcome to operating system quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("What does OS stand for? ")
if answer.lower() == "operating system":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does LU stand for? ")
if answer.lower() == "logical unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does ROM stand for? ")
if answer.lower() == "read only memory":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%.")