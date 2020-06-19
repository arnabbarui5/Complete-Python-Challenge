# Sol 1 :

# name = str(input("Enter your name : "))
# age = int(input("Enter your age : "))
#
# remYear = 100 - age
# finalYear = 2020 + remYear
#
# print("You will be 100 years old in ", finalYear)
# print("Hope you will alive till then")

# Sol 2 :

# num = int(input("Enter a number : "))
# check = int(input("Enter another number to check : "))
#
# if num % 4 == 0:
#     print("The number is divisible by 4")
# elif num % 2 == 0:
#     print("The number is divisible by 2")
# else:
#     print("The number is odd")
#
# num2 = int(num)
# check2 = int(check)
# if num2 % check2 == 0:
#     print("Yes both the numbers are divisible")
# else:
#     print("Nope , both numbers are not divisible ")


# Sol 3 :

# result = []
#
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# print("The array elements are :")
# print(a)
#
# for i in range(len(a)):
#     if a[i] < 5:
#         answer = result.append(a[i])
# print(" The elements less than 5 are :")
# print(result)
#
#
# finalResult = []
# print("I will check and tell what numbers are less then "
#       "the number you have entered")
# print("Let's see the list again :")
# print(a)
# value = int(input("Enter a number : "))
#
#
# for i in range(len(a)):
#     if a[i] < value:
#         finalAnswer = finalResult.append(a[i])
# print("The numbers less than you entered is :")
# print(finalResult)


# ---------DIVISOR----------------

# num = int(input("Enter a number : "))
#
# listNum = list(range(1, num+1))
#
# divisorList = []
# for number in listNum:
#     if num % number == 0:
#         divisorList.append(number)
#
# print(divisorList)

# ---------------------------------------------------------

# Problem :
# write a program that returns a list that contains only
# the elements that are common between the lists
# (without duplicates). Make sure your program works on two
# lists of different sizes.


# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# comList = []
#
# for i in a:
#     if i in b:
#         if i not in comList:
#             comList.append(i)
#
# print(comList)
#
# print("Now I am creating Random Samples of List to Check")
#
# # Creating Random Numbers to Test Common elements in two lists
# import random
#
# a = random.sample(range(1, 50), 10)
# print(a)
# b = random.sample(range(11, 70), 12)
# print(b)
#
# c = []
#
# for i in a:
#     if i in b:
#         if i not in c:
#             c.append(i)
#
# print("The Common elements in Randomly Generated Array List is :")
# print(c)


# ----------- Palindome String--------------------------
# Ask the user for a string and print out whether this
# string is a palindrome or not.

# say = str(input("Enter a Word : "))
#
# pal = say[::-1]
# if str(say) == str(pal):
#     print("Yes the String is a Palindrome ")
# else:
#     print("Nope ! Not a Palindrome")

# ---------------------------------------------------------

# Write one line of Python that takes this list a and
# makes a new list that has only the even elements of
# this list in it.

# a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#
# b = [element for element in a if element % 2 == 0]
# print(b)


# -------------ROCK PAPER SCISSOR GAME---------------------

# print("GAME RULE : ")
# print("You have to choose between Rock Paper and Scissor :")
# print("You can choose Q to Quit the Game")
# player1 = str(input("Enter Player 1 name : "))
# player2 = str(input("Enter Player 2 name : "))
#
# choice1 = str(input("Player 1 Choice : "))
# choice2 = str(input("Player 2 Choice : "))
#
# while True:
#
#     if choice1 == "Q":
#         print(player1, "quits the Game")
#         break
#
#     elif choice2 == "Q":
#         print(player2, "quits the Game")
#         break
#
#     elif choice1 == "rock":
#         if choice2 == "scissor":
#             print(player1, "wins this time")
#         else:
#             print(player1, "wins this time")
#             break
#
#     elif choice1 == "scissor":
#         if choice2 == "paper":
#             print(player1, "wins this time")
#         else:
#             print(player2, "wins this time")
#             break
#
#
#     elif choice1 == "paper":
#         if choice2 == "rock":
#             print(player2, "wins this time")
#         else:
#             print(player1, "wins this time")
#             break


# -----------Guessing Game----------------------

