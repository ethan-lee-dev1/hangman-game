# generate a random word
from random_word import RandomWords
from hook import hooks
r = RandomWords()
random_word = r.get_random_word()
current_guess = "_" * len(random_word)
print(random_word)

# number of tries is 8
num_of_tries = 8

def replace(str, guess, list):
    result = ""
    for char in str:
        # if current character is not guessed alphabet and is not _
        if char == guess:
            result += guess
        elif char in list:
            result += char
        else:
            result += "_"
    # print(list)
    return result

list_of_correct_guess = []
counter = 0
# while number of tries > 0 and current guess doesn't have "_"
while num_of_tries > 0 and "_" in current_guess:
    # current guess
    print("Guess the word: ", current_guess)
    # Tries left
    print("Tries left: ", num_of_tries)
    # Enter a letter: 
    guess = input("Enter a letter :")
    # make user input the guess alphabet
    # for loop to check if alphabet exist in the random_word and get the indeces
    #get the index of the alphabet
    # replace the "_" with the alphabet
        # print Good guess!
    if guess in random_word:
        list_of_correct_guess.append(guess)
        current_guess = replace(random_word, guess, list_of_correct_guess)
        print("Good guess!")
        print("--------------------------------------")
    else:
        print(hooks[counter])
        print("Oops! That letter is not in the word.")
        print("--------------------------------------")
        # subtract 1 from number of tries
        num_of_tries -= 1
        counter += 1

    if num_of_tries > 0 and "_" not in current_guess:
        print("You Won!")


if num_of_tries == 0:
    print("Game Over!")
    
    
