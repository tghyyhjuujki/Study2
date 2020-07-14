import random

comNum = random.randrange(1, 100)
cnt = 0
# print(comNum)
while True:
    userNum = int(input('숫자를 입력하세요(1~100):'))

    if userNum < 1 or userNum > 100:
        print('1~100 사이의 숫자만 입력해 주세요.')
    else:
        cnt = cnt + 1 # cnt += 1
    
        if comNum > userNum:
            print('보다 큰 숫자를 입력해 주세요.')
        elif comNum < userNum:
            print('보다 작은 숫자를 입력해 주세요.')
        else: # comNum == userNum
            print('맞췄습니다')
            break # 근접해 있는 Loop 실행을 종료

# 정답을 맞추면, 여기로 실행위치가 이동됩니다. 
print('=====================')
print('COMUPYER NUMBER={}'.format(comNum))
print('축하합니다. 총 {} 번에 맞추었습니다.'.format(cnt))
if (cnt <= 3):
    print('천재입니다.'.center(30))
elif (cnt <= 7):
    print('보통입니다.'.center(30))
else:
    print('바보이군요...'.center(30))

