number1 = int(input("输入相机数量 ："))
number2 = float(input("输入销售单价 ："))
salary = 1500 + (200 + 0.02 * number2) * number1
print("工资是 ：{}".format(salary))
