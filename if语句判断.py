# age = int(input('请输入您的年龄：'))
#
# if age >= 18:
#     print(f'您的年龄是{age},已经成年，可以上网')
# else:
#     print(f'您的年龄是{age},未成年，请自行回家写作业')
#
# print('关闭系统')

age = int(input('请输入您的年龄：'))

#童工
if age < 18:
    print(f'您输入的年龄是{age},合法')
# 18-60 合法
elif (age >= 18) and (age <= 60):
    print(f'您输入的年龄是{age},合法')
#大于60 退休
elif age > 60:
    print(f'您输入的年龄是{age},退休年龄')


money = 1
seat = 1

if money == 1:
    print('土豪 请上车')
    if seat == 1:
        print('有空座，坐下了')
    else:
        print('没有空座，站着等。。。')
else:
    print('朋友，没带钱')
    