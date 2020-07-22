# Python(0710)

---

## 13장 검색과 정렬



## 연습문제

```python
# 1번 선형정렬

#while
from typing import Any

def l_s(lst: list, value:Any) -> int:
    i = len(lst) -1
    while i != len(lst) and lst[i] != value:
        i-=1

    if i == len(lst):
        return -1
    else:
         return i
# for
from typing import Any

def l_s(lst: list, value:Any) -> int:
    i = 0
    for i in range(len(lst) - 1, 0, -1):
        if lst[i] == value:
            return i
    return -1
#sectinal
from typing import Any

def l_s(lst: list, value:Any) -> int:
    lst.insert(0, value)
    i = len(lst)-1

    while lst[i] != value:
        i-=1

    del lst[0]

    if i == len(lst):
        return -1 
    else:
        return i
# 5번 버블소트
def bubble_sort(lst: list):
    for h in range(len(lst)-1, 0, -1):
        for i in range(h):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
    print(lst)

bubble_sort([2,5,1,-3, 1, 1, 6, -4])
```



---



## 14장 OOP

attribute = property = feild = column = 속성

class = 설계 도면

instance = 실제 사용할 수 있는(설계도면에 따라 실체화 되어있는) 오브젝트를 인스턴스라 함

object = 모든 클래스의 루트 클래스



객체지향 3대특징

1. 상속 : 부모 클래스가 존재해야함
2. 다형성 : 오버로딩
3. 은닉 :  data를 숨김

보통 명사는 클래스, 동사는 메서드의 역할을 하게 프로그래밍한다.

---

### 메서드 재정의(오버라이딩)

```python
from typing import List, Any

class Book :
    def __init__(self, title: str, authors: List[str], publisher: str, isbn: str, price: float) -> None:
        self.title = title
        self.authors = authors[:]
        self.publisher = publisher
        self.isbn = isbn
        self.price = price

    def num_authors(self) -> int:
        return len(self.authors)

    def __str__(self) ->str: # 이 메서드 정의 안하면 밑에 print(python_book1)에서 주소값 호출됨. 오버라이딩(메서드 재정의)로 다른 결과 출력되게 바꿈
        return "title: {0}, Authors: {1}, publisher: {2}".format(self.title, "".join(self.authors), self.publisher)

    def __eq__(self, other: Any) -> bool:
        return isinstance(other, Book) and self.isbn == other.isbn

python_book1 = Book('practical', ['asdf', 'sdfg', 'dfgh'], 'bookshelf', '123123', 25.0)
python_book2 = Book('practical', ['asdf', 'sdfg', 'dfgh'], 'bookshelf', '123123', 25.0)
print(python_book1) # 재정의 하기 전에는 주소값 출력
print(python_book1.__str__()) # __str__ # 위 print와 같은거 출력함

print(python_book1 == python_book2) # __eq__를 정의하기 전에는 false가 출력되지만, 내용이 같은지 확인하는 메서드로 eq를 재정의한 순간부터 true로 출력된다
print(python_book1 == python_book1)
print(python_book2 == python_book2)
python_book3 = python_book1
print(python_book3 == python_book1) # __eq__가 재정의(오버라이딩) 되어있지 않을때 주소값이 같다고 출력된다.


# 만약 프롬프트에서 실행한다면,
>>> import book
>>> python_book1 = book.Book('practical', ['asdf', 'sdfg', 'dfgh'], 'bookshelf', '123123', 25.0)
>>> python_book2 = book.Book('practical', ['asdf', 'sdfg', 'dfgh'], 'bookshelf', '123123', 25.0)

# 그리고 print안에 있는 구문들만 써준다
```

---

### 14장 연습문제

```python
# 1번
from typing import List

class Country :
    def __init__(self, name: str, population: int, area: int) -> None:
        self.name = name
        self.population = population
        self.area = area

    def p_d(self)->float:
        return self.population/self.area

    def __repr__(self) -> str:
        return "Country({0}, {1}, {2})".format(self.name, self.population, self.area)

canada = Country('Canada', 34482779, 9984670)
print(canada.name)
print(canada.population)
print(canada.area)
print(canada.p_d())

print(canada)
```

