# 用户输入的语法
# 等待用户输入,接受存变量
# 数据类型字符串
# password = input("请输入密码: ")
# print(f'您输入的密码是{password}')
# print(type(password))

# 转换数据类型
"""
int(x[,base])
float(x)
str(x)
eval(str) 计算python有效表达式并返回一个对象
"""
# int 转换
# num = input('请输入数字：')
# print(int(num))
# print(type(int(num)))

# float 将数据转换成浮点型
num1 = 1
str1 = '10'
print(type(float(num1)))
print(float(num1))

# tuple() 将一个序列转换成元祖
list1 = [10, 20, 30]
print(tuple(list1))

# list() 将一个序列转换沉列表
t1 = (100, 200, 300)
print(list(t1))

# eval() 计算再字符串中有效python表达式，并返回一个对象
str2 = '1'
str3 = '1.1'
str4 = '(1000, 2000, 3000)'
str5 = '[1000, 2000, 3000]'
print(type(eval(str2)))
print(type(eval(str3)))
print(type(eval(str4)))

