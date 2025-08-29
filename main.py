from pathlib import Path
from participant_pkg import file_ops


workspace = Path("workspace_files")
path = workspace / "contact.csv"

participant_dict = {}

print("Participant Information Saver".center(60, "-"))
while True:

    while True:
        try:
            name = input("Enter Participant name: ").title()
            if name == "":
                print("Name cannot be blank!")
                continue
            elif name.isdigit():
                print("Name cannot be a number! Try again.")
                continue
            else:
                participant_dict["Name"] = name
                break
        except Exception as e:
            print(f"Error {e}")
            continue
    
    while True:
        try:
            age = int(input("Enter participants age: "))
            if age <= 0:
                print("Age should be a whole number")
                continue
            else:
                participant_dict["Age"] = age
                break
        except Exception as e:
            print("Invalid input!")
            continue

    while True:
        try:
            number = input("Enter participant phone number: ")
            if len(number) != 11:
                print("Phone number must be 11 digits!")
                continue
            elif number.isalpha():
                print("Phone number cannot ba an alphabet!")
                continue
            else:
                participant_dict["Phone number"] = number
                break
        except Exception as e:
            print("Invalid input!")
            continue
    
    while True:
        try:
            track = input("Enter participant track: ")
            if track == "":
                print("Track cannot be blank!")
                continue
            elif track.isdigit():
                print("Track cannot be a number!")
            else:
                participant_dict["Track"] = track  
                break
        except Exception as e:
            print("Invalid input!")
            break
    
    choice = input("Do you want to add another information\n1. No\n2. Yes\nEnter: ")
    if choice == "1":
        print("Participant details have been saved successfully.\n")
        break   
    else:
        continue
        
file_ops.save_participant(path, participant_dict)
file_ops.load_participant(path)