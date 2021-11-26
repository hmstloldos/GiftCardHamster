#Hamster Gift Card Generator V1

#setup
import time
import random

#functions
def g(rolls):
	data = "qwertyuioplkjhgfdsazxcvbnm1234567890QWERTYUIOPLKJHGFDSAZXCVBNM"
	result = ""
	while rolls >= 1:
		c = random.choice(data)
		result = c + result
		rolls = rolls - 1
	return result

#interface
print("ig: @hamster.py")
print("What Giftcard You Want?")

tt = input("\nAmazon\nRoblox\nFortnite\nNetflix\nPlaystation\nSteam\nXbox\nMinecraft\n\n>")

t = tt.lower()
print("")
print("How many?")
nn = input(">")
print("")
n = int(nn)

if t == "minecraft":
	for x in range(n):
		print("")
		print(g(4)+"-"+g(4)+"-"+g(4))
		
if t == "playstation":
	for x in range(n):
		print("")
		print(g(4)+"-"+g(4)+"-"+g(4))
		
if t == "amazon":
	for x in range(n):
		print("")
		print(g(4)+"-"+g(6)+"-"+g(4))
		
if t == "netflix":
	for x in range(n):
		print("")
		print(g(4)+"-"+g(6)+"-"+g(4))
		
if t == "steam":
	for x in range(n):
		print("")
		print(g(4)+"-"+g(6)+"-"+g(5))
		
if t == "fortnite":
	for x in range(n):
		print("")
		print(g(5)+"-"+g(4)+"-"+g(4))
		
if t == "roblox":
	for x in range(n):
		print("")
		print(g(3)+"-"+g(3)+"-"+g(4))

if t == "xbox":
	for x in range(n):
		print("")
		print(g(5)+"-"+g(5)+"-"+g(5)+"-"+g(5)+"-"+g(5))
time.sleep(6)
print("Hamster © 2021.")
time.sleep(10)
print("Completed")
time.sleep(1000)