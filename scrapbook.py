import random
import math


def generate_target():
    random_number = math.ceil(random.random() * 10)
    return random_number


def ask_replay():
    x = input('Do you want to continue? y/n: ')
    if x == 'y':
        return True
    else:
        return False


target = generate_target()
print(target)

guess_count = 0

while True:
    guess_count += 1

    user_input = input('Guess a number between 1 and 10: ')

    if not user_input.isdigit():
        print('Please enter a valid number.')
        continue

    guess = int(user_input)

    if not (1 <= guess <= 10):
        print('Please enter a number between 1 and 10.')
        continue

    if guess == target:
        print(f'You won! To got it right in total try of {guess_count}')
        if ask_replay():
            target = generate_target()
            guess_count = 0
            continue
        else:
            break
    elif guess > target:
        print('too high!')
    elif guess < target:
        print('too low!')

print('Thank you for playing')
