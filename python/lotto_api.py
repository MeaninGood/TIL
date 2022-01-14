# requests 불러오기
import requests

# requests 사용해서 로또 api에 데이터 요청
url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=997'
response = requests.get(url).json()

# url에서 ? 뒤에 작성되는 내용 : ? 전의 주소로 요청을 보냄
# ? 뒤의 값을 담아서
# 값이 여러 개 일 때 &로 구분

## method=getLottoNumber
## drwNo=997
## 두 개 요청한 상태

# requests.get(response)

# 요청 보내서 응답 받은 문서를 출력
print(response)

# 당첨 번호 정보를 리스트에 담기
winners = []


# 1~7까지 반복
for num in range(1, 7) :
    print(response[f'drwtNo{num}']) # key 값에 해당하는 values 출력
    # winners 리스트에 당첨번호 추가
    winners.append(response[f'drwtNo{num}'])
print(winners)