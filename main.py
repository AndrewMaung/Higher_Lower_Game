import art
import game_data
import random

def get_new_b(data, current_b):
    new_b = random.choice(data)
    while new_b == current_b:
        new_b = random.choice(data)
    return new_b

while True:
    random_items = random.sample(game_data.data, 2)
    A, B = random_items

    print(art.logo)

    Score = 0

    while True:
        nameA = A["name"]
        descriptionA = A["description"]
        countryA = A["country"]

        nameB = B["name"]
        descriptionB = B["description"]
        countryB = B["country"]

        print(f"Compare A: {nameA}, {descriptionA}, {countryA}")
        print(art.vs)
        print(f"Compare B: {nameB}, {descriptionB}, {countryB}")

        user_input = input("Is B Higher or Lower (H/L): ").lower()

        if user_input in ('h', 'higher'):
            if descriptionA > descriptionB:
                Score += 1
                A = B  # B becomes the new A
                B = get_new_b(game_data.data, A)
            else:
                break
        elif user_input in ('l', 'lower'):
            if descriptionA < descriptionB:
                Score += 1
                A = B  # B becomes the new A
                B = get_new_b(game_data.data, A)
            else:
                break
        else:
            print("Please enter 'H' or 'L' (for Higher or Lower).")

    print(f"Your score: {Score}")
    
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        break
