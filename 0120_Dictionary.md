# Dictionary

## 1. 기본 구조

- key와 value가 쌍으로 이뤄진 자료구조

- key를 통해 value에 접근

  ```python
  dict_a = {'a' : 'apple', 'b' : 'banana', 'list' : [1, 2, 3]}
  
  >>> dict_a['list']
  [1, 2, 3]
  
  dict_b = dict(a = 'apple', b='banana', list=[1, 2, 3]) 으로도 생성 가능
  ```

  

1. key는 변경 불가능한 데이터(immutable)만 활용 가능

2. value는 모든 값으로 설정 가능(list, dict)

   ```python
   dic_a = {'a' : 'apple', 'b' : 'banana', 'list' : [1, 2, 3]}
   
   >>> dict_a['list'][0]
   
   ```



3. key와 value

   ```python
   # key와 value
   
   dict_a = {}
   
   dict_a[key] = [value] # key : value 추가
   dict_a[key].append[value] # key 이미 있을 때 value 추가
   ## key 유무 판단 : if dict_a.get(key) : 로 할 수 있음
   
   
   
   # for문으로 반복해서 value 넣기
   dict_sort ={}
   for _ in range(N):
     age, name = input().split()
     if dict_sort.get(age): # key 있으면
       dict_sort[age].append(name) # append로 value 추가해줌 
     else: # key 없으면
       dict_sort[age] = [name] # key : value를 추가해 key 값 넣기
   ```

   

   

## 2. 딕셔너리 순회

1. 기본적으로  key를 순회하며, key를 통해 값을 활용

   ```python
   grades = {'john' : 80, 'eric' : 90}
   for student in grades :
       print(student)
   
       
   john
   eric
   
   
   # ========================================
   
   grades = {'john' : 80, 'eric' : 90}
   for student in grades :
       print(student, grades[student])
    
   
   john 80
   eric 90
   
   for 문 돌릴 때
   # print(student) = key 출력 ###
   # print(grade[key]) = value 출력 #####
   --> value 출력하려면 딕셔너리명[키명] 으로 해야 함
   
   ```

   

2. 추가 메서드를 활용하여 순회할 수 있음

   - keys() : key로 구성된 결과
   - values() : value로 구성된 결과
   - items() : (key, value)의 튜플로 구성된 결과

   ```python
   ### 리스트로 반환되는 것에 주의!1!!
   
   dict_values([80, 90])
   dict_items([('john', 80), ('eric', 90)])
   
   
   
   print(grades.keys()) 
   # dict_keys(['john', 'eric'])
   print(grades.values()) 
   # dict_values([80, 90])
   print(grades.items()) 
   # dict_items([('john', 80), ('eric', 90)])
   

```python
### for문에서 .items() 이용해 key, value만 출력

grades = {'john' : 80, 'eric' : 90}

for name, score in grades.items() :
    print(name, score) # 앞이 key, 뒤가 value 자동 할당
    
john 80
eric 90

```



3. enumerate() 순회

   - 인덱스와 객체를 쌍으로 담은 열거형(enumerate) 객체 반환
   - (index, value) 형태의 tuple로 구성된 열거 객체를 반환

   ```python
   mebers = ['민수', '영희', '철수']
   
   for idx, member in enumerate(members) :
       print(idx, member)
       
   0 민수 # 따옴표 다 지워지고 단순 열거형으로 출력!!!!!!
   1 영희
   2 철수
   
   
   # enumerate(딕셔너리명) 인 것에 주의!!
   
   
   # ====================================
   
   seasons = ['spring', 'summer', 'fall', 'winter']
   print(list(enumerate(seasons)))
   
   
   [(0, 'spring'), (1, 'summer'), (2, 'fall'), (3, 'winter')]
   
   # 카운트와 iterable을 이터레이션 해서 얻어지는 값을 포함하는 "튜플"을 돌려줌
   
   
   
   # 0부터 시작하는 게 싫으면 시작 값 지정도 가능
   
   print(list(enumerate(seasons, start = 1)))
   
   
   [(1, 'spring'), (2, 'summer'), (3, 'fall'), (4, 'winter')]
   
   ```





4. 리스트에서 key, value로 딕셔너리 만들기

   ```python
   a= [[1, 2], [3,4], [5,6]]
   dict_value = {
       '작은거':[],
       '큰거':[],
   } # key 값 미리 만들어두고, value에 빈 리스트 생성
   for i in a:
       dict_value['작은거'].append(min(i)) # min 값 찾아서 넣기
       dict_value['큰거'].append(max(i)) # max 값 찾아서 넣기
   print(dict_value)
   
   # =================================
   
   
   a= [[1, 2], [3,4], [5,6]]
   dict_value = {
       '작은거':[],
       '큰거':[],
   }
   for i in a:
       dict_value['작은거'].append(i[0])
       dict_value['큰거'].append(i[1])
       # dict_value['작은거'].append(min(i))
       # dict_value['큰거'].append(max(i))
   print(dict_value)
   
   
   
   
   # ========================================
   
   
   a= [[1, 2], [3,4], [5,6]]
   
   dict_value = {} # 빈 딕셔너리
   idx = ["maximum", "minimum"] # key 이름 
   for i in idx: # key를 딕셔너리에 넣는 과정 필요함
      dict_value[i] = [] # dict_value["maximum"] = []로 만들어주는 과정
   for i in a:
      for j in range(len(idx)): # value 반복문으로 넣을 거임
         dict_value[idx[j]].append(i[j]) 
           # idx의 [j]에 해당하는 값에 a 리스트 i[j]를 넣어줌
           
   ```

