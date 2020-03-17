a=0
while a in range(100):
    a = a + 1
    if a%7!=0 and a%10!=7 and a//10!=7:
        print(a)
    continue
