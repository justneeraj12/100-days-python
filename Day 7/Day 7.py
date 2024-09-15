import random

stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

lives = 6
print(stages)
word_list = ["nigga","bamboo","brother","god"]
chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_lenght = len(chosen_word)
for position in range(word_lenght):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False 
correct_letters = []


while not game_over:
    print(f"***************************{lives}/6 Lives Left********************************************")
    guess = input("Guess a letter: ").lower()
if guess in correct_letters:
    print(f"You've already guessed {guess}")
display = ""



for letter in chosen_word:
    if letter == guess:
        display += letter
        correct_letters.append(guess)
    elif letter in correct_letters:
        display += letter

    else:
        display += "_"    

print("Word to guess" + display)

if guess not in chosen_word:
    lives -= 1
    print(f"You guessed {guess}, that's not in the word. you lost a life..")
    if lives == 0:
     game_over = True

     print(f"***************************It was {chosen_word},You Lost!**************************************")

if "_" not in display:
    game_over = True
    print("***********************************You win!****************************************")

print(stages[lives])