# KPU C크릿쥬쥬 프로젝트 - 게시판 백엔드(Django)

![GitHub](https://img.shields.io/github/license/DPS0340/DjangoCRUDBoard?style=for-the-badge) ![Website](https://img.shields.io/website?down_color=grey&style=for-the-badge&up_color=blue&url=http%3A%2F%2Fdjangocrudboard-env-2.eba-pncegi8j.ap-northeast-2.elasticbeanstalk.com%2Fstatus)

## 설명

차후에 React로 프론트엔드가 개발될 게시판의 백엔드 서버입니다.

HTTP API 방식으로 JSON을 결과값으로 출력합니다.

## 팀원

박근우, 장동현, 이하늘, 이지호

## 사용 스택

개발: Python, Django

의존성 관리: pipenv

CI: Github Actions

배포: AWS Elastic Beanstalk

DB: AWS RDS상의 PostgreSQL

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