# import random
#
# number = random.randint(1, 9)
# guess = 0
# count = 0
#
# while guess != number and guess != "exit":
#     guess = input("What's your guess? : ")
#
#     if guess == "exit":
#         break
#
#     guess = int(guess)
#     count += 1
#
#     per = (1/count) * 100
#
#     if guess < number:
#         print("Too low!")
#     elif guess > number:
#         print("Too high!")
#     else:
#         print("You got it!")
#         print("And it only took you", count, "tries!")
#         print("Your accuracy is", per, "%")


# ------------List Overlap Comprehension-----------------

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#
# print(a)
# print(b)
#
# c = []
#
# for i in a:
#     if i in b:
#         if i not in c:
#             c.append(i)
#
# print("Common elements are ", c)


# -----------Primarility Functions---------------

# n = int(input("Enter a number : "))
#
#
# def prime(num):
#     if n > 1:
#         for i in range(2, n):
#             if num % i == 0:
#                 print("It is a consonent")
#                 break
#         else:
#             print("It is a prime number")
#     else:
#         print("It is neither Prime nor Consonent")
#
#
# prime(n)


# ------------------------List Ends----------------------

# a = [5, 10, 15, 20, 25]
#
# result = []
#
# for i in range(len(a)):
#     result.append(a[0])
#     result.append(a[-1])
#     break
#
# print(result)

# -------------------------------------------------------
# import random
#
# a = random.sample(range(1, 9), 5)
# print(a)
#
# result = []
#
# for i in range(len(a)):
#     result.append(a[0])
#     result.append(a[-1])
#     break
#
# print("First and Last are : ", result)

# ------------------Fabonicci Series------------------------------

# terms = int(input("Enter how many terms : "))
#
# n1, n2 = 0, 1
# count = 0
#
# print("Generating Fibonacci Series :")
#
# if terms <= 0:
#     print("Please enter a positive number ")
# elif terms == 1:
#     print(n1)
# else:
#     while count < terms:
#         print(n1)
#         nth = n1 + n2
#         # Updating Values
#         n1 = n2
#         n2 = nth
#         count += 1

# --------------------------------------------------------

# def fibo(n):
#     if n <= 1:
#         return n
#     else:
#         return fibo(n - 1) + fibo(n - 2)
#
#
# num = int(input("Enter a number : "))
#
# # check if the number of terms is valid
# if num <= 0:
#     print("Please enter a positive integer")
# else:
#     print("Fibonacci sequence:")
#     for i in range(num):
#         print(fibo(i))


# ------------------------------------------------------------

# Write a program (function!) that takes a list and returns
# a new list that contains all the elements of the first list
# minus all the duplicates.


# a = [1, 2, 3, 4, 5, 4, 3, 2, 1]
# print(a)
# b = []
#
# b.extend(i for i in a if i not in b)
# print(b)
# -------------------Using Functions-----------------------
# def newList(x):
#     b = []
#     b.extend(i for i in x if i not in b)
#     return b
#
#
# a = [1, 2, 3, 4, 5, 6, 2, 3, 4, 2, 1, 3, 5, 2, 100]
# print(a)
# print(newList(a))


# ------------Reverse Word Order--------------------

# def reverseWord(w):
#     return ' '.join(w.split()[::-1])
#
#
# print(reverseWord("I am Pablu"))


# ----------Password Generator-----------------------

# import random
# import string
#
#
# def randomString(stringLength=8):
#     letter = string.ascii_letters + string.digits
#     return ' '.join(random.choice(letter) for i in range(stringLength))
#
#
# print("How strong you want Password :")
# print("""
# 1. For Strong Password type 'strong'
# 1. For Medium Password type 'medium'
# 1. For Weak Password type 'weak'
# """)
#
# takeCommand = input(" Now Say : ")
#
# if takeCommand == "strong":
#     print(randomString(10))
# elif takeCommand == 'medium':
#     print(randomString(6))
# elif takeCommand == 'weak':
#     print(randomString(4))
# else:
#     print("You have to Select One")

