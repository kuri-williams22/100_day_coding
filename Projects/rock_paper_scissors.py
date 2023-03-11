import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
choice = int(input('Enter 0 for rock, 1 for paper, or 2 for scissors: '))
computer = random.randint(0,2)
if computer == 0:
  if choice == 0:
    print(f'Computer: {rock}')
    print(f'You: {rock}')
    print('It is a tie!')
  elif choice == 1:
    print(f'Computer: {rock}')
    print(f'You: {paper}')
    print('You win!')
  elif choice == 2:
    print(f'Computer: {rock}')
    print(f'You: {scissors}')
    print('You lose!')
  else:
    print('Not an option.')

elif computer == 1:
  if choice == 0:
    print(f'Computer: {paper}')
    print(f'You: {rock}')
    print('You lose!')
  elif choice == 1:
    print(f'Computer: {paper}')
    print(f'You: {paper}')
    print('It is a tie!')
  elif choice == 2:
      print(f'Computer: {paper}')
      print(f'You: {scissors}')
      print('You win!')
  else:
    print('Not an option')
  
elif computer == 2:
  if choice == 0:
    print(f'Computer: {scissors}')
    print(f'You: {rock}')
    print('You win!')
  elif choice == 1:
    print(f'Computer: {scissors}')
    print(f'You: {paper}')
    print('You lose!')
  elif choice == 2:
      print(f'Computer: {scissors}')
      print(f'You: {scissors}')
      print('It is a tie!')
  else:
    print('Not an option')
    
