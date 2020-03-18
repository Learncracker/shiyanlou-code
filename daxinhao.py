'''     上尖形
row = int(input("Enter the number of rows: "))
n = 0
while n <= row:
	x = "*" * n
	print(x)
	n += 1 
'''
# 下尖倒置
row = int(input("Enter the number of rows: "))
n = row
while n >= 0:
	x = "*" * n
	y = " " * (row - n)
	print(y + x)
	n -= 1 
