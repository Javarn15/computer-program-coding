
def get_name():
    while True:
        sub_name = input("Enter your name: ")
        if len(sub_name) > 0:
            return sub_name 
        else:
            print("Invalid input. Please enter your name.")

# Subroutine to variable
name = get_name()

# ==========================
# Section 2: Age Input and Age Range Validation
# ==========================

# Age input and validation subroutine
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

# Age range validation subroutine
def validate_age(age):
    if age < 12:
        print("Sorry, you must be 5 or older to participate in the camp.")
        exit()
    if age > 17:
        print("Sorry, you must be 17 or younger to participate in the camp.")
        exit()

# Validate age
validate_age(age)

# Blank line
print()

activity_list = ['cultural immersion(5-days "easy" cost 800$)','Kayaking and Pancakes(3-days "moderate" costs 400$)','Mountain biking(4-days "difficult" costs 900$)']
 
print('Choose an activity: ')
print(f'1. {activity_list[0]}')
print(f'2. {activity_list[1]}')
print(f'3. {activity_list[2]}')
    

while True:
        try:
            chosen_activity = int(input("Enter the number of your chosen activity: "))
            if chosen_activity in [1, 2, 3]:
                break           
            else:
                print("Invalid input. Please enter a number between 1 and 3.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

              #meal options 


            meal_opitions = ['standered','vegetarian','dairy-free','no meal']
