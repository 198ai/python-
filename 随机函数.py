import random

# 玩家输入
player = int(input('请出拳：0--石头；1--剪刀；2--布'))
computer = random.randint(0, 2)
#print(computer)
# 判断输赢
if((player==0) and (computer ==1)) or ((player == 1) and (computer ==2)) or ((player ==2) and (computer ==0)):
    print('玩家获胜，哈哈哈')
elif player == computer:
    print('平局，别走，再来一局')
else:
    print('电脑获胜')