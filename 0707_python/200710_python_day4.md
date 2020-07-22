# Python(0710)

---

## 10장 파일 입출력



### 파일 읽기

먼저 file_example.txt 만들어준다

```
First line of text
Second line of text
third line of text
한글테스트
```



이제 불러온다

```python
import os
cp = os.getcwd()			# 현재 경로 cp에 저장
os.chdir(cp+'\\day4')		# 경로 바꿔주는것, eroor2 떴는데 경로가 달라서 그랬다.

# file_example.txt생성해주고 오류 생겨도 해제할 수 있게 with 사용
with open('file_example.txt','r', encoding='utf-8') as file:
    print(file)
    contents = file.read()
    
print(contents)
file.close()	# 사용하고 나서 닫아줘야한다

'''
First line of text
Second line of text
third line of text
한글테스트
'''
```



### redalines, readline

```python
# 만약 read 대신 readlines 사용하면 아래와 같이 출력
['First line of text\n', 'Second line of text\n', 'third line of text\n', '한글테스트']

# 만약 read 대신 readline 사용하면 아래와 같이 출력
First line of text
```



### 예제

아래에서 22부터 아래 수를 더하고 싶다

```
Coloured fox fur production, HOPEDALE, Labrador, 1834-1842
#Source: C. Elton(1942) "Voles, Mice and Lemmings", Oxford Univ. Press
#Table 17, p.265--266
  22
  29
   2
  16
  12
  35
   8
  83
 166
```



```python
import os
os.chdir(os.getcwd()+'\\day4')

with open('hopedale.txt', 'r') as hopedale_file:
    hopedale_file.readline() # 한줄 건너띄우고

    data = hopedale_file.readline().strip()
    while data.startswith('#'):
        data = hopedale_file.readline().strip()	# 주석이 나오면 그 다음줄 저장

    total_pelts = int(data)		# 현재 data에는 22가 저장되어있다

    for data in hopedale_file:
        total_pelts += int(data.strip())

print("Total number of pelts :", total_pelts)
```



### 인터넷 파일 불러오기

```python
import urllib.request
import os
os.chdir(os.getcwd()+'\\day4')

url = 'https://robjhyndman.com/tsdldata/ecology1/hopedale.dat'
with urllib.request.urlopen(url) as webpage:
  for line in webpage:
    line = line.strip()
    line = line.decode('utf-8')
    print(line)
```



여기에서 숫자만 나오게 해서 더하는 것은

```python
import urllib.request
import os
os.chdir(os.getcwd()+'\\day4')
total_pelts=0
url = 'https://robjhyndman.com/tsdldata/ecology1/hopedale.dat'
with urllib.request.urlopen(url) as webpage:
    for line in webpage:
        line = line.strip()
        line = line.decode('utf-8')
        print(line)

        if line.startswith('#'):	# 주석 건너뛰고
            continue
        
        try:
            total_pelts += int(line)
        except:
            continue				# 에러 떠도 건너뛴다

print("Total number of pelts :", total_pelts)

```

---

## 파일 쓰기

```python
import os
os.chdir(os.getcwd()+'\\day4')

file = open('my_recioe.txt', 'w', encoding='utf-8') # 인코딩 안하면 깨짐
print(type(file))

text="""* 라면 레시피
1. 물을 끓인다.
"""

file.write(text)
file.close()
```



만약 w를 a(append)로 바꾸면

```python
file = open('my_recioe.txt', 'w', encoding='utf-8') 
# 누적된다
'''
* 라면 레시피
1. 물을 끓인다.
* 라면 레시피
1. 물을 끓인다.
'''
```

---

### StringIO를 이용한 파일 읽기

```python
from io import StringIO
i = '1.3 3.4\n2 4.2\n-1 1\n'
print(i)

infile = StringIO(i)    # 일반 텍스트 입력을 파일입출력처럼 처리할 수 있다.
print(infile.readline())
infile.readline()		# 한줄 띄어준다
print(infile.readline())

'''
1.3 3.4
2 4.2
-1 1

1.3 3.4
		
-1 1
'''
```

---

### 10장 연습문제

```python
# 1번 파일 불러오고 그 데이터의 백업파일을 .bak확장자로 저장
import os
os.chdir(os.getcwd()+'\\day4')

contents=''
with open('file_example.txt','r', encoding='utf-8') as file: # 불러오고
    contents = file.read()

fileWrite = open('file_example.bak', 'w', encoding='utf-8')
fileWrite.write(contents)	# 저장

file.close()
fileWrite.close()

# 2번 원자이름 번호 원자량을 리스트로 저장
import os
os.chdir(os.getcwd()+'\\day4')

with open('metal.txt','r', encoding='utf-8') as file:
    for line in file:
        li = line.split()
        print(li)
```



### 번외, 3일차 성적입출력 변경 4,5번에 파일 저장 불러오기 추가, 6번에 csv파일작업 추가

현재 경로에 문제가 있다 수정해보자

