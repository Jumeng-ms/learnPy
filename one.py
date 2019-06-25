print('hello world');

a = 123
print(type(a))

b = 'one'
print(type(b))

c = 1.23
print(type(c))


a = 5
b = 8
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b) # 无条件舍去除法
print(a ** b) # a 的 b 平方

a = -3
b = 4
print(abs(a))   # abs()绝对值
print(max(a , b))     # 最大值
print(min(a , b))     # 最小值

a = 123
b = '456'
print(a + int(b))
print(str(a) + b)

'''
a = input();  #输入
print('a = ',a)

b = input('Your Name:') #输入提示
print('Your Name;',b)
'''

#循环 for 变量名称 in range（范围 X到Y）
for i in range(1,10):
    for j in range(1,10):
        print(i*j)
#从1-10 每次+2
for i in range(1,10,2):
    print(i)

#1-10 每次-3
for j in range(10,1,-3):
    print(j)

#猜数
ans = 29
for guessChance in range(0,3):
    guess = int(input())
    i = 2 - guessChance
    if ans == guess:
        print('Bingo!')
        break
    else:
        print('错误,还剩'+str(i)+'机会')
print('游戏结束')