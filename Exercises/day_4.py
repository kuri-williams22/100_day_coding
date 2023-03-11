# Pre-Exercise 1 learning random module
import random
random_integer = random.randint(1, 10)
print(random_integer)
love_score = random.randint(1, 100)
print(f'Your love score is: {love_score}')
random_float = random.random()
print(random_float)
print()

# Pre-Exercise 2 learning lists
states = ['idaho', 'colorado', 'arizona', 'california']
print(random.choice(states))
print(states[-1])

# Pre-Exercise 3 manipulating lists
# dirty_dozen = ['strawberries', 'spinach', 'kale', 'nectarines', 'apples', 'grapes', 'peaches', 'cherries', 'pears', 'tomatoes', 'celery', 'potatoes']
fruits = ['strawberries', 'nectarines', 'apples', 'grapes', 'peaches', 'pears', 'tomatoes']
vegetables = ['spinache', 'kale', 'celery', 'potatoes']
dirty_dozen = [fruits, vegetables]
print(dirty_dozen)
print(dirty_dozen[1][1])

# Exercise 1 
#Remember to use the random module
#Hint: Remember to import the random module here at the top of the file. 🎲
import random 
#Write the rest of your code below this line 👇
coin = random.randint(0,1)
if coin == 0:
    print('Heads')
else:
    print('Tails')
print()

# Exercise 2
# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
random_name = random.choice(names)
print(f'{random_name.title()} is going to buy the meal today!')
print()

# Exercise 3
# 🚨 Don't change the code below 👇
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
horizontal_position = int(position[0])
vertical_position = int(position[1])
map[vertical_position -1][horizontal_position -1] = 'X'

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")


