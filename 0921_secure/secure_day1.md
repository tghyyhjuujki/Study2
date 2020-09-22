## EQST 1번

### ASP

아래와 같이 입력하고 아무 비밀번호 입력하면 정답 나옴

![image-20200921114219205](secure_day1.assets/image-20200921114219205.png)

![image-20200921114241622](secure_day1.assets/image-20200921114241622.png)

### JSP

![image-20200921131440091](secure_day1.assets/image-20200921131440091.png)



### PHP

주석만 #으로 바꿔주면 된다

![image-20200921120433443](secure_day1.assets/image-20200921120433443.png)

---

## 3번(주석 필터링)

### ASP, JSP, PHP

아이디 뒤에 틀린 것을 넣어준다

![image-20200921135920140](secure_day1.assets/image-20200921135920140.png)

### JSP, PHP

아이디 뒤에 맞는 것을 넣어줘도 된다.

![image-20200921140122756](secure_day1.assets/image-20200921140122756.png)



---



![image-20200921141933441](secure_day1.assets/image-20200921141933441.png)



![image-20200921143340839](secure_day1.assets/image-20200921143340839.png)





인젝션 대책

![image-20200921161206847](secure_day1.assets/image-20200921161206847.png)

---

## 4번 테이블 이름 찾기

파라미터마다 싱클쿼테이션을 넣어본다. 맨 뒤에 넣었을 때 500에러 난다

![image-20200921163719769](secure_day1.assets/image-20200921163719769.png)

다음과 같이 첫번째 글자 아스키코드값 몇인지 찾는다.

![image-20200921170021233](secure_day1.assets/image-20200921170021233.png)

 첫번째 답은 osec