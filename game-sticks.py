sticks = 21

print("There are 21 sticks, you can take 1-4 sticks each time ")
print("Whoever take the last stick will be the loser")

while True:
	print("sticks left ",sticks)
	if sticks == 1:
		print("You are the loser")
		break
	sticks_taken = int(input("Take sticks(1-4):"))
	if sticks_taken >= 5 or sticks_taken <= 0:
		print("wrong chioce")
		continue
	print("Computer took:",(5 - sticks_taken),"\n")
	sticks -= 5
