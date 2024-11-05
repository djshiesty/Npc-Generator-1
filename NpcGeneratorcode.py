#Defining the npc traits in the lists.
npcnamelist=[]
npchaircolorlist=[]
npcclothinglist=[]
npcagelist=[]
npcheightlist=[]
npcweightlist=[]
npcpetlist=[]

#Defining options for random selections and importing "random".
coloroptionlist=["Black","Brown","Blonde","Grey","White","Red"]
clothingoptionlist=["Casual","Semi-casual","Formal","Streetwear","Sportswear","Rock"]
petoptionlist=["Dog","Cat","Parrot","Fish","Hamster","Turtle","Rabbit","Snake"]
import random

#Asking the user for the number of characters he wants to generate and defining 2 variables used for the characters.
#Error Handling added for an invalid input
while True:
    try:
        num_character=int(input("How many characters are required?:"))
    except ValueError:
        print("Please enter a valid integer value")
        continue
    else:
        print(num_character)
        break
i=0
j=0

#Taking inputs for character names for the number of characters that the user wants and all of the atributes of the character, the main portion of the code. Storing all names in the list "npcnamelist".
for i in range(num_character):
    print("What is character name for",i+1)
    npcnamelist.append(str(input()))
    min_age, max_age=input("What is the age range for the NPC character?:").split("-")
    npcagelist.append(random.randrange(int(min_age),int(max_age)))
    min_height, max_height=input("What is the height range for the NPC character in cms?:").split("-")
    npcheightlist.append(random.randrange(int(min_height),int(max_height)))
    min_weight, max_weight=input("What is the weight range for the NPC character in lbs?:").split("-")
    npcweightlist.append(round(random.uniform(float(min_weight),float(max_weight)),1))
    character_pet=input("Does the NPC character have a pet or not? True or False")
    #Boolean input here
    if bool(character_pet.upper()=="TRUE"):
        npcpetlist.append(random.choice(petoptionlist))
    else:
        npcpetlist.append("None")
    npcclothinglist.append(random.choice(clothingoptionlist))
    npchaircolorlist.append(random.choice(coloroptionlist))

#Printing the final character atributes.


for j in range(num_character):
    print("\n","Character name:",npcnamelist[j],"\t","Character age:",npcagelist[j],"\t","Character height:",npcheightlist[j],"\t","Character weight:",npcweightlist[j],"\t","Character pet:",npcpetlist[j],"\t","Character hair color:",npchaircolorlist[j],"\t","Character clothing:",npcclothinglist[j])
#Opening a file and storing a simple message
f = open("chardef.txt", "w")
new_message = "Generated character values: " + str(num_character)
f.write(new_message)
f.close()

f = open("chardef.txt", "r")
print(f.read())

