n = int(input("Enter the number of students:"))
data = {}
subjects = ('physics','math','history')
for i in range(0,n):
	name = input('Enter the name of Students {}:'.format(i + 1))
	marks = []
	for x in subjects:
		marks.append(int(input("Enter marks of {}:".format(x))))
	data[name] = marks
for x,y in data.items():
	total = sum(y)
	print("{}'s total marks {}".format(x,total))
	if total < 120:
		print(x,"failed :(")
	else:
		print(x,"passed :)")
