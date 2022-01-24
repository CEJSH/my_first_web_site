import random



mine=int(input("하나를 선택하세요: 가위(0), 바위(1), 보(2) :"))
random_number=random.randint(0,2)
if random_number == 2 and mine == 2:
    print("컴퓨터는 보를 냈습니다.\n비겼습니다.")
elif random_number == 2 and mine == 1:
    print("컴퓨터는 보를 냈습니다.\n당신이 졌습니다.")
elif random_number == 2 and mine == 0:
    print("컴퓨터는 보를 냈습니다.\n당신이 이겼습니다.")
elif random_number == 1 and mine == 1:
    print("컴퓨터는 바위를 냈습니다.\n비겼습니다.")
elif random_number == 1 and mine == 0:
    print("컴퓨터는 바위를 냈습니다.\n당신이 졌습니다.")
elif random_number == 1 and mine == 2:
    print("컴퓨터는 바위를 냈습니다.\n당신이 이겼습니다.")
elif random_number == 0 and mine == 0:
    print("컴퓨터는 가위를 냈습니다.\n비겼습니다.")
elif random_number == 0 and mine == 2:
    print("컴퓨터는 가위를 냈습니다.\n당신이 졌습니다.")
elif random_number == 0 and mine == 1:
    print("컴퓨터는 가위를 냈습니다.\n당신이 이겼습니다.")
