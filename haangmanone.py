from random import choice

def run_game():
    word: str = choice(['Apple', 'Cucumber', 'Grape', 'Kiwi', 'Dragon Fruit', 'Lemon', 'Plum', 'Cherries', 'Tomato', 'Plum', 'Cantaloupe'])
        
    username: str = input('What is your name? >> ')
    print(f"Welcome to Hangman, {username}!")
        
    #Setup
    guessed: str = ""
    tries: int = 3
        
    while tries > 0:
        blanks: int = 0
                
        print('Word: ', end = "")
        for char in word:
            if char in guessed:
                print(char, end = "")
            else:
                print('-', end = "")
                blanks += 1
                
        print() #Adds a blank line
        
        if blanks == 0:
            print('You Got It!')
            break
            
        guess: str = input('Enter a Letter: ')
            
        if guess in guessed:
            print(f'You already used: "{guess}". Please try with another letter!')
            continue
            
        guessed += guess
        
        if guess not in word:
            tries -= 1
            print(f"Sorry, that was wrong... ({tries} tries remaining)")
                  
                  
        if tries == 0:
            print('No more tries remaining... You Lose.')
            break
                  
                  
if __name__ == '__main__':
        run_game()