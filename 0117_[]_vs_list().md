# [ ] vs list()

- 둘 중에 성능은 항상 대괄호 방식이 더 좋음
- 특히 list() 방식은 C언어 방식
- 최우선은 가독성 !!
- '코드의 간결함' 보다, 어떤 목적으로 어떻게 짜여진 코드인지 보여주는 게 더 중요함





# 성능 ( loop & map & list comprehension)

- `for` -> 버전이 올라가면서 비약적으로 성능이 향상됨



```python
# keys(), values(), items()
a = { 'key' : 'value' }

for k, v in a.items() : # key와 value를 동시에 가지고 있는 것
    print(k, v)
    
    
print(keys()) # key 값만
print(values()) # value 값만


# enumerate
b = {'김' : 'rn'}
for idx, val in enumerate(b) :
    print(idx, val)
```



```python
1e-10 == 1 * 10^(-10)
```



```python
# 딕셔너리의 순서

{ 'key' : 'value' }
for idx, val in enumerate(a) :
    print(idx, val)
    
    
# 편의를 위해 정렬되어 나올 뿐, 순서는 없음
```





a = { 'key' : 'value' }



