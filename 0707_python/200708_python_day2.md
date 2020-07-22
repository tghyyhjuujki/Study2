# Python(0708)

## 6장 모듈화

### \_\_name__ , \_\_main__

왜 쓰는가? >> https://hyoje420.tistory.com/45

 https://madplay.github.io/post/python-main-function

import 했을 때 실행할 함수를 선별하기 위해 사용



### from

```python
from os import test # test라는 이름의 함수가 다른 모듈에도 있을 가능성이 있으므로 from을 붙여 정확히 어떤 파일인지 명시해 충돌을 방지한다
```



---

## 7장 메서드

### str 객체

```python
str.center('asdf', 26) # 26개의 칸에서 문자열을 가운데 위치시킴
str.count('asdf asdf asdf asdf', 'asdf') # asdf몇번 들어가 있는지 카운트
str.capitalize('asdf') # 맨 앞 글자 대문자로

s = 'Eighty percent of $ucce$$ is $howing up'
s = s.replace('$', 's') # $를 s로 교체
```

---

## 8장 list

시퀀스 자료형 : 여러 데이터를 하나의 변수에 할당하는 기법(다양한 자료형 포함 가능)



### 강력한 split기능 제공

```python
colors = ['red','blue','green','black','red','blue','green','black']
print(colors[0:6])
print(colors[0:5])
print(colors[5:])
print(colors[-8:]) # -8부터 카운트 한다는 뜻, -1은 7번 인덱스에 있는 black, -2는 6번 인덱스에 있는 green

''' 
결과
['red', 'blue', 'green', 'black', 'red', 'blue']
['red', 'blue', 'green', 'black', 'red']
['blue', 'green', 'black']
['red', 'blue', 'green', 'black', 'red', 'blue', 'green', 'black']
'''
```



### 연산기능 제공

```python
color1 = ['red', 'blue', 'green']
color2 = ['orange', 'black', 'white']
total = color1 + color2
print(total)

# ['red', 'blue', 'green', 'orange', 'black', 'white'] 출력


# 다음과 같이 쪼개기 가능
c1,c2,c3,c4,c5,c6 = total
print(c1)
print(c2)
print(c3)
print(c4)
print(c5)
print(c6)

'''
출력
red
blue
green
orange
black
white
'''

# 곱하기 가능
print(color1*2) # ['red', 'blue', 'green', 'red', 'blue', 'green']

# in 연산자
print('black' in color2) # true 출력
```



### 리스트 메서드

```python
a = [1,2,3,4,5]
a.append(10)

b = [100,200,300]
a.extend(b)

print(a)

print(a.pop())
print(a)

'''
출력
[1, 2, 3, 4, 5, 10, 100, 200, 300]
300
[1, 2, 3, 4, 5, 10, 100, 200]
'''
```



### 이중리스트

```python
life = [
    ['c',76.5],
    ['u',75.5],
    ['m',72.2]
]

c1, c2, c3 = life
print(c1)

# ['c', 76.5] 이 출력된다 (언패킹)
```

---



## 자료구조

stack : LIFO

queue : FIFO

튜플(tuple) : 리스트와 같지만, 데이터의 변경을 허용하지 않는 자료구조

세트(set) : 데이터의 중복을 허용하지 않고, 수학의 집합연산을 지원하는 자료구조

딕셔너리(dictionary) : 키와 값 형태의 데이터를 젖아하는 자료구조, 키는 중복 허용안됨

collections : 위 기능들을 사용할 수 있게 지원하는 파이썬 내장모듈