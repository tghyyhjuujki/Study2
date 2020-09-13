gm.zip을 가상머신에 옮기는 방법

 https://www.rejetto.com/hfs/?f=dl 다운로드 받고 공유를 한다

![image-20200902092813430](secure_day3.assets/image-20200902092813430.png)

/var/www/gm 디렉토리 만들고 bee box에서 wget으로 공유로 다운받자. 그리고 압축 해제

```sh
$ mkdri /var/www/gm
$ wget [위 주소]/gm.zip
$ unzip gm.zip
```

이제 mysql에 접속해서 gmshop db 만들어준다

```sh
$ mysql -u root -p # 비번은 bug
```

gmshop에 soulution.sql을 덤프한다.

```sh
$ mysql -u root -pbug gmshop < solution.sql
```

그리고 ip/gm경로로 접족하면 쇼핑몰이 뜬다



지금까지 배운것 정리하자면,

정보수집

- OSINT 이용 : 서브도메인-ip, 담당자 이메일, 노출된 페이지 정보를 수집

- 포트 스캔 : 불필요한 서비스 오픈 여부

- if)웹 -> 버전정보, 기본 설치된 서비스, 디렉터리 검사, 파일 검사

  시스템 -> 버전정보 확인, 보안설정 미흡

이번에는 포트스캔과 웹,시스템의 취약점을 점검할 것임

여기부터nmap NSE이다. 기본설정, 특정취약점 연결, 특정 스크립트는 취약점 분석, 공격코드 포함 하는 기능함.

kali linux 키자

```sh
$ nmap [bee box ip] # 포트스캔함, 이렇게 디폴트로는 잘 안씀
$ nmap -sV [bee box ip] # 버전정보까지 확인함, 여기부터 오래걸린다
```

버전을 알면 공격하기 쉬워짐

![image-20200902101624374](secure_day3.assets/image-20200902101624374.png)

다음과 같이 포트검색도 가능

```sh
$ nmap 192.168.20.0/24 -p80,8080
```



두개는 무슨차이 있을까?

```sh
$ $ nmap 192.168.20.0/24 # 전체 포트 보여줌
$ $ nmap 192.168.20.0/24 -p1-1000 # 1000아래 포트만 보여줌
```



다음과 같이 파일로 저장 가능, 왠만하면 원본은 xml로 저장하는게 좋음

```sh
$ $ nmap -sV 192.168.20.129 -oX result.xml
```

이걸 보고서로 뽑으려면, 다음과 같이 html로 변환후 firefox에서 열어주자

![image-20200902104223210](secure_day3.assets/image-20200902104223210.png)

굉장히 깔끔하게 나온다.

![image-20200902104310533](secure_day3.assets/image-20200902104310533.png)

다음 ㅂ명령어 로그인 허용 됐는지 여부까지 알 수 있다.

```sh
$ nmap -sV -cX 192.168.20.129
```

![image-20200902110745138](secure_day3.assets/image-20200902110745138.png)





아래 경로에서 nse 스크립트 확인 가능함. lua 기반

![image-20200902111050460](secure_day3.assets/image-20200902111050460.png)

https://nmap.org/nsedoc/categories/default.html여기서 구체적인 스크립트 확인 가능, default로 선택하면 주욱 나오는데, default에 다 포함된 것이다. 

이 두개는 공격이니까 충분히 테스트하고 사용하자.

![image-20200902111652262](secure_day3.assets/image-20200902111652262.png)

하나 사용해보자

![image-20200902111928762](secure_day3.assets/image-20200902111928762.png)

이거 사용하면 사이트의 title정보 가져올 수 있음

![image-20200902111913125](secure_day3.assets/image-20200902111913125.png)

---

위 기능들이 포함된 도구가 있다. sparta. 공격할 bee box ip를 적어주자

![image-20200902112327774](secure_day3.assets/image-20200902112327774.png)

위에 취약점 분석을 자동으로 해준다. 굉장히 편리하다 따로따로 쓸 필요 없이 한번에 스캔해준다.

![image-20200902113402256](secure_day3.assets/image-20200902113402256.png)



## 수동적 공격(취약점) - Passive Attack

디렉터리 검사/파일 검사

- 스파이더 (Spider)
  - 링크된 페이지를 크롤링하면서 진단
  - 연결된 페이지를 1회 방문을 함
  - 장애 요소는 많지 않음
  - 취약점) 관리자 페이지 접근? 디렉터리 리스팅 취약점(Index of 취약점) 버전정보 노출 여부...
  - 장애요소) 게시물의 submit 페이지 (게시물 작성....)

```sh
$ owasp-zap
```

실행하고 Help - Chech for update 에 들어가서 세가지 모듈 설치해준다

![image-20200902114347149](secure_day3.assets/image-20200902114347149.png)

여담으로 얘도 프록시다.

firefox 환경설정에 들어가서

![image-20200902114628410](secure_day3.assets/image-20200902114628410.png)

다음과 같이 설정

![image-20200902114716640](secure_day3.assets/image-20200902114716640.png)

스파이더 공격

![image-20200902132053268](secure_day3.assets/image-20200902132053268.png)

체크 해제

![image-20200902132011998](secure_day3.assets/image-20200902132011998.png)

알람

![image-20200902132249969](secure_day3.assets/image-20200902132249969.png)

기억할 것

수동적 공격 : 패턴이 안들어감

능동적 공격 : 공격 패턴이 들어감

<br/>

강제디렉터리 검사(Forced)

- 갖고 있는 사전파일을 각 대입
- 백업파일(zip, bak)
- 취약점) 관리자 페이지를 검색, index of 취약점, 백업파일, 인증처리 미흡페이지 등

