from replit import clear
import random
from hangman_words import word_list
lives = 6
from hangman_art import logo
print(logo)
#Randomly choose a word from the word_list from hangman_word
chosen_word = random.choice(word_list)
#display to create blanks
display = []  
for char in chosen_word:
  display += "_"
print(display)

end_of_game = False
#Loop to check if the Player has won or not
while not end_of_game:
  
  guess = input("Guess a letter: ").lower() 
  clear()
  if guess in display:
    print("You have already guessed it")
  for position in range(len(chosen_word)):
    letter = chosen_word[position]
    if guess == letter:
      display[position] = letter
    # To keep a track of lives in the game
  if guess not in chosen_word:
    lives -= 1
    print("Uh oh! Wrong letter, You loose a life")
    #Checking Loose
    if lives == 0:
      end_of_game = True
      print("You loose")

  #Join all the elements in list and turn it into a string
  print(' '.join(display))  


  #CHecking Win
  if "_" not in display:
    end_of_game = True
    print("You Won")

  from hangman_art import stages
  print(stages[lives])

#Printing Solution
print(f"The corect Word was {chosen_word}")