import math
a = int(input("enter value of a :"))
b = int(input("enter value of b :"))
c = int(input("enter value of c :"))
d = b * b - 4 * a * c
if d < 0:
    print ("root are imaginary") 
else:
    root1 = (-b + math.sqrt(d)) / (2 * a)
    root2 = (-b - math.sqrt(d)) / (2 * a)
    print("root1={}  root2={}".format(root1,root2))
