

## 1. 모듈과 패키지

1. 모듈 
   - 특정 기능을 하는 코드를 파이썬 파일(.py) 단위로 작성한 것
2. 패키지 
   - 특정 기능과 관련된 여러 모듈 집합
   - 패키지 안에는 또 다른 서브 패키지를 포함



3. 모듈과 패키지 불러오기

   ```python
   import module
   from module import var, function, Class
   from module import * # *은 '전체를 가지고 오겠다'는 뜻
   
   from package import module
   from package.module import var, function, Class
   ```



4. 예제

   ```python
   import random
   
   print(random.sample(range(1, 46), 6))
   
   [5, 24, 45, 2, 42, 39]
   ```

   ```python
   a = {'a' : ['apple', 'banana'], 'b' : 'banana', 'c' : 'car', 'd' : 'drive', 'e' : ['error', 'eat']} # 코드가 길어질수록 복잡함
   
   print(a)
   '''
   {'a' : ['apple', 'banana'], 'b' : 'banana', 'c' : 'car', 'd' : 'drive', 'e' : ['error', 'eat']}
   '''
   
   # ==================
   
   import pprint
   
   pprint.pprint(a)
   '''
   {'a' : ['apple', 'banana'], 
   'b' : 'banana', 
   'c' : 'car', 
   'd' : 'drive', 
   'e' : ['error', 'eat']}
   '''
   
   # =====================
   
   from pprint import pprint # pprint에 있는 거에서 import pprint할래
   
   pprint(a) # 이렇게 줄여서 쓸 수 있음
   ```



5. 종류

   - datetime : 날짜와 시간을 조작하는 클래스 제공
   - pprint : 예쁘게 출력
   - math : 수학 함수

   1. 파이썬에 기본적으로 설치된 모듈과 내장 함수
      - random.py 등

   

   

6. 파이썬 패키지 관리자 (pip) 

   - (PyPI(Python Package Index)에 저장된 외부 패키지들을 설치하도록 도와주는 패키지 관리 시스템

     

7. 패키지 설치 

   - 최신 / 특정 / 최소 버전을 명시하여 설치 가능

     ```bash
     $ pip install SomePackage
     $ pip install SomePackage == 1.0.5
     $ pip install 'SomePackage>=1.0.4'
     ```

     

   - 이미 설치되어 있는 경우 이미 설치되어 있음을 알리고 아무것도 하지 않음



8. 패키지 관리하기

   - 아래의 명령어들을 통해 패키지 목록을 관리(1)하고 설치(2)할 수 있음

   - 일반적으로 패키지를 기록하는 파일의 이름은 requirements.txt로 정의

     ```bash
     $ pip freeze > requirements.txt # requirements를 txt파일로 저장, 파일로 지금 현재 버전 상태를 보존(freeze)해달라는 뜻
     $ pip install -r requirements.txt # txt파일에 있는 모든 버전을 다 다운 받도록 요청(-r)
     ```

     



9. 모듈 / 패키지 활용하기

   ```python
   NAME = 'SSAFY'
   
   def odd(n) :
       return n % 2 == 1
   
   def even(n) :
       return n % 2 == 0
   
   
   # check.py로 저장
   ```

   ```python
   import check
   # 위의 코드 저장된 경로 나옴
   
   >>> check.NAME
   'SSAFY' # 출력됨
   
   >>> check.odd(2)
   False
   
   from check import NAME
   >>> NAME
   'SSAFY'
   
   
   from check import *
   >>> NAME
   'SSAFY'
   
   >>> odd(1)
   True
   
   >>> even(2)
   True
   ```



10. 패키지

    - 패키지는 여러 모듈 / 하위 패키지로 구조화

      ex) package.module

    - 모든 폴더에는 `__init__.py`를 만들어 패키지로 인식
    - 수학과 통계 기능이 들어간 패키지를 아래와 같이 구성

## 



## 2. 가상환경

- 동일한 컴퓨터에 별도의 가상환경

  ```bash
  # 예시
  
  $ python -m(make) venv(가상환경) venv(<-가상환경이름임) # venv와 Lib라는 폴더가 생김
  
  $ pip list # 아직 전체 전역에서 설치된 모든 것들 다 쓰는 환경임
  
  $ source venv/Scripts/activate # (venv) 라고 뜸
  
  $ pip list # 가상환경에만 설치된 Lib 뜸
  
  $ pip install notebook # 가상환경에만 설치됨?
  ```

  

## 

## 3. 사용자 모듈과 패키지

```python
my_package(폴더) / math (파일) 생성
    
    안에 __init__.py 만들고 함수 생성  가능
    
from my_package(폴더) import math(파일)
    
from my_package.math import math

print(math.PI) # 이렇게 패키지로 묶어서 쓸 수 있다
```

