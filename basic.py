from colorama import Back
import random

f = open('answers.txt', 'r')
answers = f.read()

c = open('guesses.txt', 'r')
allowed = f.read()

word_list = answers.split('\n')
allowed_list = allowed.split('\n')

while True:
    count = 0
    word = random.choice(word_list)
    word = word.upper()
    print("Enter Your 5 letter Guess word: ")
    # print(word)

    while count < 6:
        count = count + 1

        guess = input()
        guess = guess.upper()
        for j in range(len(allowed_list)):
            if guess == allowed_list[j]:
                print("Word not in Dictionary")
            else:
                output = ""
                if word == guess:
                    print("Congrats You Got it!")
                    print("The Word is: ", word)
                    count = count + 6
                else:
                    for i in range(len(word)):
                        if guess[i] == word[i]:
                            output = output + Back.RED + guess[i] + Back.RESET
                        elif guess[i] in word:
                            output = output + Back.YELLOW + guess[i] + Back.RESET
                        else:
                            output = output + guess[i] + Back.RESET
                    print(output)
    print("You lost! The word was: ", word)


