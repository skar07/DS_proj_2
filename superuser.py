from superaction.regimeActions import regime
from superaction.userActions import userAct
import config


class supers:
    def __init__(self, name):
        self.name = name

    def actions(self):
        print("\nPlease enter a choice from below: ")
        obj1 = regime(1)

        while(True):
            print("1. Create member\n2. View member\n3. Delete member\n4. Update member\n5. Create regimen\n6. View regiment\n7. Delete regimen\n8. Update regimen\n9. Back")
            choice = int(input("Select option here: "))
            if choice == 1:
                userCreate()
            elif choice == 2:
                obj1 = userAct()
                obj1.userView()
            elif choice == 3:
                pass
            elif choice == 4:
                pass
            elif choice == 5:
                obj1.reg()
            elif choice == 6:
                pass
            elif choice == 7:
                pass
            elif choice == 8:
                pass
            elif choice == 9:
                return
            else:
                print("Invalid choice. Please type in a valid choice")
                continue


def userCreate():
    name = input("Please enter the full name of the member: ")
    age = input("Please enter the age of the member: ")
    gender = input("Please enter the gender of the member: ")
    number = int(input("Please enter the mobile number of the member: "))
    email = input("Please enter the email address of the member: ")
    bmi = input("Please enter the BMI of the member: ")
    duration = input("Please enter the membership duration of the member: ")
    config.data = {"name": name, "age": age, "gender": gender,
                   "mob": number, "email": email, "bmi": bmi, "duration": duration}
    config.members.append(config.data)
    print(config.members)
    return
