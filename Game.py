#So Today we are starting with the guessing game
from Ggamefunction import *
import time
print("\n\t\tWelcome to our Game;)")
time.sleep(0.5)
print("\n\t\tLoading Instructions",end="")
for i in range(1,6):
    print(".",end="")
    time.sleep(0.25)
time.sleep(1.5)
print("\n\t\tBefore we start there are some rules of the game\n\n\t\t1. Every turn costs $10")
time.sleep(1.5)
print("\n\t\t2. Once you commit to play a round there's no going back")
time.sleep(1.5)
print("\n\t\t3. After every turn you'll have the option to opt out")
time.sleep(1.5)
print("\n\t\t4. If you loose you cannot take your frustrations on the machine")
time.sleep(2)

while True:
    print("\n\t\tLet the game begins\n\t\tA. Login\tB.Signup")
    a=input("\n\t\tIf you are a new user please press B to Signup: ")
    if a.upper()=='A':
        login()
    if a.upper()=='B':
        signup()
