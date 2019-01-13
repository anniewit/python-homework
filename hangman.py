import random

def choose_word():
    
    chosen_word = random.choice(list(open('words.txt')))
    #print("Spoiler alert: ")
    #print(chosen_word)
    return(chosen_word)

def print_word(word):
    print(word, sep= ' ')

def guess_letter():
    letter = input("Choose a letter between a and z: ")
    return letter

def main():

    print("Welcome to Hangman! You have 10 guesses.")

    display = []
    word = choose_word()
    display.extend(word)
    display.remove('\n') # something weird that the choice function does i guess
    #print(display)

    #initialize word
    for i in range(len(display)):
        display[i] = "_"
    
    # output
    print_word(display)
    

    guessed_letters = []    # collects all the letters that were guessed
    guess_count = 10        #can also be different to take it harder/easier
    letter_count = 1        #because word has \n as extra letter for whatever reason 
    solved = False

    while solved == False:
        # new guess
        guess = guess_letter()

        #checks if letter was guessed before
        while guess in guessed_letters: 
            print('Letter used already. Try a different one. ')
            guess = guess_letter()
        guess_count -= 1
        guessed_letters.append(guess)

        # reveals right letters and counts the right letters so far
        for i in range(len(word)):
            if word[i] == guess:
                letter_count += 1
                display[i] = guess
                
        print_word(display)

        # checking for win: as many right letters needed as word has
        if letter_count == len(word):
            print("You win!")
            solved = True
            break
        
        # 
        if guess_count > 1:
            print(str(guess_count) + " guesses left!")
        elif guess_count == 1:
            print("LAST GUESS!")
        elif guess_count == 0:
            print("You lost :( ")
            print("The right word was: " + word )
            break

    

main()