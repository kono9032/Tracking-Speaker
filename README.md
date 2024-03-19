
![스크린샷 2024-03-19 213245](https://github.com/kono9032/Tracking-Speaker/assets/63148742/92ea78f9-e70f-4835-bbe1-11873db21f83)

1. server_code / 카메라 영상 처리 담당
- 플랫폼 : RaspberryPI
- 사용언어 : python
- 주요 동작 :<br>
	소켓 통신, 방문자 입장 번호 부여 알고리즘<br>
	대기 인원수 송수신<br>
	영상 처리 좌표 송수신<br>
	영상 처리 트래킹(담당X)
	
2. manager_code / 직원용 호출 키오스크
- 플랫폼 : RaspberryPI
- 사용언어 : python
- 주요 동작 :<br>
	유선 시리얼 통신, 호출 번호 조합형 TTS 알고리즘<br>
	대기 인원수 송수신<br>
	호출 대상 영상 좌표 송수신<br>
	터치 스크린 GUI
	
3. client_code / 고객용 방문 키오스크
- 플랫폼 : RaspberryPI
- 사용언어 : python
- 주요 동작 :<br>
	유선 시리얼 통신, 대기 인원수 송수신<br>
	입장 이벤트 발생, 대기 순번 송신<br>
	터치 스크린 GUI
	