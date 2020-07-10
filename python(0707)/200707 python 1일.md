# Python(0707)

확장자는 py

파이썬 실행하는 네가지 방법

1. 프롬프트
2. vscode
3. terminal에서 파일 실행
4. 주피터

```python
def convert(f): # f는 parameter
    return(f-32)*5/9
convert(212) # 212는 argument
```

```python
pow(a,b) # a의 b승
abs(a) # 절대값
round(a,b) # a를 소수점 b까지 출력
a//b # 정수 나눗셈
3**6 # 3의 6승
--5 # 양수 5
a^b # xor 연산자
```

```python
# 다음과 같이 {}안에 format을 넣어서 표현할 수 있다.
print('{}의 총점{}'.format(name,sum(int(kor), int(eng), int(mat))))
```



```python
def x(d1: int, d2:int) -> int: # d1, d2를 int형으로 명시했고 반환형을 int로
```



## 텍스트처리

```python
len('asdf') # 4, 문자 개수를 반환, int, float의 길이는 읽을 수 없다
'asdf'+str(7)+'asdf' # 'asdf7asdf'
'asdf{}''asdf'.format(7) # 'asdf7asdf'
'asdf'*5 # 'asdfasdfasdfasdfasdf'

n = '''one
two
three'''
print(n)

one
two
three
#띄어쓰기 된 상태로 출력된다

b='asdf'
a in b # true, b안에 a라는 값이 들어가 있나
```

