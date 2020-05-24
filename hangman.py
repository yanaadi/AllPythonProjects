#!/usr/bin/env python
# coding: utf-8

# In[2]:


from random import choice

import string

hangman= ["""
  +---+
      |
      |
      |
     ===""", """
     +---+
     O   |
         |
         |
        ===""", """
     +---+
     O   |
     |   |
         |
        ===""", """
     +---+
     O   |
    /|   |
         |
        ===""", """
     +---+
     O   |
    /|\  |
         |
        ===""", """
        +---+
        O   |
       /|\  |
       /    |
           ===""", """
           +---+
           O   |
          /|\  |
          / \  |
              ==="""]
words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()

def play_game():
    
    correctLetters = ''
    
    the_word = choice(words)
    
    count = 0
    
    blanks = ['__' for i in the_word]
    
    print(hangman[count])

    gamestarts = True
    
    while gamestarts:
        
        print(*blanks)
        
        guess = input().lower()
        
        if guess not in string.ascii_lowercase:
            
            print('Invalid entry !!! Enter a valid character')
            
            continue
            
        else:
            
            count+=1
            
            for i in enumerate(the_word):
                
                if guess == the_word[i[0]]:
                    
                    correctLetters+=the_word[i[0]]
                    
                    blanks[i[0]] = guess
                    
                if blanks==list(the_word):
                    
                    print(f'You guessed it right !!! The secret word is {the_word}')
                    
                    restart = input('Would you like to play again ? (y/n)')
                    
                    if restart=='y':
                        
                        play_game()
                        
                    else:
                        
                        gamestarts = False
                        
                if count==6:
                    
                    print(f'Game Over !!! You failed to guess the secret word.The secret word is {the_word}')
                    
                    print(hangman[count])
                    
                    if len(correctLetters)>0:
                        
                        print('You managed to get these right',*correctLetters)
                    
                    restart = input('Would you like to play again ? (y/n)')
                    
                    if restart=='y':
                        
                        play_game()
                        
                    else:
                        
                        gamestarts = False
                        
                        break
            else:
                
                if guess not in the_word:
                    
                    print(hangman[count])

if __name__=='__main__':
    play_game()


# In[ ]:




