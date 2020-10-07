XSS 1, 2번 답

![image-20200923113908389](secure_day3.assets/image-20200923113908389.png)

3번 답

![image-20200923154040674](secure_day3.assets/image-20200923154040674.png)



---



## CSRF

1번

1. 일반 사용자로 로그인 후 csrf 공격코드 있는 게시물 작성
2. 권한 변경 시도해봄
3. 관리자로 로그인 후 게시물 열람
4. 다시 일반 사용자로 로그인하면 권한상승되어있음



권한 변경 시도

![image-20200923154544981](secure_day3.assets/image-20200923154544981.png)

변경 불가능 뜸

![image-20200923154722546](secure_day3.assets/image-20200923154722546.png)



다음과 같이 버프스윗으로 권한변경하는 코드 확인 가능

![image-20200923154628522](secure_day3.assets/image-20200923154628522.png)



버프스윗을 통해 게시글 작성시 다음과 같이 이미지 공격코드 삽입

![image-20200923154432494](secure_day3.assets/image-20200923154432494.png)

관리자로 로그인하고 게시글 열람

![image-20200923154803067](secure_day3.assets/image-20200923154803067.png)



다시 일반사용자로 로그인하면 권한 상승되어 있음

![image-20200923154847106](secure_day3.assets/image-20200923154847106.png)

---



## SSRF

CSRF는 클라이언드 사이드이고, SSRF는 서버 사이드이다.

![image-20200923160639922](secure_day3.assets/image-20200923160639922.png)



![image-20200923160934873](secure_day3.assets/image-20200923160934873.png)



1번문제

![image-20200923164651634](secure_day3.assets/image-20200923164651634.png)

로그인 후 공지사항 업데이트 부분에서 프록시 켜야함. 그리고 file 부분에 문제에서 제시한 주소 넣으면

![image-20200923164631837](secure_day3.assets/image-20200923164631837.png)

![image-20200923164805165](secure_day3.assets/image-20200923164805165.png)



다음과 같이 db정보 탈취가 가능하다

![image-20200923164836885](secure_day3.assets/image-20200923164836885.png)





2번

사진 확인하기를 누르면 서버에서 이미지를 가져와서 base64로 인코딩한 후 보여줌. 이를 이용해서 SSRF 공격한다

![image-20200923173855495](secure_day3.assets/image-20200923173855495.png)



admin_login.php 를 프록시에서 보면 다음과 같이 나온다

![image-20200923174229942](secure_day3.assets/image-20200923174229942.png)

이 코드는 현재 base64로 인코딩 되어있기 때문에 decoder로 가서 디코딩해준다

![image-20200923174344768](secure_day3.assets/image-20200923174344768.png)

vscode에서 확인해보면 admin의 아이디와 비밀번호를 알 수 있다.

![image-20200923174444537](secure_day3.assets/image-20200923174444537.png)

이제 db정보를 찾아야 한다. 맨 위에서 아래와 같은 php 파일을 찾을 수 있다. 사실 php 파일 모두 열어봐야한다.

![image-20200923174542971](secure_day3.assets/image-20200923174542971.png)

include/common/declare.php를 확인해보면, 아래 파일들을 확인할 수 있고

![image-20200923175139098](secure_day3.assets/image-20200923175139098.png)

![image-20200923175146213](secure_day3.assets/image-20200923175146213.png)

그럼 다시 class.php를 털면

![image-20200923175334999](secure_day3.assets/image-20200923175334999.png)

db정보를 확인할 수 있다.

![image-20200923175405345](secure_day3.assets/image-20200923175405345.png)