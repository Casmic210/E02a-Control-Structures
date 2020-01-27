Edit README.md to answer the following questions:

- Open main01.py. Before running it, what do you expect this program to do?
  - Now right click on the main1.py window and select “Run Python File in Terminal”. Click in the bottom panel, and answer the question. Describe what happened.
  - What do you think the program did with what you typed in answer to the question?

  I expect it to ask me for input.
  Once I told it Orange It said "PS C:\Users\casey>"
  I think the program created user data for me.

- Open main02.py. Before running it, describe how this is different than main01.py.
  - What do you think the color = input() will do?
  - Run the program in the terminal and answer the question. Did the program do what you expected?

  This program is different because the imput is for a color which gets printed.
  I think the color = imput() will make the color always be my answer.
  No. It just repeated the imput back to me followed by user information.

- Open main03.py. Before running it, describe how this is different than main02.py.
  - What is happening on lines 9–12?
  - Why are lines 10 and 12 indented?
  - Run the program and answer the question. What happens if you don’t capitalize Red?
  - What does this tell you about "color"?

  This is different because it wants you to choose red. If not, it starts again.
  The programming is telling you that red is correct otherwise it is wrong.
  They're indented because they are actions based on the imput beforehand.
  If you dont capitalize Red it doesn't accept it as the right answer and you start again.
  It tells me that the "color" is used as an answer.

- Open main04.py. Before running it, describe how this is different than main03.py.
  - What problem is this trying to solve?
  - Run the program and answer the question. What happens if you use some other capitalization scheme (i.e., “RED” or “reD“)?

  This program is different because it is taking the uncapitalized "red" into account.
  It is trying to stop wrong "red" answers due to different capitals.
  It doesn't accept "RED" or "reD" because the only answer it is looking for is "Red" or "red".

- Open main05.py. What do you expect line 9 to do?
  - What problem is it trying to solve?
  - Run the program and answer the question. What happens if you add spaces before or after the word (i.e., “ RED “ or “ red”)?

  I expect line 9 to interpret any capitalization of red as all lowercases.
  It's trying to solve the capitalization problem.
  If there are spaces in the anser it is counted as wrong

- Open main06.py. How is line 9 different than in main05.py?
  - What would you guess .strip() is doing?
  - Run the program and answer the question. Is there another way of writing “red” that will break this logic?

  This line is different because it both the lowercase and a strip.
  I'm guessing that the strip is used to include spaces in the answer.
  I can break the logic by putting spaces inbetween all the letters in red.

- Open main07.py. Before running this program, how do you expect this to be different than main06.py?
  - What is happening on line 12?
  - Run the program and answer the question.

  This program is different because it gives the player a hint if they choose pink.
  Line 12 is saying that if you chose pink it will answer differently.

- Open main08.py. What is the purpose of line 9?
  - Why are lines 10–17 indented?
  - Run the program. What would happen if line 10 were moved before line 9 (and no longer indented)?
  - Make that change and run the program again. (To end any Python program, you can type ctrl-c)

  The purpose of line 9 is that when the answer is red, the following lines are correct.
  Lines 10-17 are indented because they are contingent upon the color being red. If the question is before the color instructions, then it doesn't work anymore.

- Open main09.py. What is happening on line 13?
  - What is the purpose of “count”?
  - What is happening on line 22?
  - Run the program.

  Line 13 means that the program will add up how many tries you took.
  The purpose of the counting is to see how long it took the player to guess the right answer.
  There is no Line 22.

- *Extra credit:* open main10.py. Add a comment to each line describing what it is doing (a comment follows a pound sign [#]).

- *Extra credit:* open main11.py. What is happening on lines 6-11?

  Lines 6-11 show the different color choices and allows the program to randomly generate a new color based off of the last color. This becomes the answer for the game.
  
Commit your changes and push them back to the repository.