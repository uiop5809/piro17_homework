num = 0

while True:
    try:
        cnt = int(input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :"))
        if cnt != 1 and cnt != 2 and cnt != 3:
            raise Exception("1, 2, 3 중 하나를 입력하세요")
        break
    except ValueError:
        print("정수를 입력하세요")
    except Exception as e:
        print(e)