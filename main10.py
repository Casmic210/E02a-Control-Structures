#!/usr/bin/env python3
import sys, random

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"


print('Greetings!') #it prints out the word "Greetings!" to the player
colors = ['red','orange','yellow','green','blue','violet','purple'] #This is a selection of the colors that could be the answer
play_again = ''
best_count = sys.maxsize            # the biggest number

while (play_again != 'n' and play_again != 'no'):
    match_color = random.choice(colors) #the color is randomly generated
    count = 0 #count is zero because player hasn't guessed yet
    color = '' #randomly generated color is selected as the answer
    while (color != match_color): #if the color typed matches the answer
        color = input("\nWhat is my favorite color? ")  #\n is a special code that adds a new line
        color = color.lower().strip() #code to help with capitals and spaces
        count += 1 #Player has guessed once, the number increases
        if (color == match_color):
            print('Correct!') #tells the player they are correct
        else: #if they didn't type the right colorvthey try again and are told how many times they've guessed
            print('Sorry, try again. You have guessed {guesses} times.'.format(guesses=count))
    
    print('\nYou guessed it in {} tries!'.format(count)) #tells how many guesses it took

    if (count < best_count): #if it is the smallest number of tries
        print('This was your best guess so far!') #tells player it was their best
        best_count = count #that number now becomes the new best number

    play_again = input("\nWould you like to play again (yes or no)? ").lower().strip() #asks to play again

print('Thanks for playing!') #if they don't want to play again, it tells player thanks