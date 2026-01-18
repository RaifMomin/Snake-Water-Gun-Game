import random
'''
**SNAKE WATER GUN GAME!**
snake = 1
water = -1
gun = 0

'''

computer = random.choice([1,-1,0])
youstr = input('Enter your number:(snake(s),water(w),gun(g) : ')
youdict ={"s":1,"w":-1,"g":0}
revdict = {1:"snake",-1:"water",0:"gun"}
you=youdict[youstr]
print(f"Your number is {revdict[you]} and computer number is {revdict[computer]}")
if you == computer:
    print("its a Draw!")
else:
   if(you == 1 and computer == -1):
       print("You Win!")
   elif(you == -1 and computer == 1):
       print("You Lose!")
   elif(you == 0 and computer == 1):
       print("You Lose!")
   elif(you == 1 and computer == 0):
       print("You Win!")
   elif(you == -1 and computer == 0):
        print("You Win!")
   elif(you == 0 and computer == -1):
        print("You Lose!")
   else:
       print("invalid input")
