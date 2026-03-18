number = 23

while True:
    guess = int(input("请输入一个数字："))
    if guess == number:
        print("恭喜你，猜对了")
        break
    elif guess < number:
        print("你猜的数字小了")
    else:
        print("你猜的数字大了")
print("游戏结束啦")
