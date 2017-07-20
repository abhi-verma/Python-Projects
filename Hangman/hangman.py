# Hangman game
from __future__ import print_function

import random

import string

WORDLIST_FILENAME = "C:/Users/abhin/Desktop/words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    chosen_word = random.choice(wordlist)
    while len(chosen_word) != 4:
        chosen_word = random.choice(wordlist)
    return chosen_word

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
  
    secretWord = list(secretWord)
    
    for ele in lettersGuessed:
      if len(secretWord) == 0:
        return True
      else:
        if ele in secretWord:
            secretWord = [x for x in secretWord if x != ele]
    
    if len(secretWord) != 0:
        return False
    else:
        return True

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
   
    hang_man = ''
    
    for ele in secretWord:
      if ele in lettersGuessed:
        continue
      else:
        secretWord = secretWord.replace(ele, "_")
    
    for ele in secretWord:
      hang_man += (ele + ' ')
      
    return hang_man


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    
    available_letters = list(string.ascii_lowercase)
    
    for ele in lettersGuessed:
      available_letters.remove(ele)
    
    return ''.join(available_letters)

def guessesLeft(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
        
    guesses_rem = 8 - len(lettersGuessed)
    
    return guesses_rem
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
        
    lettersGuessed = []
    
    print('Welcome to the game, Hangman!')
    
    print('I am thinking of a word that is 4 letters long.')
    
    guess_rem = guessesLeft(lettersGuessed)
    
    print(secretWord)
    
    while guess_rem >= 0:
        print('----------------')
        
        if guess_rem == 0:
            print('Sorry, you ran out of guesses. The word was ' + secretWord + '.')
            break
            
        if '_' not in getGuessedWord(secretWord, lettersGuessed):
            print('Congratulations, you won!')
            break

        print('You have ' + str(guess_rem) + ' guesses left.')
        print('Available letters: ' + getAvailableLetters(lettersGuessed))
        user_guess = str(raw_input('Please guess a letter: '))
        
        if user_guess in lettersGuessed:
            print("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))
            continue
        
        lettersGuessed.append(user_guess)
        if user_guess in secretWord:
            print('Good guess: ' + getGuessedWord(secretWord, lettersGuessed))
            
        else:
            print('Oops! That letter is not in my word: ' + getGuessedWord(secretWord, lettersGuessed))
            guess_rem -= 1
    
    

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
