# Python(07089)



## 자료구조

stack : LIFO. push할 때는 append() 사용

queue : FIFO

튜플(tuple) : 리스트와 같지만, 데이터의 변경을 허용하지 않는 자료구조

세트(set) : 데이터의 중복을 허용하지 않고, 수학의 집합연산을 지원하는 자료구조

딕셔너리(dictionary) : 키와 값 형태의 데이터를 젖아하는 자료구조, 키는 중복 허용안됨

collections : 위 기능들을 사용할 수 있게 지원하는 파이썬 내장모듈

---

## Stack

### 문자열 역순으로 출력하기

```python
x = input('영어 문자열 입력')
l = list(x)
print(l)	# ['a', 's', 'd', 'f', 'a', 's', 'd', 'f']

ret = []
for i in range(len(l)):
    ret.append(l.pop())

print(ret)	# ['f', 'd', 's', 'a', 'f', 'd', 's', 'a']
```



### pop 의 기능

```python
a =  [1,2,3,4,5]
a.append(10)
a.append(20)
print(a)	# [1, 2, 3, 4, 5, 10, 20]

a.pop(0)
print(a)	# [2, 3, 4, 5, 10, 20] 

a.pop(1)
print(a)	# # [2, 4, 5, 10, 20], pop을 delete처럼 쓸 수 있는 말도 안 되는..
```

---

## tuple

리스트와 같지만, 데이터의 변경을 허용하지 않는 자료구조

```python
t = (1,2,3)
print(t)		# (1, 2, 3)
print(t+t)		# (1, 2, 3, 1, 2, 3)
print(t*3)		# (1, 2, 3, 1, 2, 3, 1, 2, 3)
print(len(t))	# 3

t[1] = 5		# error, tuple은 데이터를 변경할 수 없다
```



---

## Set

 데이터의 중복을 허용하지 않고, 수학의 집합연산을 지원하는 자료구조

```python
s = set([1,2,3,4,5,1,2,3])	
print(s)		# {1, 2, 3, 4, 5}

s.add(1)
print(s)		# {1, 2, 3, 4, 5}, 중복이라 안들어감

s.remove(1)
print(s)		# {2, 3, 4, 5}

s.add(1)
print(s)		# {1, 2, 3, 4, 5}

s.update([11,12,13,14,15])
print(s)		# {1, 2, 3, 4, 5, 11, 12, 13, 14, 15}

s.discard(11)
print(s)		# {1, 2, 3, 4, 5, 12, 13, 14, 15}

s.clear()
print(s)		# set()
```



---

## Dictionary

키와 값 형태의 데이터를 젖아하는 자료구조, 키는 중복 허용안됨

```python
na_num = {'usa':'1', 'aus':'61', 'jap':'81','kor':'82', 'chi':'86'}
print(na_num.keys()) # dict_keys(['usa', 'aus', 'jap', 'kor', 'chi']), 출력이 []이렇게, 즉 리스트 형식으로 나오기 때문에 리스트 참조방식으로 접근가능

na_num['ger'] = 49
print(na_num.values()) # dict_values(['1', '61', '81', '82', '86', 49])
print(na_num.items())	# dict_items([('usa', '1'), ('aus', '61'), ('jap', '81'), ('kor', '82'), ('chi', '86'), ('ger', 49)]), 괄호: 리스트 안에 튜플이 들어가있다는 뜻

# 각 딕셔너리 값에 접근하는
# 방법1
for item in na_num.items():
    k, v = item 	# 언패키징, 키와 값을 따로 저장 가능
    print(item,k,v)
    
'''
('usa', '1') usa 1
('aus', '61') aus 61
('jap', '81') jap 81
('kor', '82') kor 82
('chi', '86') chi 86
('ger', 49) ger 49
'''

# 방법2, 처음부터 분리
for k, v in na_num.items():
    print(k,v)
    
'''
usa 1
aus 61
jap 81
kor 82
chi 86
ger 49
'''
```

---

## 9장 반복문

### 간단 예제

```python
c = 'Uasdf Sasdf Aasf'

for i in c:
    if i.isupper():
        print(i)
'''
U
S
A
'''

# 첫번째인자 = 시작값, 두번째인자 = 중지값
print(list(range(1,5)))		# [1, 2, 3, 4]
print(list(range(1,10)))	# [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(5,10)))	# [5, 6, 7, 8, 9]
print(list(range(0,50, 4)))	# [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48]

# 1~100까지 합
t = 0
for i in range(1,101):
    t+=i
print(t)		# 5050
```



### 중첩리스트

```python
e = [[1,2],[3,4],[5,6]]

for i in e:
    print(i)

for i in e:
    for j in i:
        print(j)
        
'''
[1, 2]
[3, 4]
[5, 6]
1
2
3
4
5
6
'''
```



