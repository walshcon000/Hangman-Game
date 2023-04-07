import random

print("Welcome to Hangman")
print("--------------------------------------------------------------------------------------")

wordDictionary = ["abruptly", "foxglove", "lengths", "subway","absurd","frazzled", "lucky", "swivel", "abyss" , "funny" , "luxury" , "syndrome"]

### Choose a random word
randomWord = random.choice(wordDictionary)

for x in randomWord:
  print("_", end=" ")

def print_hangman(wrong):
  if(wrong == 0):
    print("\n+---+")
    print("    |")
    print("    |")
    print("    |")
    print("=======")
    print("Guesses = 6")
  elif(wrong == 1): 
    print("\n+---+")
    print("O   |")
    print("    |")
    print("    |")
    print("=======")
    print("Guesses = 5")
  elif(wrong == 2):
    print("\n+---+")
    print("O   |")
    print("|   |")
    print("    |")
    print("=======")
    print("Guesses = 4")
  elif(wrong == 3):
    print("\n+---+")
    print(" O  |")
    print("/|  |")
    print("    |")
    print("=======")
    print("Guesses = 3")
  elif(wrong == 4):
    print("\n+---+")
    print(" O  |")
    print("/|\ |")
    print("    |")
    print("=======")
    print("Guesses = 2")
  elif(wrong == 5):
    print("\n+---+")
    print(" O  |")
    print("/|\ |")
    print("/   |")
    print("=======")
    print("Guesses = 1")
  elif(wrong == 6):
    print("\n+---+")
    print(" O   |")
    print("/|\  |")
    print("/ \  |")
    print("=======")
    print("Guesses = 0")

def printWord(guessedLetters):
  counter=0
  rightLetters=0
  for char in randomWord:
    if(char in guessedLetters):
      print(randomWord[counter], end=" ")
      rightLetters+=1
    else:
      print(" ", end=" ")
    counter+=1
  return rightLetters

def printLines():
  print("\r")
  for char in randomWord:
    print("\u203E", end=" ")

length_of_word_to_guess = len(randomWord)
amount_of_times_wrong = 0
current_guess_index = 0
current_letters_guessed = []
current_letters_right = 0

while(amount_of_times_wrong != 6 and current_letters_right != length_of_word_to_guess):
  print("\nLetters guessed so far: ")
  for letter in current_letters_guessed:
    print(letter, end=" ")
  ### Prompt user for input
  letterGuessed = input("\nGuess a letter: ")
  ### User is right
  if(randomWord[current_guess_index] == letterGuessed):
    print_hangman(amount_of_times_wrong)
    ### Print word
    current_guess_index+=1
    current_letters_guessed.append(letterGuessed)
    current_letters_right = printWord(current_letters_guessed)
    printLines()
  ### User was wrong
  else:
    amount_of_times_wrong+=1
    current_letters_guessed.append(letterGuessed)
    ### Update the drawing
    print_hangman(amount_of_times_wrong)
    ### Print word
    current_letters_right = printWord(current_letters_guessed)
    printLines()

print("Game over! Thanks for playing!")
