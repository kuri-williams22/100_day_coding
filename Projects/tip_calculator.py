#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print('Welcome to the tip calculator!')
bill = input('Enter bill here: $')
people = input('How many people are there: ')
tip = input('How much would you like to tip: ')

float_tip = float(tip)
float_bill = float(bill)
int_people = int(people)
convert_tip = ((float_tip / 100) * float_bill)
total_bill = (float_bill + convert_tip)
split_cost = (total_bill / int_people)
round_cost = "{:.2f}".format(split_cost)
print(f'Each person should pay: ${round_cost}')
