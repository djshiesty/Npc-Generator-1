# Npc-Generator-1

This is the README in my repository for my project that I have created.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [My background](#my-background)
- [An example of my code](#an-example-of-my-code)
- [Feedback and Contributing](#feedback-and-contributing)

## Overview

*A brief description of my program.*

This is a python program which generates NPCs (Non playable characters) based on the inputs the user provides and randomly generated 
options inside of a list. The inputs specifically ask for each characters name and age, weight, and height ranges, along with a 
statement asking them whether if the NPCs have a pet or not. Alongside that, two atributes (Hair color and clothing) and randomly generated
from a prewriten list. It should also be important to note that these ranges randomly select a single value from the given input. Each 
atribute and input is individual to each NPC character, where they print out in designated rows.


## Features

*Key highlights of my program.*

- Feature 1: Outputs: The program gives you an outcome based on an input, and random selections from either inputted ranges or pre-written
  lists.
- Feature 2: Conveniences: The program makes it more convenient to write down large arrays of different NPC characters, where you can decide
  how many characters you wish to generate and what exactly you want in each of them. After writing down on all of the inputs, they print out
  in a neat, orderly list.
- Feature 3: Error handling: One of the features I added that saved a lot of hassle was solving the capitalization issue in my boolean portion
  of the program. Whenever I typed in an input that wasnt capitalized properly, it rendered it as 'False', which bugged me for a while.
  However, I found out that adding a '.upper()' after stating the variable name (for the input) when making a detection system for 'True' or
  'False' helped solve the problem immediately. This helped the program run a bit easier and allowed for more flexibility in user inputting.


## My background

*A brief description about myself.*

I am a highschool student from the United States who has a passion for coding and technological software. Computer Science is a very
interesting topic to me; its very cool to see how a bunch of binary numbers can create an advanced software capable of changing our lives,
such as artifical intelligence, or the internet. I really enjoy coding and learning new things about this amazing field of industry
and innovation. It intrigues me to understand more about computer science and its endless aspects and utilitarian features included.

## An example of my code

*This code example demonstrates a main feature of my code, where I created a variable for the number of characters that the user wants,
and another one (i) to implement in my 'for' loop. I then created an input statement where the user writes down the NPC characters name,
and the code appends the input to a priorly made list where it marks down the given name of that specific character.*

```python
num_character=int(input("How many characters are required?:"))
print(num_character)
i=0

for i in range(num_character):
    print("What is character name for",i+1)
    npcnamelist.append(str(input()))
```

## Feedback and Contributing

For any feedback or questions, feel free to reach out!

