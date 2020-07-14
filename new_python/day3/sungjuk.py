sungjuk = {}
sungjuk['USER1'] = [100, 90, 80]
sungjuk['USER2'] = [70, 85, 99]
sungjuk['USER3'] = [45, 86, 90]
sungjuk['USER4'] = [80, 85, 81] 
# 국어, 영어, 수학, 총점, 평균, 석차 

def showSungjuk():
    for user in sungjuk:
        # total, average -> [100, 90, 80, 총점, 평균]
        temp = sungjuk[user] # [100, 90, 80] -> list 
        if len(temp) < 5:
            total = temp[0] + temp[1] + temp[2]
            avg = total / 3
            temp.extend([total, avg]) # [100, 90, 80, 270, 90]

    # newList = sungjuk.items() # (USER1, [100, 90, 80, 270, 90])
    newList = sorted(sungjuk.items(), key=lambda u: u[1][3], reverse=True)

    for user in newList:
        print(user[0], '\t', seperateGrade(user[1]))

def seperateGrade(data):
    result = ''
    for _num in range(len(data) - 1): # [70, 85, 99, 254]
        result += str(data[_num]) + '\t'
    
    return result + ("%.4f" % (data[len(data) - 1]))

while True:
    print('## 현재 등록자 수:', len(sungjuk))
    # 1~4 입력값만 허용 
    # 입력값을 int()로 casting 
    try: 
        cmd = int(input('1) 성적입력 2) 성적출력 3) 성적조회 4) 종료 (1~4) -> '))
    except:
        print('** 명령어는 1~4 사이의 숫자만 입력해 주세요. **')
        continue

    if cmd == 1:
        # 입력조건 1) 이름,국어,영어,수학
        # 입력조건 2) 각 과목의 점수는 0~100점 사이
        while True:
            try:
                userData = input('성적을 입력하세요. (이름,국어,영어,수학) -> ')
                data = userData.split(',')
                # len(data) = 4, data[0] = 이름, data[1] = 국어
                if len(data) != 4:
                    raise Exception
                else: # OK
                    kor = int(data[1])
                    eng = int(data[2])
                    mat = int(data[3])

                    # 각 과목이 0~100 사이의 점수인지 체크 
                    if kor < 0 or kor > 100:
                        raise Exception
                    if eng < 0 or eng > 100:
                        raise Exception
                    if mat < 0 or mat > 100:
                        raise Exception
            except Exception as ex:
                print("** 성적데이터를 정확하게 입력해 주세요.")
                continue
            else:
                print(data)
                # sungjuk['USER4'] = [80, 85, 81] 
                sungjuk[data[0]] = [int(data[1]), int(data[2]), int(data[3])]
                break

    elif cmd == 2:
        # 정보 출력
        print("#" * 50)
        print('이름\t국어\t영어\t수학\t총점\t평균')
        print("#" * 50)
        showSungjuk()
    elif cmd == 3:
        # 정보 조회 -> 출력
        searchUser = input('검색할 사용자명을 입력하세요=>')
        print(sungjuk[searchUser])
    elif cmd == 4:
        quit()
    else:
        print()