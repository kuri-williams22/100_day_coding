# Exercise 1
# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
first_num = int(two_digit_number[0])
second_num = int(two_digit_number[1])
added_num = first_num + second_num
print(added_num)

# Exercise 2
# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
convert_height = float(height)
convert_weight = float(weight)
bmi = int((convert_weight) / (convert_height**2))
print(bmi)

# Exercise 3
# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
convert_age = int(age)
days = (90 * 365) - (convert_age * 365)
weeks = (90 * 52) - (convert_age * 52)
months = (90 * 12) - (convert_age * 12)
print(f'You have {days} days, {weeks} weeks, and {months} months left.')
