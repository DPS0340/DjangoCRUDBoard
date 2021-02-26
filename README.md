# KPU C크릿쥬쥬 프로젝트 - 게시판 백엔드(Django)

![GitHub](https://img.shields.io/github/license/DPS0340/DjangoCRUDBoard?style=for-the-badge) ![Website](https://img.shields.io/website?down_color=grey&style=for-the-badge&up_color=blue&up_message=online&url=https%3A%2F%2Fdjangocrudboard.ml%2Fstatus)

## 설명
### 게시판
간단한 포럼 기능을 할 수 있는 게시판 프로젝트의 **백엔드 서버** 깃허브입니다.\
로깅(logging)과 모니터링 기능을 붙이고 CI/CD 파이프라인을 구성하였습니다.\
React 프론트엔드 깃허브는 [이곳](https://github.com/Front-end-PJ/Forum_Front_end)에서 확인 가능합니다.

HTTP API 방식으로 JSON을 결과값으로 출력합니다.

[스터디 자료 velog](https://velog.io/@dps0340/KPU-C%ED%81%AC%EB%A6%BF%EC%A5%AC%EC%A5%AC-%EC%8A%A4%ED%84%B0%EB%94%94-%EC%9E%90%EB%A3%8C)

## 로컬 설정 가이드

### 

### 실행
```
docker-compose stop
docker-compose up --build
```

### 환경 변수 설정
```
'Django_secret_key': 시크릿 키, 온라인 등에서 생성 가능

'BOARD_DEBUG': 디버깅 상태인가 나타내는 변수, 프로덕션에서는 설정 X
```

## 아키텍처
![Architecture](https://user-images.githubusercontent.com/22572874/108958313-24e45000-76b6-11eb-8415-aa7a7dc6d0ac.png)

## 사용 스택
|분류|기술|
|------|---|
|배포환경|AWS Lightsail Ubuntu 20.04 LTS, Docker, Docker-compose|
|개발|Python, Django|
|의존성 관리|Pipenv|
|CI/CD|Github Actions, AWS Codedeploy, Shellscrpit|
|프론트엔드|React.js, Redux|
|백엔드|Nginx, Gunicorn, Django|
|데이터베이스|Docker-compose 상의 PostgreSQL|
|로깅(logging)|Elasticsearch, Logstash, Kibana, Filebeat |
|모니터링|Grafana, Prometheus|

## 데모
TODO

## 팀원

| 이름   | 학과         | 역할 | 소개 페이지                                         |
| ------ | ------------ | ---- | --------------------------------------------------- |
| 이지호 | 컴퓨터공학과 | 백엔드, 도커라이즈, 로깅, 모니터링, CI/CD | [개인 프로필로 이동](https://github.com/DPS0340) |
| 박근우 | 메카트로닉스공학과 | 백엔드, 도커라이즈 | [개인 프로필로 이동](https://github.com/Gnu-Kenny) |
| 장동현 | 메카트로닉스공학과 | 프론트엔드 |  [개인 프로필로 이동](https://github.com/ww8007) |
| 이하늘 | 메카트로닉스공학과 | 프론트엔드 | [개인 프로필로 이동](https://github.com/oldsalao) |
| 한승욱 | 컴퓨터공학과 | 백엔드, 도커라이즈, 모니터링 | [개인 프로필로 이동](https://github.com/SeungWookHan) |    

## 데이터베이스 모델링

![Database](https://user-images.githubusercontent.com/22572874/108862105-44866480-7633-11eb-8ca5-dece747862d8.png)
- 세부 설명(TODO)

## API

Postman으로 문서화 하였습니다.

[API  링크](https://documenter.getpostman.com/view/4929660/TVsxC6r1)

## PORTS

80: 디버그 서버 API, 릴리즈 서버는 443 포트로 리다이렉트

443: 릴리즈 서버 API 포트로 사용

5000: grafana

5005: prometheus
