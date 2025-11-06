from sys import exec_prefix


participants =[]
print("Welcome to SMIT TechFest!")
print("Event organized by Feliciano Vicenzo Pineda IV of APPDAET BTCS1")

num_parti = int(input("\nHow many participants will register?"))

if num_parti > 0:
    for i in range(num_parti):
        name = (input("\nEnter participant's name: "))
        course = (input("\nEnter chosen track: "))
        participant = {"name": name, "track": course}
        participants.append(participant)

    print("\nRegistered Participants:")
    index = 1
    while index <= len(participants):
        participant = participants[index - 1]
        print(f"{index}. {participant['name']} - {participant['track']}")
        index += 1


    unique_courses = {p["track"] for p in participants}
    if len(unique_courses) < 2:
        print("\nNot enough variety in tracks.")
    else:
        print(f"\nTracks offered in this event: ")
        for track in unique_courses:
            print(track)


else:
    print("Invaild number of participants.")
    exit()







