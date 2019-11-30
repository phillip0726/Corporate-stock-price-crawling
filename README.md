# Corporate-stock-price-crawling
네이버에서 기업 주가를 약 1년치 크롤링해옵니다.

## 0. Requirment
- selenium
- openpyxl
- chromedriver (On the same path with main.py)

## 1. Inputs
- 기업코드를 입력합니다. (네이버 기업 주가를 검색하면 확인할 수 있습니다)
<img src="https://user-images.githubusercontent.com/37935285/69900772-16c45880-13bb-11ea-9e0e-a957350b8630.png" width="90%"></img>

- 기업코드에 0을 입력하면 프로그램이 종료됩니다.
- 기업명을 입력합니다. (엑셀파일을 만들 때 사용됩니다)

## 2. Outputs
- 기업명을 제목으로 엑셀파일이 만들어집니다.
- 현재부터 약 1년치의 주가 정보를 저장합니다.
