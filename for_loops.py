#********************************************************************
 #                                                                  
 #  Team Edge List Mini-project: FOR LOOP CHALLENGES
 # 
 #   Complete the following loop challenges below. Follow the ToDos
 #   1. COUNTER: Write a loop that prints a happy birthday message for every
 #      year you have been alive.
 #   2. ITERATOR: Write a for for loop that prints every item in a list

 #   3. EVEN COUNTDOWN: Write a for loop that counts down from 100 to 0, 
 #      printing only the odd numers
 #   4. FINDER: Write a function that takes in a list and a word and prints 
 #      CONGRATULATIONS!! if the word is found in the list
 #   5. NESTED: Write a function that logs every letter in a sentence
 # 
 # ***************************************************************/
import random

print("------------------- CHALLENGE 1 : COUNTER -------------------")

#this list prints every number between 0 and 10, using range

for x in range(11):
    print("Counter at: " + str(x))
   

#-->TODO: Write a loop that prints a happy birthday message for every year you have been alive.
for count in range(1,17):
    print ("Happy " + str(count) + "th birthday")


print("------------------- CHALLENGE 2 : ITERATOR ----------------------")

#here is a list full of colors...
colors = ['red' , 'violet' , 'cyan' , 'pink' , 'lime' , 'white' , 'yellow', 'black' , 'magenta', 'green', 'orange']

#This is how you can iterate through a list:
for x in colors:
    print("The color is: " + x)

#-->TODO: Declare a list with at least 5 animals. You provide the animals.
animals = ['lion', 'cat', 'chicken', 'dog', 'fish']

#-->TODO: Print all the animals in the array with a for loop. 
for y in animals:
    print("The animal is "+ y)


print("------------------- CHALLENGE 3 : EVEN COUNTDOWN ------------------")


#The line below makes a random number between 0-50 and assigns it to the random variable
random = random.randint(0, 50)

#this if/else statement checks if the number is even using the modulo operator (%)
if random % 2 == 0:
    print(str(random) + " is even!")
else:
    print(str(random) + " is odd!")

#-->TODO: Write a function that counts BACKWARDS from 100 and prints only even numbers
def count_back():
    for x in range(100, 0, -1):
        if x % 2 == 0:
            print(x)
count_back()

print("\n-----------------\n")
#-->TODO: Write a function that counts BACKWARDS from the given random number and prints only odd numbers
def count_funct():
    global random
    for count in range(random, 0, -1):
        if count % 2 != 0:
            print(count)
count_funct()

print("------------------- CHALLENGE 4 : Finder ------------------")

#This code uses the in operator to see if an element exists in a list. It only has to appear once.
color = input('Type a one word color and see if it is one of my favorite colors! >> ')
if color in colors:
    print("Yes, that color is a fav")
else:
    print("No, that color is not one of my favorites")

#-->TODO Declare a list of any strings you  want: cities, friends, movies, etc.
my_list = ["new york", "new jersey", "ernesto", "mijail", "doctor strange", "total recall"]


#-->TODO Write function to prompt the user to "Guess" if an element is present in your list. Store their response in a variable. 
#   --> If their guess is in your list, print CONGRATULATIONS!
def guess():
    global my_list
    user_guess = input("Guess which city, friend or movie I have or like >> ").lower()
    if user_guess in my_list:
        print("CONGRATULATIONS!")
    else:
        print("Try again later")

#-->TODO Call your function.
guess()


print("------------------- CHALLENGE 5 : Nested ------------------")

#this is how you get the length of a word:
big_word = "antidisestablishmentarianism"
print(f"{big_word} has {len(big_word)} letters")

#this is how you can nest for loops, one inside the other! These loop through all the colors, and then through all the characters in the color
for color in colors:
#for all the colors:
    print(color)
    for c in color:
        print(" - " + c) #log each letter. Remember, a string is also an array of characters.


#-->TODO Write a function that prints every letter in a sentence that a user enters.
user_words = []
def challenge():
    global user_words
    user_input = input("Enter a word\n").lower()
    user_words.append(user_input)
    splitting = user_input.split(" ")
    for x in splitting:
        print(x)
        for c in x:
            print(" - "+ c)
    return user_words
c = challenge()

#-->CHALLENGE: Let the user know which word is the shortest one!
for times in range(2):
    challenge()

word1 = len(user_words[0])
word2 = len(user_words[1])
word3 = len(user_words[2])

if word1<word2 and word1<word3:
    print(str(user_words[0]) + " is the shortest word")
elif word2<word1 and word2< word3:
    print(str(user_words[1]) + " is the shortest word")
elif word3<word1 and word3< word3:
    print(str(user_words[2]) + " is the shortest word")
else:
    print("there is a tie between 2 or 3 words")
