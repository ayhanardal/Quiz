print("Welcome Quiz!")

while True:
    playing = input("Do you want to play? (Yes/No) :").lower()
    print(playing)
    if playing == "yes":
        print("Okay! Let's play :)")
        break
    elif playing == "no":
        quit()
    else:
        print("Try again.")
        continue

point = 0

answer = input("What does CPU stand for? :").lower()
if answer == "central processing unit":
    print("Correct!")
    point += 1
else:
    print("Incorrect!")

answer1 = input("What does GPU stand for? :").lower()
if answer1 == "graphic processing unit":
    print("Correct!")
    point += 1
else:
    print("Incorrect!") 

answer2 = input("What does RAM stand for? :").lower()
if answer2 == "random access memory":
    print("Correct!")
    point += 1
else:
    print("Incorrect!")

print("Result : "+ str((point / 3)*100)+"%")


while True:   
    exit = input("Type 'exit' for escape :").lower()
    if exit == "exit":
        quit()
        continue