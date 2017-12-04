# 먼지먹고 무임승차 (free ride with dust)

[미세먼지 고농도 시 '서울형 비상저감조치' 시행계획](http://opengov.seoul.go.kr/sanction/12497613)에 따라, 익일 혹은 당일 대중교통 무료 여부를 확인할 수 있는 웹사이트 [freeridewithdust.kr](https://freeridewithdust.appspot.com/)

## DONE:

- [x] 서울형 비상저감조치 기준 확인하기

    당일 00\~16시 구간의 PM2.5 평균 농도와 23시에 발표하는 다음날 예보의 농도가 모두 50 이상일 때–  
첫차 시간\~9시, 18시\~21시에 운행하는 대중교통 무료. 단 서울시내 구간만 해당됨.  
  - [x] 무료 요금 구간
  - [x] 미세먼지 기준치 (당일, 명일)
  - [x] 00-16시 평균치(오늘 평균)  
  요청 URL: http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnMesureLIst?itemCode=PM25&dataGubun=HOUR&searchCondition=WEEK&pageNo=1&numOfRows=10&_returnType=json&ServiceKey=hFfytrBnh8rAAckaVVfx4io3JRk4hFurd5sM4SUf5Fhnea2dOVy8rUlJrHBxN%2BuZYe5vWIvd0g9NldVJu8Bd3g%3D%3D
  - [x] 23시 기준 익일 예보  
  요청 URL: http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getMinuDustFrcstDspth?searchDate=2017-11-26&InformCode=PM25&_returnType=json&ServiceKey=hFfytrBnh8rAAckaVVfx4io3JRk4hFurd5sM4SUf5Fhnea2dOVy8rUlJrHBxN%2BuZYe5vWIvd0g9NldVJu8Bd3g%3D%3D
- [x] 도메인 이름 정하기
  freeridewithdust.kr
- [x] github 저장소 만들기
	- [ ] CI(git에 올리면 자동 deploy)는 숙제
- [x] 저렴하게 사용할 서버 찾기(앱엔진, 헤로쿠, 등등…)
  구글 클라우드 플랫폼 앱 엔진 사용
- [x] 개발스택
- [x] 디자인
- [x] 개발
- [x] 배포


---

## TODO:

- [ ] 다국어 지원하기
- [ ] 알림 기능 추가
- [ ] SNS 페이지 홍보
	- [ ] 트윗봇
	- [ ] 페북페이지
- [ ] 아이폰 추가
- [ ] 안드로이드 추가
- [ ] 디자인
	- [ ] 그라디언트 옵션 추가
	- [ ] 아이콘 css로 그리기
	- [ ] 미적으로 아름답게
	- [ ] 파비콘
	- [ ] 다국어 버튼 추가
- [ ] 개발
	- [ ] 장고로 옮기기
- [ ] 도메인 구입하기
- [ ] ㅎㅈㄴ
	- [ ] 아두이노 벨만들기(혜정님 전용!?)
- [ ] 널체움 글자에 페이스북 또는 슬랙링크 추가하기
