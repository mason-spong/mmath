#!/usr/local/anaconda3/bin/python3

import sys, argparse, random

parser = argparse.ArgumentParser()
parser.add_argument("-a", "--addition", help="output addition problems",
  action="store_true")
args = parser.parse_args()


# random.randint(1, upper)

# num1 = randomDigits(args.digits)
# num2 = randomDigits(args.digits)

# if args.addition:
#   print(str(num1) + " + " + str(num2))

def addition():
  lower = input("Enter lower bound: ")
  upper = input("Enter upper bound: ")
  num1 = random.randint(int(lower), int(upper))
  num2 = random.randint(int(lower), int(upper))
  answer = num1 + num2
  print(str(num1) + " + " + str(num2) + " =")
  user_answer = int(input())
  if user_answer == answer:
    print("CORRECT")
  else:
    print("INCORRECT: Correct answer is " + str(answer))





def subtraction():
  print("hi")

def multiplication():
  print("hi")

def division():
  print("hi")

welcome_text = "Welcome to mmath! Select 1-4: (type 'quit' to exit)"

menu_text = "  1 Addition\n"
menu_text += "  2 Subtraction\n"
menu_text += "  3 Multiplication\n"
menu_text += "  4 Division"

menu_options = {"1", "2", "3", "4"}

user_input = ""

while user_input != "quit":
  print(welcome_text)
  print(menu_text)
  user_input = input()
  if user_input not in menu_options:
    print("'" + user_input + "' is not an option. Please select 1-4")
  elif user_input == "1":
    addition()
  elif user_input == "2":
    subtraction()
  elif user_input == "3":
    multiplication()
  elif user_input == "4":
    division()





  





  