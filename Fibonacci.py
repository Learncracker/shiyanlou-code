'''
a,b = 0,1
while b < 100:      
    print(b)     # 换行输出结果
    a,b = b,a+b
'''
a,b = 0,1
while b < 100:
    print(b,end=' ')      # 单行输出所有结果，即去除 print 内的换行处理
    a,b = b,a+b
print()                  # 注释掉改行，程序仍能正常输出，末尾多出 % ， 为什么？