```python
from typing import List
import report
import os
#os.chdir(os.getcwd()+'\\day3')
s = {}
# s['u1'] =[100,90,80]
# s['u2'] =[99,99,99]
# s['u3'] =[88,88,88]
# s['u4'] =[77,77,77]
# 총점 평균 석차
'''
이름 ,총점, 평균만을 표시하는 report.csv파일을 생성하시오
ex)
이름, 총점, 평균
u1, 270...
u2, 270...
'''
def run_s() -> List[str]:
    for user in s:
        temp = s[user]
        if len(temp) < 5 :
            t = s[user][0]+s[user][1]+s[user][2]
            avg = t/3
            temp.extend([t,avg])    # extend는 순서대로 값을 넣고, append 쓰면 한 덩어리 그대로 넣는다

    # newList = s.items()         # items로 넣으면 i[0]은 key, i[1]은 value. items는 반환값이 리스트
    newList = sorted(s.items(), key = lambda u: u[1][3], reverse=True)
    # 여기가 제일 중요한데, lambda로 u변수를 선언하고 u에서 총점에 해당하는 값을 reverse로 정렬해서 newList에 저장. 여기서 총점을 key로 놓고 정렬이 가능해진다!
    return newList

def show():
    newList = run_s()
    for i in newList:
        print(i[0], '\t', seper(i[1]))

def seper(data):
    ret=''
    for i in range(len(data)-1):
        ret += str(data[i]) + '\t'
    return ret + ("%2f" % (data[len(data) - 1]))    # 마지막 value만 소수 2번째자리로 출력


while True:
    print('현재 등록자 수 :', len(s))

    try:
        cmd = int(input('1) 성적입력 2) 성적출력 3)성적조회 4) 저장 5)불러오기 6)리포트 출력 9) 종료 ->'))
    except:
        print('명령어는 1 ~ 4 사이의 숫자만 입력해주세요')
        continue

    if cmd == 1:
        # 입력조건 : 이름 국어 영어 수학, 각 과목은 0 ~ 100점
        try :
            while True:
                u = str.split(input('[ 이름 국어 영어 수학 ] 형식으로 입력'))
                if len(u) != 4 or int(u[1]) > 100 or int(u[2]) > 100 or int(u[3]) > 100 or int(u[1]) < 0 or int(u[2]) < 0 or int(u[3]) < 0: raise Exception
                else:
                    print(u)
                    s[u[0]] = [int(u[1]), int(u[2]), int(u[3])]
                    break
        except Exception as ex:
            print('제대로좀')
            continue

    elif cmd == 2:
        print('-'*50)
        print('이름\t국어\t영어\t수학\t총점\t평균')
        print('-'*50)
        show()
    elif cmd == 3:
        search = input('검색할 유저를 입력')
        print(s[search])
    elif cmd == 4:
        with open('sung.dat', 'w', encoding='utf-8') as file:
            cal_s = run_s()
            for i in cal_s:
                name = i[0]
                score = i[1]
                file.write(name+',')
                for j in score:
                    file.write('{0},'.format(j))
                file.write('\n')
            print('++파일을 저장합니다')
    elif cmd == 5:
        print('++파일을 불러옵니다')
        with open('sung.dat', 'r', encoding='utf-8') as file:
            for line in file:
                li = line.split(',')
                s[li[0]] = [int(li[1]),int(li[2]),int(li[3]),int(li[4]),float(li[5])]

    elif cmd == 6:
        dir = os.path.dirname(os.path.realpath(__file__))
        # infile = dir + '/sung.dat'
        infile = os.getcwd()+'/sung.dat'
        outfile = dir + '/report.csv'
        report.generate_report(input_file=infile, output_file=outfile)
        print('리포트 출력')
    elif cmd == 9:
        quit()
    else:
        continue
```

---

## 12장 연습문제

```python
# 2번 a 한번순회로 최소값 및 인덱스 구하기
c = [809, 834, 477, 478, 307, 122, 96, 102, 324, 476]
temp = c[0]
idx = 0
for i in range(len(c)-1):
    if temp > c[i]:
        temp = c[i]
        idx = i
print(temp,idx)

# b , 그런 기능을 가진 함수 만들기, 튜플로 반환해야함
c = [809, 834, 477, 478, 307, 122, 96, 102, 324, 476]

def min_index(li:list)->list:
    temp = li[0]
    idx = 0
    for i in range(len(li)-1):
        if temp > li[i]:
            temp = li[i]
            idx = i
    ret = (idx,temp)
    return ret
print(min_index(c))

# c True면 최소값, False면 최댇값 반환
c = [809, 834, 477, 478, 307, 122, 96, 102, 324, 476]
def min_index(li:list, bo:bool):
    temp = li[0]
    idx = 0
    if bo == True:
        for i in range(len(li)-1):
            if temp > li[i]:
                temp = li[i]
                idx = i
        print(temp,idx)
    else:
        for i in range(len(li)-1):
            if temp < li[i]:
                temp = li[i]
                idx = i
        print(temp,idx)

min_index(c, True)
min_index(c, False)
```

