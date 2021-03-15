from superuser import supers
from user import users
import sys


def disp():
    print("Welcome to Gym Membership Manager:")
    print("-----------------------------------------------")
    while(True):
        print("Roles:\n1. Superuser\n2. Member\n3. Exit")
        role = int(input(
            "Please enter 1 if you are a superuser, 2 if you're a member, or 3 to exit: "))
        if role == 1:
            name1 = input("Please enter your name: ")
            obj = supers(name1)
            obj.actions()
        elif role == 2:
            name2 = input("Please enter your name: ")
            obj = users(name2)
            obj.actions()
        elif role == 3:
            sys.exit()
        else:
            print("Invalid choice. Please enter a valid choice\n")
            continue
