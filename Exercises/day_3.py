# Pre-exercise Roller Coaster if/elif/else nested statement
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height > 120:
    print('You are tall enough to ride the rollercoaster!')
    age = int(input('How old are you: '))
    if age < 12:
        bill = 5
    elif age <= 18:
        bill = 7
    else:
        bill = 12
    wants_photo = input('Do you want a photo taken? (Y/N): ')
    if wants_photo == 'y':
        bill += 3
    print(f'You owe ${bill}.')
else:
    print('Sorry, you are not tall enough to ride the rollercoaster!')

# Exercise 1
# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if number % 2 == 0:
    print('This is an even number.')
else:
    print('This is an odd number.')

# Exercise 2
# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = float((weight) / (height**2))
if bmi < 18.5:
    print(f'Your BMI is {round(bmi)}, you are slightly underweight')
elif bmi < 25:
    print(f'Your BMI is {round(bmi)}, you have a normal weight.')
elif bmi < 30:
    print(f'Your BMI is {round(bmi)}, you are slightly overweight.')
elif bmi < 35:
    print(f'Your BMI is {round(bmi)}, you are obese.')
else:
    print(f'Your BMI is {round(bmi)}, you are clinically obese.')

# Exercise 3
# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if year % 4 == 0:
    if year % 100 == 0:
        print('Not leap year.')
    else:
        if year % 400 == 0:
            print('Leap year.')
    print('Leap year')
else:
    print('Not leap year.')

# Exercise 4
# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bill = 0
if size.lower() == 's':
    bill = 15
    if add_pepperoni.lower() == 'y':
        bill += 2
elif size.lower() == 'm':
    bill = 20
    if add_pepperoni.lower() == 'y':
        bill += 3
else:
    bill = 25
    if add_pepperoni.lower() == 'y':
        bill += 3
if extra_cheese.lower() == 'y':
    bill += 1
print(f'Your final bill is: ${bill}.')

# Exercise 5
# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
blend_names = name1.lower() + name2.lower()
count_t = blend_names.count('t')
count_r = blend_names.count('r')
count_u = blend_names.count('u')
count_e = blend_names.count('e')
count_l = blend_names.count('l')
count_o = blend_names.count('o')
count_v = blend_names.count('v')
count_e2 = blend_names.count('e')
true_score = (count_t + count_r + count_u + count_e)
love_score = (count_l + count_o + count_v + count_e2)
total_score = str(true_score) + str(love_score)
total_score = int(total_score)

if total_score < 10 or total_score > 90:
    print(
        f'Your score is {total_score}, you go together like coke and mentos.')
elif total_score > 40 and total_score < 50:
    print(f'Your score is {total_score}, you are alright together.')
else:
    print(f'Your score is {total_score}.')
