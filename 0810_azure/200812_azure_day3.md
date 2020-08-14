# Azure 200812

### docker

```sh
$ docker iamgems -f $(docker images -q) # 한꺼번에 이미지 지움

$ docker inspect [컨테이너ID, 태그] # 컨테이너 스펙 확인
```

빌드시 반드시 .(dot)을 붙여야 한다(dockerfile 경로지정, 현재디렉토리를 가르킴)

### DB 프레임워크 종류

oracle

mysql

mssql

sybase

카산드라

db2

sqlite

---

### ISMS (정보보호관리체계)

구축

1) 정보자산(식별, 분석, 중요도(CIA))

(서버, os,db,network etc..)

2) 위험분석 R = V x A x T + C (Asset이 0이면 Risk가 없기 때문에 곱연산)

식별, 분석, 대응

위험대응

- 회피

- 수용 : 받아들이긴 하지만 모니터링이 필요함

- 감소 : 보안위협에는 제거란 단어가 없음

- 전가 : 공유

3) 보호대책

관리적 : 보안 교육(보안 사고 60%가 사람떄문), 정책, 지침, 규정 제정 

기술적 : 시정조치

물리적 : 출입통제 시스템

---

### Hadoop

HDFS (하둡 파일 시스템)