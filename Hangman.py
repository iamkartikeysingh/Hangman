import random
from hangman_words import word_list
from hangman_art import logo 
from hangman_art import stages
print(logo)
random_word = random.choice(word_list)
display = []
lives = 6
word_length = len(random_word)
end_of_game = False
for _ in range(word_length):
    display+="_"
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    for position in range(word_length):
        letter = random_word[position]
        if letter == guess:
            display[position] = letter
    if guess == guess:
        print(f"You have already guessed {guess}")
    if guess not in random_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives-=1

    print(f"{' '.join(display)}")
    if(lives==0):
        end_of_game=True
        print("You Lose")

    if "_" not in display:
        end_of_game=True
        print("You Win")
    
    print(stages[lives])
