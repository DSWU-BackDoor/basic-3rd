# 1. 기본 분석

- 사용된 프로토콜을 3가지 이상 작성하시오. -> SSL, HTTP, DNS


# 2. 웹 요청 분석

- HTTP 요청 중 ".pdf" 파일을 다운로드하는 요청을 찾으시오.

- 전체 URL (http:// 포함)을 작성하시오. -> [http://www.yongin.go.kr/ebook/src/viewer/download.php?host=main&site=20220430_101634_1&no=1]

- 요청 방식(GET/POST)을 작성하시오. -> GET

# 3. 서버 응답 분석

- 서버가 반환한 파일의 종류는 무엇인가? -> application/pdf

- 파일 크기는 얼마인가? -> 867,700 B(약 867KB)

- 파일 이름은 무엇인가? -> (23)_도시계획_계획의_실행.pdf

# 4. 파일 복구

-  NetworkMiner를 사용하여 파일을 복구하고, 복구 과정을 단계별로 작성하시오.
1. 복구하고자 하는 파일을 NetworkMiner에 불러온다.
2. 상단의 Files 탭을 클릭하여 추출된 전체 파일 목록을 확인한다. 우측 상단의 Filter 기능을 사용하여 복구하려는 파일의 확장자(.pdf, .jpg)나 키워드를 입력해 원하는 파일을 식별한다.
3. 식별된 파일의 세부 정보를 확인한다.(Source/Destination Host, Size 등)
4. 파일을 복구하고 저장한다.'Open File'을 눌러 파일의 내용을 확인한다.
5. 복구된 파일이 깨지지 않았는지, 의도한 데이터가 맞는지 최종 확인한다. PDF 리더나 이미지 뷰어로 파일을 열어 데이터 유실 여부를 확인하고, 필요 시 Parameters 탭에서 Content-Type 등을 대조하여 서버가 보낸 원본 형식과 일치하는지 검토한다.

-  복구 과정 화면을 캡처하여 첨부하시오.
<img width="500" alt="image" src="https://github.com/user-attachments/assets/2992f631-3c81-4747-903f-442b2716b616" />
