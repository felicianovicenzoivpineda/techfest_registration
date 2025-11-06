parti_name = []
parti_course = []
print("Welcome to SMIT TechFest!")
print("Event organized by Feliciano Vicenzo Pineda IV of APPDAET BTCS1")

num_parti = input(int("How many participants will register?"))
while True:
    if num_parti < 0:
        print("Invaild number of participants.")
        break
    else:
        continue
for i in range(len(num_parti)):
    parti_name.append(input("\nEnter participant's name: "))
    parti_course.append(input("\nEnter chosen track: "))

participant = {"parti": parti_name, "course": parti_course}

print("\nRegistered Participants:")
index = 1
while index < len(parti_name):
    print(participant)
    index += 1
