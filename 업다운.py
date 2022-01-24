import random
ran_num=random.randint(1,50)
count=0
while True:
    mine = int(input("숫자를 입력하세요:"))
    count += 1
    if mine>ran_num:
        print(f"{count}. {mine} 다운")
    elif mine<ran_num:
        print(f"{count}. {mine} 업")
    else:
        break

print(f"{count}. {mine} 정답입니다~\n시도 횟수는 {count}번입니다.")