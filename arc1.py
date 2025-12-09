"""
attempts = 0

while True:
    code = input("Please type in your PIN: ")
    attempts += 1

    if code == "1234":
        success = True
        break

    if attempts == 3:
        success = False
        break

    # this is printed if the code was incorrect AND there have been less than three attempts
    print("Incorrect...try again")

if success:
    print("Correct PIN entered!")
else:
    print("Too many attempts...")
"""


def happySad():
    mood=input("enter ur mood now  happy or sad   :" )
    if mood=="sad":
        for i in range(10):
            print(" oh baby u too fine to be sad")
    elif mood=="happy" :
            print(" love to hear that baby ")

happySad()