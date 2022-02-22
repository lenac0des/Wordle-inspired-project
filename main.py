import random

def processGuess(theAnswer, theGuess):
    position = 0
    clue = ""
    for letter in theGuess:
        if letter == theAnswer[position]:
            clue += "G"
        elif letter in theAnswer:
            clue += "Y"
        else:
            clue += "-"
        position += 1
    print(clue)
    return clue == "GGGG" #True if correct, False if not correct
    

#first load your random words and store them into a list
word_list = []
word_file = open("random_words.txt")

# Create a for loop
for word in word_file:
    word_list.append(word.strip())

# picking a random word
wordle_answer = random.choice(word_list)

# Two conditions for while loops
num_of_guesses = 0
correct_guess = False

while num_of_guesses < 6 and not correct_guess:
    word_guess = input("Insert a 5 letter word of your choice: ")
    print("You have guessed", word_guess)
    num_of_guesses += 1


    #processing the guess
    correct_guess = processGuess(wordle_answer, word_curveguess)


#ending of wordle game message
if correct_guess:
    print("Congrats! You guessed the correct word in", num_of_guesses, "times!")
else:
    print("Womp womp you have used up all of your guesses the correct word is...", wordle_answer)