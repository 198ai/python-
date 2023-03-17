"""
1,データ準備
"""
age = 18
weight = 75.5
stu_id = 1
stu_id2 = 1000
name = "雷声楽"
# 1、今年我的年龄是X岁 --整数 %d
print('我的名字是%s' % name)
# 2、我的名字是x -- 字符串 %s
print('我的名字是 %s' % name)
# 3、我的体重是X公斤 -- 浮点数 %f
print('我的体重是%.3f公斤' % weight)
# 4、我的学号是001
print('我的学号是%03d' % stu_id)
print('我的学号是%03d' % stu_id2)
# 5、我的名字是x，今年x岁了
print('我的名字是%s,今年%d' % (name, age))
print('我的名字是%s,明年%d岁了' % (name, age))

# 6、我的名字是x，今年x岁了，体重x公斤，学号是x
print('我的名字是%s,今年%d岁了，体重%.2f公斤，学号是%d' % (name, age, weight, stu_id))

# f'{表达式}'我的名字是x，今年x岁了 python 3.6以后的功能
print('我的名字是%s, 今年%s岁了' % (name, age))
print(f'我的名字是{name}, 今年{age}岁了')

