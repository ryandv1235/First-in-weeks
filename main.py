import random

Family = ["Ryan", "Laura", "Erwin", "Peggy"]

for x in Family:
	print(x)

notGuessed = True
maxBound = 5

while notGuessed:
	userInput = input("Raad een getal tussen 0-5")
	NumberToGuess = random.randint(0, 5)
	print(NumberToGuess)
	if userInput.isdiggit():
		if(userInput == NumberToGuess):
			print("You won!")
			notGuessed = False
			

