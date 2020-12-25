from random import randint


def pick_number(message):
    user_input1 = None
    while user_input1 is None:
        try:
            user_input1 = int(input(message))
        except ValueError:
            print("Please enter a number")
            continue
    return user_input1


random_int = randint(0, 100)

print(random_int)

user_guesses = []
user_input = pick_number("Guess a number between 1 and 100")


while user_input != random_int:
    while user_input in user_guesses:
        print("You already tried that!")
        user_input = pick_number("Try another number")
    else:
        user_guesses.append(user_input)
    if user_input > random_int:
        pick_number("Try something lower!")
    elif user_input < random_int:
        pick_number("Try something higher!")


print("YOU WIN!!")


