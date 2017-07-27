# coding=utf-8
import random

secret_number = random.randint(1, 20)
print('１から２０までの数を当ててください。')

# 当たるまで聞く
while True:
    print('数を入力してください。')
    guess = int(input())

    if guess < secret_number:
        print('小さいです')
    elif guess > secret_number:
        print('大きいです')
    else:
        break

print('大当たり')
