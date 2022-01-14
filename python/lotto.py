# random.sample(리스트, 개수) - 비복원추출

import random

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
# print(response)

# 당첨 번호 정보를 리스트에 담기
winners = []


# 1~7까지 반복
for num in range(1, 7) :
    # print(response[f'drwtNo{num}']) # key 값에 해당하는 values 출력
    # winners 리스트에 당첨번호 추가
    winners.append(response[f'drwtNo{num}'])
print(winners)


numbers = list(range(1, 46))

for i in range(1000) :
    lotto = random.sample(numbers, 6)
    # 당첨 횟수 기록
    cnt = 0
    # print(lotto[0]~[5])
    
    for num in lotto :
        # print(num)
        # lotto가 가지고 있는 값들 하나하나가 
        # winners 안에 들어 있다면
        if num in winners :
           # 관계 형성
            cnt += 1
        # 당첨 갯수를 기록
        # 6개 당첨 == 1등
    if cnt == 6 :
        print(i)
        print('1등!!!')


