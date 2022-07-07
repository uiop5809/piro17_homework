import random

num = 0
flag = False

def brGame():
    while True:
        try:
            cnt = int(input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : "))
            if cnt != 1 and cnt != 2 and cnt != 3:
                raise Exception("1, 2, 3 중 하나를 입력하세요")
            return cnt
        except ValueError:
            print("정수를 입력하세요")
        except Exception as e:
            print(e)

while True:
    # computer
    cnt = random.randint(1, 3)
    for i in range(num, num + cnt):
        print("computer :", i + 1)
        if i + 1 == 31:
            flag = True
            break
    num += cnt

    if flag == True:
        print("player win!")
        break

    # player
    cnt = brGame()
    for i in range(num, num + cnt):
        print("player :", i + 1)
        if i + 1 == 31:
            flag = True
            break
    num += cnt

    if flag == True:
        print("computer win!")
        break
