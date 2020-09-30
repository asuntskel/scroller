import os
size = 20
ground = ["_" for i in range(size)]
print(ground)

char = "o"
ground[5] = char
def clear():
    os.system("CLS")

def checkinput():
    key_pressed = input("> ")

    if key_pressed == "d":
        if ground[size-1] == char:
            pass
        else:
            ground[ground.index(char)+1] = char #set right tile to char value
            ground[ground.index(char)] = "_" # reinitiate origin tile to "_"

    
    if key_pressed == "a":
        if ground[0] == char:
            pass
        else:
            ground[ground.index(char)-1] = char #set right tile to char value
            ground[ground.index(char)+1] = "_" # reinitiate origin tile to "_"

    if key_pressed == "q":
        quit() if input("Are you sure you want to quit? Y/N") in "Yy" else print("mmmh")

    else:
        pass

clear()
print("Enter 'a' for left, 'd' for right! Confirm with enter.\n You may quit anytime by entering 'q'")
while True:
    checkinput()
    clear()
    print(ground)

else:
    quit()