![image-20200902132616409](secure_day3.assets/image-20200902132616409.png)



## 공격적 공격(취약점) - Active Attack

SQL Injection, XSS, LFI, PHP Injection......

---

admon 뚫기

1. 관리자 페이지 접근(접근 제어 미흡)
2. 비 암호화 통신 여부 확인(둘 중 하나는 되어있어야 함)
   - ssl 통신 여부 확인
   - 클라이언트 암호화 확인

3. 예측가능한 암호냐?

![image-20200902141709652](secure_day3.assets/image-20200902141709652.png)

burp suite 키고 포워드 한번만 누름

![image-20200902141750746](secure_day3.assets/image-20200902141750746.png)

send to intruder해주고 이동

payload position : 공격 패턴

cookie: 서버 입장에서는 전달되어 온 값, burp는 이걸 표시해 줌. 우리는 adminid, adminpwd 안에 아이디랑 비밀번호를 넣어 공격할 예정.![image-20200902145103243](secure_day3.assets/image-20200902145103243.png)

바꾸고

![image-20200902145334913](secure_day3.assets/image-20200902145334913.png)

아디 및 비번 넣을 입력

![image-20200902145322499](secure_day3.assets/image-20200902145322499.png)

각 5개씩 넣어서 총 25번 돌게 된다. 근데 전부 체크 되어 있어서 뭐가 답인지 모른다

![image-20200902145447801](secure_day3.assets/image-20200902145447801.png)

맞는 거는 이렇게 뜸 리스폰스에

![image-20200902145542049](secure_day3.assets/image-20200902145542049.png)

옵션에서 다음과 같이 설정

![image-20200902145635681](secure_day3.assets/image-20200902145635681.png)

다시 돌려주면 맞는거만 체크 해제되어있다

![image-20200902145719900](secure_day3.assets/image-20200902145719900.png)

off하면 뚫려있음

![image-20200902145838076](secure_day3.assets/image-20200902145838076.png)

---

## AstroGrep

파일에 text 있나 검색함, 경로와 text를 넣고 context line 5정도 놓고 검색. haad.php를 참조하는 모든 파일 보여줌. 매우 좋은 프로그램.

![image-20200902153019742](secure_day3.assets/image-20200902153019742.png)

<br/>

다음과 같이 셋팅하면 인증처리 안 된 놈들 보여줌

![image-20200902153240666](secure_day3.assets/image-20200902153240666.png)

파일을 주소창에 입력하면,

![image-20200902153522171](secure_day3.assets/image-20200902153522171.png)

다운로드 된다.

![image-20200902153545654](secure_day3.assets/image-20200902153545654.png)

---

## 인증처리 미흡(자바스크립트)

이번에는 리스폰스값을 수정할 것임. 회원가입에 들어가서 아무 값이나 입력하면 처리가 안된다. 서버에서 체크하는 것은 우리가 어떻게 할 수 없음.

![image-20200902154720222](secure_day3.assets/image-20200902154720222.png)

페이지 소스를 보고 다음 코드를 없애줄 것이다.

![image-20200902155045238](secure_day3.assets/image-20200902155045238.png)

회원가입에 인터셉터 온 해주자

![image-20200902155136039](secure_day3.assets/image-20200902155136039.png)

ㅇ

![image-20200902155151672](secure_day3.assets/image-20200902155151672.png)

forward 한번 누르면 페이지 소스가 나옴. jumin 검색해보자

![image-20200902155331751](secure_day3.assets/image-20200902155331751.png)

219줄까지 싹다 지우고

![image-20200902155415830](secure_day3.assets/image-20200902155415830.png)

아래와 같이 만든다

![image-20200902155437462](secure_day3.assets/image-20200902155437462.png)

forword 한번 더 해주고 회원가입 해보면, 아래와 같이 조작 가능. 체크 함수를 다 지워서 조작된 주민번호로 가능함

![image-20200902155700864](secure_day3.assets/image-20200902155700864.png)

이번에는 회원가입 창에서 변경해줄 것이다.

![image-20200902162100280](secure_day3.assets/image-20200902162100280.png)

send 아래는 이렇게만 남기자

![image-20200902162135009](secure_day3.assets/image-20200902162135009.png)

이제 대충 폼 작성하자.

![image-20200902162241359](secure_day3.assets/image-20200902162241359.png)

회원가입하고 로그인하면 된다.

![image-20200902162529282](secure_day3.assets/image-20200902162529282.png)

이제 82번 쇼핑몰 뚫어보자. 아래와 같이 남긴다.

![image-20200902164505926](secure_day3.assets/image-20200902164505926.png)

회원가입이 되었다.

![image-20200902164309714](secure_day3.assets/image-20200902164309714.png)

이 모든게 자바스크립트 단에서 처리해서 생긴 문제이다.

---

### 다른 사용자 게시물

- 1:1 문의게시판(비밀글) -> 취약) 보기, 수정, 삭제

대충 아무 게시물 만들어주자

![image-20200902171242600](secure_day3.assets/image-20200902171242600.png)

버프 스윗에서 확인해보면

![image-20200902171410763](secure_day3.assets/image-20200902171410763.png)

이렇게 나온다.

![image-20200902171345300](secure_day3.assets/image-20200902171345300.png)

여기서 idx를 바꾸면 다른 사람 글을 볼 수 있다!

![image-20200902171938735](secure_day3.assets/image-20200902171938735.png)

수정도 마찬가지

![image-20200902172054470](secure_day3.assets/image-20200902172054470.png)

응용해서 자유게시판의 비밀글을 털었다.

![image-20200902173931949](secure_day3.assets/image-20200902173931949.png)