# ------------------------COWS AND BULLS GAME------------------------
# import random
#
#
# def compare_numbers(number, user_guess):
#     cowbull = [0, 0]  # cows, then bulls
#     for i in range(len(number)):
#         if number[i] == user_guess[i]:
#             cowbull[1] += 1
#         else:
#             cowbull[0] += 1
#     return cowbull
#
#
# if __name__ == "__main__":
#     playing = True  # gotta play the game
#     number = str(random.randint(0, 9999))  # random 4 digit number
#     print(number)
#     guesses = 0
#
#     print("Let's play a game of Cowbull!")  # explanation
#     print("I will generate a number, and you have to guess the numbers one digit at a time.")
#     print("For every number in the wrong place, you get a cow. For every one in the right place, you get a bull.")
#     print("The game ends when you get 4 bulls!")
#     print("Type exit at any prompt to exit.")
#
#     while playing:
#         user_guess = input("Give me your best guess! : ")
#         if user_guess == "exit":
#             break
#         cowbullcount = compare_numbers(number, user_guess)
#         guesses += 1
#
#         print("You have " + str(cowbullcount[0]) + " cows, and " + str(cowbullcount[1]) + " bulls.")
#
#         if cowbullcount[1] == 4:
#             playing = False
#             print("You win the game after " + str(guesses) + "! The number was " + str(number))
#             break  # redundant exit
#         else:
#             print("Your guess isn't quite right, try again.")


# ----------------Element Search---------------------------
# def func(oList, number):
#     for i in oList:
#         if i == number:
#             return True
#     return False
#
#
# OrderedList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# if __name__ == "__main__":
#     print(func(OrderedList, 6))
#     print(func(OrderedList, 11))
#     print(func(OrderedList, 2))
#     print(func(OrderedList, 9))
#     print(func(OrderedList, 20))
#     print(func(OrderedList, 15))

# -------------------Draw a a Game Board----------------------

# a = '---'.join('    ')
# b = '   '.join('||||')
# print('\n'.join((a, b, a, b, a, b, a)))
# ------------- Pick Word ------------------------
# import random
#
# with open('words.txt') as f:
#     word = list(f)
# print(random.choice(word).strip())

# ------------------HANGMAN Game--------------------------------

# if __name__ == '__main__':
#     print("Welcome to hangman!!")
#     word = "EVAPORATE"
#     guessed = "_" * len(word)
#     word = list(word)
#     guessed = list(guessed)
#     lstGuessed = []
#     letter = input("guess letter: ")
#     while True:
#         if letter.upper() in lstGuessed:
#             letter = ''
#             print("Already guessed!!")
#         elif letter.upper() in word:
#             index = word.index(letter.upper())
#             guessed[index] = letter.upper()
#             word[index] = '_'
#         else:
#             print(''.join(guessed))
#             if letter is not '':
#                 lstGuessed.append(letter.upper())
#             letter = input("guess letter: ")
#
#         if '_' not in guessed:
#             print("You won!!")
#             break


# -------------Birthday Dictionary-----------------------

# def birthday(name):
#     if name == "Albert Einstein":
#         return "14/03/1879"
#     elif name == "Benjamin Franklin":
#         return "17/01/1706"
#     elif name == "Ada Lovelace":
#         return "10/12/1815"
#
#
# print("""Welcome to the birthday dictionary. We know the birthdays of:
# Albert Einstein
# Benjamin Franklin
# Ada Lovelace""")
# say = str(input("Who's birthday do you want to look up? : "))
# print(say, "birthday is on", birthday(say))
#
# # ----------Now Using Dictionary----------------
#
# birthday = {"Albert Einstein": "14/03/1879",
#             "Benjamin Franklin": "17/01/1706",
#             "Ada Lovelace": "10/12/1815"
#             }
#
# print("""Welcome to the birthday dictionary. We know the birthdays of:
#  Albert Einstein
#  Benjamin Franklin
#  Ada Lovelace""")
# say = str(input("Who's birthday do you want to look up? : "))
# print(say, "birthday is on", birthday[say])

# ------------JSON-----------------

# birthday = {'Albert Einstein': {
#     'name': 'Albert Einstein',
#     'dob': "14/03/1879"
# }, 'Benjamin Franklin': {
#     'name': 'Benjamin Franklin',
#     'dob': "17/01/1706"
# }, 'Ada Lovelace': {
#     'name': 'Ada Lovelace',
#     'dob': "10/12/1815"
# }}
#
# print("""Welcome to the birthday dictionary. We know the birthdays of:
#   Albert Einstein
#   Benjamin Franklin
#   Ada Lovelace""")
# say = str(input("Who's birthday do you want to look up? : "))
# print(say, "birthday is on", birthday["Albert Einstein"]["dob"])

# -------------Extra ----------------------------
from collections import Counter

sandwiches = ["ham", "cheese", "roast beef", "ham", "cheese", "roast beef", "ham"]
c = Counter(sandwiches)
print(c)
print("There are {} ham sandwiches".format(c["ham"]))
