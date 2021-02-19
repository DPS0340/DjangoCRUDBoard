# KPU C크릿쥬쥬 프로젝트 - 게시판 백엔드(Django)

![GitHub](https://img.shields.io/github/license/DPS0340/DjangoCRUDBoard?style=for-the-badge) ![Website](https://img.shields.io/website?down_color=grey&style=for-the-badge&up_color=blue&url=http%3A%2F%2Fdjangocrudboard-env-2.eba-pncegi8j.ap-northeast-2.elasticbeanstalk.com%2Fstatus)

## 설명

React 프론트엔드가 개발 중인 게시판의 백엔드 서버입니다.

HTTP API 방식으로 JSON을 결과값으로 출력합니다.

[스터디 자료 velog](https://velog.io/@dps0340/KPU-C%ED%81%AC%EB%A6%BF%EC%A5%AC%EC%A5%AC-%EC%8A%A4%ED%84%B0%EB%94%94-%EC%9E%90%EB%A3%8C)

## 팀원

박근우, 장동현, 이하늘, 이지호

## 사용 스택

개발: Python, Django

의존성 관리: pipenv

CI/CD: Github Actions, AWS Codedeploy

배포: Docker, Docker-compose, AWS EC2

DB: Docker-compose 상의 PostgreSQL

로깅: prometheus, grafana

## 데이터베이스 모델링

TODO

## API

Postman으로 문서화 하였습니다.

[API  링크](https://documenter.getpostman.com/view/4929660/TVsxC6r1)

## 로컬 설정 가이드

### 환경 변수 설정

'Django_secret_key': 시크릿 키, 온라인 등에서 생성 가능

'DB_USER': DB 사용자 id

'DB_PASSWORD': DB 사용자 비밀번호

'DB_HOST': DB 서버 url

'DB_PORT': DB 서버 포트, PostgreSQL기준 기본값 5432

'BOARD_DEBUG': 디버깅 상태인가 나타내는 변수, 프로덕션에서는 설정 X
