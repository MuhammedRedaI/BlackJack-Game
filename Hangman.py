from words import words
import random
import string

def get_valid_word(words):
    word = random.choice(words)
    while " " in word or "-" in word:
        word = random.choice(words)
    return word.upper()

def Hangman():
    
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    live = 6
    while len(word_letters) > 0 and live > 0:
        # Corrected join formatting for better readability   
        print("you have:", live, " turn/s remaining")
        if len(used_letters) > 0:
            print("You have used these letters: ", ' '.join(used_letters)) 
        word_list = (letter if letter in used_letters else '-' for letter in word)
        print("Current Word: ", ' '.join(word_list))
        
        user_letter = input("Guess a letter: ").upper()
        
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                live -= 1
        elif user_letter in used_letters:
            print("You have already entered that!!")
        else:
            print("Please enter a valid character!!")

    if live == 0:
        print("you have no more lives, the word was:", word," you lost :( ")
    else:
        print("you have guessed the word:", word ," right. you 've won")

Hangman()
