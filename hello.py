print('......欢迎进入游戏时间......')
temp = input('来猜猜我心里想的是哪个数字吧，qvq：')
guess = int(temp)
if guess == 2:
   print('你太聪明啦！ouo')
while guess != 2:
    if guess == 2:
       print('被你猜对啦！')
       break
    if guess > 2:
       guess = int(input('哎呀，大了大了！再来一遍吧：'))
    if guess < 2:
       guess = int(input('哎呀，小了小了！再来一遍吧：'))
print('没错，答案就是2！^_^')
