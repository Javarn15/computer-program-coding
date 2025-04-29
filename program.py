name = input("What is your name")


def get_age(name):
    while True:
        try:
            age = int(input(f"Hi {name}, please enter your age: "))
            if age > 0:
                return age
            else:
                print("Invalid input. Age must be greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a valid number for your age.")

# Subroutine to variable
age = get_age(name)

def validate_age(age):
    if age < 5:
        print("Sorry, you must be 5 or older to participate.")
        exit()
    if age > 17:
        print("Sorry, you must be 17 or younger to go to camp .")

        validate_age(age)

        print()