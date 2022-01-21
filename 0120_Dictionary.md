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
   
   # ===========================
   
   append 하지 않더라도,
   리스트 + 리스트 = [ , ]로 됨
   
   
   
   # for문으로 반복해서 value 넣기
   dict_sort ={}
   for _ in range(N):
     age, name = input().split()
     if dict_sort.get(age): # key 있으면
       dict_sort[age].append(name) # append로 value 추가해줌 
     else: # key 없으면
       dict_sort[age] = [name] # key : value를 추가해 key 값 넣기
   ```
   
   
   
   - key 접근 방식 `get`
   
     ```python
     # d{'a' :''} 일 때,
     
     d['a'] -> KeyError 
     d.get('a') -> None 반환
     
     ## get으로 접근하는 것이 좋다
     
     
     
     dictionary 핸들링
     
     - dict.keys() : 키값 출력
     - dict.values() : 값 출력
     - dict.items() : 키와 값 출력
     - dict.get(key, default) : 키 값에 대응하는 value 출력
       - (default값 = None이고 na값에 default에 입력된 값을 교환시켜서 출력한다)
       - dict[key]로도 value를 출력할 수 있는데 이때 na값이 있으면 키에러가 뜨는것이 차이점
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



4. 2차원 리스트를 딕셔너리로 만들기

   ```python
   members = [
       		[0, 0, 0],
       		[0, 0, 0],
       		[0, 0, 0]
   			]
   
   for number in numbers :
       for num in number :
           print(num)
           
   # members[0][0] -> members[1][0] -> members[2][0] -> members[0][1] ... 순으로 출력
   
   
   numbers = [
       		{'items' : [1, 2, 3, '철수']}
   			]
   
   # '철수' 뽑기
   numbers[0]['items'][?]
   if items == '철수' :
   # numbers[리스트][딕셔너리][리스트]
   
   
   
   # =========================================
   
   numbers = [
       		{'items' : [1, 2, 3, '철수']},
       		{'items' : [1, 2, 3, '영희']}
   			]
   
   for number in numbers :
       print(number) # 딕셔너리 {} 하나씩 나옴
       for key in number :
           print(key) # 키만 따로 나옴 : items
           print(number[key]) # value만 나옴 : [1, 2, 3, '철수'] , [1, 2, 3, '영희']
           for i in number[key] :
               print(i) # value만 한 줄에 하나씩 따로 나옴 1 ~ '철수'
               if i == '철수' : 
                   print(i, '정답') # 철수 정답 이라고 나옴 
   
   ```

   







5. 리스트에서 key, value로 딕셔너리 만들기

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

