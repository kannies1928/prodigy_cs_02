import random
number=random.randint(1 , 100)
attempts =0
print("welcome to the number guessing game !")
print("i have chosen a number between 1 to 100 ")
 
while True:
   guess=int(input("enter your guess: "))
   attempts += 1
   if guess<number:
     print("too low!try again")
   elif guess>number:
     print("too high!try again")
   else :
     print("congraulations!you guseed a number")
     print("number of attempts:",attempts)
     break
