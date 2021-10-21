#fix the win function
import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readline()
    wordlist = line.split()
    return wordlist

hangers = [
'''
------
|    |  
|          
|      
|      
|  
''',

'''
------
|    |  
|    o      
|      
|      
|  
''',

'''
------
|    |  
|    o      
|    |      
|      
|  
''',

'''
------
|    |  
|    o      
|   \|      
|      
|  

''',

'''
------
|    |  
|    o      
|   \|/      
|      
|  
''',

'''
------
|    |  
|    o      
|   \|/      
|   /  
|  
''',

'''
------
|    |  
|    o      
|   \|/      
|   / \ 
|  
''',
]

def chooseWord(wordlist):
    return random.choice(wordlist)

wordlist = loadWords()

def isWordGuessed(word, lettersGuessed):
    count = 0
    print(word)
    for letter in word:
        if letter in lettersGuessed:
            count += 1
    if count == len(word):
        return True
    else:
        return False

def getGuessedWord(word, lettersGuessed):
    print("Previous guesses: " + str(lettersGuessed))
    list_of_correct_guesses=[]
    for letter in word:
        if letter in lettersGuessed:
            list_of_correct_guesses.append(letter)   
    answer = ''
    for letter in word:
        if letter in list_of_correct_guesses:
            answer+=letter
        else:
            answer+='_ '
    return answer
        
def hangman(word):
    print("Welcome to Hangman!")
    print("The word is",len(word),"letters long.")
    global lettersGuessed
    mistakeMade = 0
    lettersGuessed=[]
    
    while 6 - mistakeMade > 0:
        
        if isWordGuessed(word, lettersGuessed):
            print("Congratulations, you won!")
            break
            
        else:
            print("You have",6-mistakeMade,"incorrect guesses left.")
            guess=str(input("Guess a letter: ")).lower()
            
            if guess in lettersGuessed:
                print("You've already guessed that letter:",getGuessedWord(word,lettersGuessed))
                
            elif guess in word and guess not in lettersGuessed:
                lettersGuessed.append(guess)
                print("Good guess:",getGuessedWord(word,lettersGuessed))
                
            else:
                lettersGuessed.append(guess)
                mistakeMade += 1
                print("That letter is incorrect:",getGuessedWord(word,lettersGuessed))
                
        if 6 - mistakeMade == 0:
            print("You ran out of guesses. You lost. The word was ",word)
            break
        
        else:
            continue


word = chooseWord(wordlist).lower()
hangman(word)