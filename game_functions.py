import random

# function to be used by game_1: Guess the Number
def pick_value(poss_values):
    middle_index == poss_values // 2
    return poss_values[middle_index]

# function to be used in game_2: Higher or Lower
def check_higher_lower(current_val, next_val, user_input):
    if next_val > current_val and user_input == 'h':
        return True
    elif next_val < current_val and user_input == 'l':
        return True
    else:
        return False


 

# function to be used in game_3: Hangman
def process_guess(letter, board, word):
    found = False

    # Check each position in the word for the letter inputted
    for i in range(len(word)):
        if word[i] == letter:
            board[i] = letter
            found = True

    if found:
        print(f"Good job! '{letter}' is in the word")
        return True
    else:
        print(f"Sorry, '{letter}' is not in the word ")
        return False


