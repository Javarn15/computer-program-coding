
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

#activities to choose from 
activity_list = ['cultural immersion(5-days "easy" cost 800$)','Kayaking and Pancakes(3-days "moderate" costs 400$)','Mountain biking(4-days "difficult" costs 900$)']
 
print('Choose an activity: ')
print(f'1. {activity_list[0]}')
print(f'2. {activity_list[1]}')
print(f'3. {activity_list[2]}')


# Activity input with validation
while True:
    try:
        chosen_activity = int(input("Enter the number of your chosen activity: "))
        if chosen_activity in [1, 2, 3]:
            break
        else:
            print("Invalid input. Please enter a number between 1 and 3.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if chosen_activity == 1:
    activity_fee = 800
elif chosen_activity == 2:
    activity_fee = 400
elif chosen_activity == 3:
    activity_fee = 900

   
   
   
meal_opitions = ['standered','vegetarian','vegan']

print('choose a meal option: ')
print(f'1. {meal_opitions[0]}')
print(f'2. {meal_opitions[1]}')
print(f'3. {meal_opitions[2]}')

while True:
    try:
        chosen_meal = int(input("Enter the number of your chosen meal: "))
        if chosen_meal in [1, 2, 3]:
            break
        else:
            print("Invalid input. Please enter a number between 1 and 3.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")



   #shuttle bus fee 



def def_shuttle_bus():
    while True:
        Shuttle_bus = input('Do you require a shuttle bus for $80? (yes/no) (y/n): ')
        if Shuttle_bus in ['yes', 'y']:
            shuttle_fee = 80
            return shuttle_fee
        elif Shuttle_bus in ['no', 'n']:
            shuttle_fee = 0
            return shuttle_fee
        else:
            print('Invalid input. Please enter "yes" or "no".')
            print()
 
shuttle_fee = def_shuttle_bus()
print(f'Your shuttle bus fee is: ${shuttle_fee}')
 

 #total coat for the camp

total_cost= activity_fee + shuttle_fee 

final = input(f" would you like to pay {total_cost}? (yes/no) (y/n) ")
if final == "yes":
    print ("thanks welcome to camp")
else:
    print("cancel")    


            


