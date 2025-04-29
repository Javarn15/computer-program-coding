name = input("What is your name")
age = input("what is your age")


def validate_age(age):
    if age < 4:
        print("Sorry, you must be 5 or older to participate.")
        exit()
    if age > 18:
        print("Sorry, you must be 17 or younger to go to camp .")