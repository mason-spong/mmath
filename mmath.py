#!/usr/local/anaconda3/bin/python3

import sys, argparse, random

parser = argparse.ArgumentParser()
parser.add_argument("-a", "--addition", help="output addition problems",
  action="store_true")
args = parser.parse_args()

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

  user_command = input("[ENTER] to continue or 'menu' to return to menu\n")
  if user_command == "menu":
    return 0
  else:
    return 1

def subtraction():
  lower = input("Enter lower bound: ")
  upper = input("Enter upper bound: ")
  num1 = random.randint(int(lower), int(upper))
  num2 = random.randint(int(lower), int(upper))
  answer = num1 - num2
  print(str(num1) + " - " + str(num2) + " =")
  user_answer = int(input())
  if user_answer == answer:
    print("CORRECT")
  else:
    print("INCORRECT: Correct answer is " + str(answer))

  user_command = input("[ENTER] to continue or 'menu' to return to menu\n")
  if user_command == "menu":
    return 0
  else:
    return 2

def multiplication():
  lower = input("Enter lower bound: ")
  upper = input("Enter upper bound: ")
  num1 = random.randint(int(lower), int(upper))
  num2 = random.randint(int(lower), int(upper))
  answer = num1 * num2
  print(str(num1) + " * " + str(num2) + " =")
  user_answer = int(input())
  if user_answer == answer:
    print("CORRECT")
  else:
    print("INCORRECT: Correct answer is " + str(answer))
  user_command = input("[ENTER] to continue or 'menu' to return to menu\n")
  if user_command == "menu":
    return 0
  else:
    return 3
  
def division():
  lower = input("Enter lower bound: ")
  upper = input("Enter upper bound: ")
  num1 = random.randint(int(lower), int(upper))
  num2 = random.randint(int(lower), int(upper))
  print(str(num1) + " / " + str(num2) + " =")
  answer = round(float(num1) / float(num2), 1)
  user_answer = float(input())
  if round(user_answer, 1) == answer:
    print("CORRECT")
  else:
    print("INCORRECT: Correct answer is " + str(answer))

  user_command = input("[ENTER] to continue or 'menu' to return to menu\n")
  if user_command == "menu":
    return 0
  else:
    return 4

welcome_text = "Welcome to mmath! Select 1-4: (type 'quit' to exit)"

menu_text = "  1 Addition\n"
menu_text += "  2 Subtraction\n"
menu_text += "  3 Multiplication\n"
menu_text += "  4 Division"

menu_options = {"1", "2", "3", "4"}

user_input = ""
state = 0

while user_input != "quit":
  if state == 0:
    print(welcome_text)
    print(menu_text)
    user_input = input()

    if user_input not in menu_options:
      print("'" + user_input + "' is not an option. Please select 1-4")
    elif user_input == "1":
      state = 1
    elif user_input == "2":
      state = 2
    elif user_input == "3":
      state = 3
    elif user_input == "4":
      state = 4
      
  elif state == 1:
    state = addition()
  elif state == 2:
    state = subtraction()
  elif state == 3:
    state = multiplication()
  elif state == 4:
    state = division()









  





  