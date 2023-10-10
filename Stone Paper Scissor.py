import random
import ctypes

# Function to print text in bold
def print_bold(text):
    kernel32 = ctypes.windll.kernel32
    kernel32.SetConsoleTextAttribute(kernel32.GetStdHandle(-11), 7)
    print(text)
    kernel32.SetConsoleTextAttribute(kernel32.GetStdHandle(-11), 15)

b = input("Your turn: Stone(1) Paper(2) Scissor(3)\n ")

if b == '1':
    print("__________ You chose Stone __________")
elif b == '2':
    print("__________ You chose Paper __________")
elif b == '3':
    print("__________ You chose Scissor __________")
else:
    print("Invalid input. Please enter 1, 2, or 3.")
print  ("**************************************************************************************")
randno = random.randint(1, 3)
print("My turn: Stone(1) Scissor(2) Paper(3)")
if randno == 1:
    print("__________ Stone __________")
elif randno == 2:
    print("__________ Paper __________")
else:
    print("__________ Scissor __________")
if b == randno:
    print("It's a tie")
elif (randno == 1 and b == '3') or (randno == 2 and b == '1') or (randno == 3 and b == '2'):
    print_bold("__________ You lose __________")
else:
    print_bold("__________ You win __________")