## continue

```python
s = 'c3h7'
t = 0
cnt = 0

for i in range(len(s)):
    if s[i].isalpha():
        continue
    t += int(s[i])
    cnt+=1

print(t,cnt)		# 10 2
```



## 9장 연습문제

```python
# 1 한줄에 하나씩 출력
c = [1,2,3,4,5,6]

for i in range(len(c)):
    print(c[i])
    
# 2 한줄에 여러개
for i in range(len(c)):
    print(c[i],end=' ')		# 1 2 3 4 5 6
    
# 3 c 안바뀌고 c의 값 +1 된 값을 temp에 저장
temp=[]
for i in c:	
    temp.append(i+1)

print(c)			# [1, 2, 3, 4, 5, 6]
print(temp)			# [2, 3, 4, 5, 6, 7]

# 7 리스트 값 모두 더하기
t = 0
for i in range(len(c)):
    t+=c[i]

print(t)		# 21

#10 1부터 10 내림차순 출력
for i in range(10,0,-1):
    print(i,end=' ')		# 10 9 8 7 6 5 4 3 2 1 

# 11 2부터 22까지 합과 평균
t=0
cnt=0
for i in range(2,23):
    t+=i
    cnt+=1
    
print(t)		# 252
print(cnt)		# 21
print(t/cnt)	# 12.0

# 13 별그리기1
temp=''
for i in range(7):
    temp+='T'
    print(temp)
    
# 14 별그리기2
temp=''
for i in range(7):
    for j in range(0,7-i):
        print(' ',end='')
    temp+='T'
    print(temp)
# 파이썬은 더 쉡게 가능
for i in range(1,8):
    print(' '*(7-i),'T'*i)
    
# 15 별그리기 while로
temp=''
i=0
j=7
while i<7:
    while j>0:
        j-=1
        print(' ',end='')
    i+=1
    j=7-i
    temp+='T'
    print(temp)
```



### lambda

함수의 이름 없이, 함수처럼 사용할 수 있는 익명의 함수

```python
def f(x,y):
    return x+y
f(1,2)		# 3

f = lambda x, y: x+y	# 위 함수를 람다식으로 표현. : 기준으로 앞은 변수, 뒤는 할 동작
f(1,2)		# 3
```



### **번외(중요)

```python
s = {}
s['u1'] =[100,90,80]
s['u2'] =[99,99,99]
s['u3'] =[88,88,88]
s['u4'] =[77,77,77]
# 총점 평균 석차

def show():
    for user in s:
        temp = s[user]
        if len(temp) < 5 :
            t = s[user][0]+s[user][1]+s[user][2]
            avg = t/3
            temp.extend([t,avg])    # extend는 순서대로 값을 넣고, append 쓰면 한 덩어리 그대로 넣는다

    # newList = s.items()         # items로 넣으면 i[0]은 key, i[1]은 value. items는 반환값이 리스트
    newList = sorted(s.items(), key = lambda u: u[1][3], reverse=True)
    # 여기가 제일 중요한데, lambda로 u변수를 선언하고 u에서 총점에 해당하는 값을 reverse로 정렬해서 newList에 저장. 여기서 총점을 key로 놓고 정렬이 가능해진다!
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
        cmd = int(input('1) 성적입력 2) 성적출력 3)성적조회 4) 종료 ->'))
    except:
        print('명령어는 1 ~ 4 사이의 숫자만 입력해주세요')
        continue

    if cmd == 1:
        # 입력조건 : 이름 국어 영어 수학, 각 과목은 0 ~ 100점
        try :
            while True:
                # 만약 여기서 ,(쉼표) 기준으로 나누고 싶으면, 
                # userData = input('성적을 입력하세요. (이름,국어,영어,수학) -> ')
                # data = userData.split(',')
                u = str.split(input('[ 이름 국어 영어 수학 ] 형식으로 입력'))
                if len(u) != 4 or int(u[1]) > 100 or int(u[2]) > 100 or int(u[3]) > 100 or int(u[1]) < 0 or int(u[2]) < 0 or int(u[3]) < 0: raise Exception
                else:
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
    else:
        quit()
        
'''
현재 등록자 수 : 4
1) 성적입력 2) 성적출력 3)성적조회 4) 종료 ->2
--------------------------------------------------
이름    국어    영어    수학    총점    평균
--------------------------------------------------
u2       99     99      99      297     99.000000
u1       100    90      80      270     90.000000
u3       88     88      88      264     88.000000
u4       77     77      77      231     77.000000
'''
```

---

## 11장

### 연습문제

```python
# 1

```

