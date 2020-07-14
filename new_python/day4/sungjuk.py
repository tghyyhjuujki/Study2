from typing import List
import report
import os 

sungjuk = {}
# sungjuk['USER1'] = [100, 90, 80]
# sungjuk['USER2'] = [70, 85, 99]
# sungjuk['USER3'] = [45, 86, 90]
# sungjuk['USER4'] = [80, 85, 81] 
# 국어, 영어, 수학, 총점, 평균, 석차 
"""
이름, 총점, 평균만을 표시하는 report.csv 파일을 생성하시오.
ex)
이름,총점,평균
USER1,270,90.00
USER2,254,84.67
"""
def runSungjuk() -> List[str]:
    for user in sungjuk:
        temp = sungjuk[user] # [100, 90, 80] -> list 
        if len(temp) < 5:
            total = temp[0] + temp[1] + temp[2]
            avg = total / 3
            temp.extend([total, avg]) # [100, 90, 80, 270, 90]
    newList = sorted(sungjuk.items(), key=lambda u: u[1][3], reverse=True)
    return newList

def showSungjuk():
    newList = runSungjuk()

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
        cmd = int(input('1) 성적입력 2) 성적출력 3) 성적조회 4) 저장하기 5) 불러오기 6) 리포트출력 9) 종료 (1~9) -> '))
    except:
        print('** 명령어는 1~9 사이의 숫자만 입력해 주세요. **')
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
        with open('sungjuk.dat','w',encoding='utf-8') as file:
            calculatedSungjuk = runSungjuk()
            for element in calculatedSungjuk:
                _name = element[0]
                file.write(_name+',')
                _nums = element[1] # [100, 90, 80, 270, 90.0]
                for _number in _nums:
                    file.write("{0},".format(_number))
                file.write('\n')
            print('++ 파일에 저장 하였습니다.')
    elif cmd == 5:
        with open('sungjuk.dat','r',encoding='utf-8') as file:
            for line in file:
                # sungjuk['USER1'] = [100, 90, 80]
                _values = line.split(',')
                sungjuk[_values[0]] = [int(_values[1]), int(_values[2]), int(_values[3]), int(_values[4]), float(_values[5])]
            print('++ 파일을 읽어 왔습니다.')
    elif cmd == 6:
        dir = os.path.dirname(os.path.realpath(__file__))
        infile = dir + '/sungjuk.dat'
        outfile = dir + '/report.csv'
        report.generate_report(input_file=infile, output_file=outfile)
    elif cmd == 9:
        quit()
    else:
        print()