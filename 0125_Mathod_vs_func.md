# 1. 메소드 vs 함수

- 김대리 vs 프리랜서(소속x)

  ```python
  dict.get() = 메소드
  random.choice() = 함수
  ```

  

1. 함수 
   - 무조건 하나의 객체를 반환해야 함
   - 원본값을 바꾸긴 하지만 걔도 반환 값이 있음 = None
   - 내부 로직으로 뭔가 처리하는 과정이 있음



# 2. 문자열 조회  / 탐색 - 메소드

```python
dict['key'] # 값이 없으면 오류가 발생해야 하는 상황 
dict.get('key') # 값이 없으면 None을 반환하면 되는 상황

s.find(x) # x의 첫 번째 위치 반환, -1을 반환
s.index(x) # x의 첫 번째 위치를 반환. 없으면 오류 발생
s.isalpha() # 알파벳 문자 여부 (유니코드 상, 한글 포함)
s.isupper() # 대문자 여부
s.lslower() # 소문자 여부
s.istitle() # 타이틀 형식 여부
```

 



# 3. 문자열 변경 메소드

```python
s.replace(old, new[, count]) # 바꿀 대상 글자를 새로운 글자로 바꿔서 반환. 원본 바꾸기 x

s.strip([char]) # 공백이나 특정 문자 제거, .split(sep = None, maxsplit = -1)


s.split([char]) # 공백이나 특정 문자를 기준으로 분리
# 문자열을 특정한 단위로 나눠 "리스트"로 반환

'separator'.join([iterable]) # 구분자로 iterable을 합침
# 반복가능한(iterable) 컨테이너 요소들을 구분자(separator)로 합쳐 문자열 반환
# iterable에 문자열이 아닌 값이 있으면 Error

s.capitalize() # 가장 첫 번째 글자를 대문자로
s.title() # '나 공백 이후를 대문자로
s.upper() # 모두 대문자
s.lower() # 모두 소문자
s.swapcase() # 대<->소문자 변경
```





# 4. 리스트 메소드

```python
L.append(x)
L.insert(i, x)
L.remove(x)
# pop과 달리 '인자에 넣어준 값'을 제거함 == 특정한 값을 지정해서 지움

L.pop()
# 인덱스로 따라가기 때문에 a에서 제거된 값이 무엇인지 알 수 없음
# 그래서 반환값을 통해 뭘 뺐는지 알 수 있게 하는 것

L.pop(i)
L.extend(m)
L.index(x, start, end)
L.reverse()
L.sort()
# a.sort()는 원본 변경.
# sorted(a)는 정렬된 리스트 반환하기만 함. 원본 변경 x
L.count(x)
```





# 5. 튜플

- 순서를 가지는 0개 이상의 자료형
- 변경 불가





# 6. 셋

- 순서 없는 가변자료형
- 중복 불가
- 수학에서 집합과 동일한 연산 가능
- 딕셔너리에 value 없는 key들만 모아놓은 자료형이라고 생각하면 편함

```python
s.copy() # 셋의 얕은 복사본을 반환
s.add(x) # 항목 x가 셋 s에 없다면 추가
s.pop() # 셋s에서 "랜덤하게 (순서가 없으니까)" 항목을 반환, 해당 항목 제거
# set이 비어있을 경우 keyError
s.remove(s) # 항목 x를 셋 s에서 삭제, 항목이 존재하지 않을 경우 KeyError
s.discard(x) # 항목 x를 셋s에서 제거, 항목 x가 셋s에 없어도 에러 반환 x
s.update(t) # 셋 t에 있는
s.isdisjoint(t)
s.issubset(t)
s.issuperset(t)
```





# 7. 딕셔너리 메소드

```python
d.clear()
d.copy()
d.keys()
d.values()
d.items()

d.get(key[, default]) # key를 통해 value를 가져옴, KeyError 발생x
# default 값 설정 가능(기본 None)
# 그니까 value가 없으면 default 값 집어 넣는 형태로 쓸 수 있음

d.get(k, v)
d.pop(key[, default]) # key가 딕셔너리에 있으면 제거하고 해당 값을 반환
# 그렇지 않으면 default를 반환
d.pop(k, v)
d.update([other]) # 값을 제공하는 key, value로 덮어씀


a = dict('이건' : '왜안돼') --> 진짜 안 됨
a = dict(이건 = '돼') --> 이건 됨
>>> {'이건' : '돼'}

a.update(this='마찬가지로 함수') ## 함수니까 제발 = 형태로 넣어라
>>> {'이건' : '돼', "this" : '마찬가지로 함수'}

a.update(3='이거?') # 안 됨!!!! literal은 변수로 쓸 수 없기 때문에

a.update(int(3)='이거?') # 안 됨!!!! literal은 변수로 쓸 수 없기 때문

### 정수형으로 집어 넣기 -- 할당하는 방식으로 집어넣어라 이거 말고는 읎는 듯 ㅠ ###
a[3] = '??' 로 하면
>>> {'이건' : '돼', "this" : '마찬가지로 함수', 3 : '??'}


```

