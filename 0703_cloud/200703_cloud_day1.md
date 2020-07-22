## 200703 클라우드



deploy : 배치, 어떤 어플리케이션을 설치하는 작업을 배치(deploy)한다고 함

Iaas : 인프라, AWS의 EC2를 예로 들 수 있음

Paas : 플래폼, OS와 미들웨어는 제공되므로 Application만 구축해주면 된다.

Heroku에 node를 띄우는 것을 예로 들 수 있음.



### node.js, heroku 이용해서 어플리케이션 배포하기

heroku 는 Paas로 Iaas인 AWS와 차이가 있다 그것 확인하기 위한 작업

node.js로 Hello World 어플리케이션 작성(소스 구글에서 대충 긁어옴)

```js
var http = require('http');
http.createServer(function (req, res) {
    res.writeHead(200, {'Content-Type': 'text/html'});
    res.end('Hello World');
}).listen(1337, '127.0.0.1');
console.log('Server running at http://127.0.0.1:1337/');
```



heroku가 exe로 설치 안될 떄,

```shell
$ npm install -g heroku
```



작업할 디렉토리로 이동해서

```shell
$ heroku login # heroku 로그인
$ git init
$ heroku git:remote -a my-first-heroku-jeonghoon # 주소 연결
$ npm init # 여기서 pakage.json 만듦
$ npm install express --save # save는 pakage.json에 저장한다는 의미
```



vscode에서 내용 수정

```shell
$ code package.json # 바로 code 열림
```



 script 안에 아래 추가해서 npm start 명령어로 실행

```js
"start":"node app.js",
```

```shell
$ npm start
```



깃에 올릴때 heroku는 살짝 다름

```shell
$ git add .
$ git commit -m "update"
$ git push heroku master
```



그리고 본인 heroku 주소로 들어가면 배포가 잘 된 것을 확인할 수 있다

![image-20200706092309632](images/image-20200706092309632.png)