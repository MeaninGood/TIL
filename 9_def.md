# def 함수 배우기

- 코드 중복 방지 / 재사용 용이
- 숫자를 받아서(input)
- 세제곱 결과를 반환(output)
- 호출 : cube(2), cube(10), cube(100)
- **return이 정의되어 있지 않으면, 무조건 None이라는 하나의 객체 반환**
- `if function()` 가능 - def가 하나의 객체로 쓰임

```python
def function_name(parameter) :
    # code block
    return returning_value

# ============================

def cube(number) :
    return number **3 # number * number * number

print(cube(2))
print(cube(10))
print(cube(100))

# ===========================

def cube(n) :
    # n = 2
    print(n, type(n))
    return n ** 3

print(cube(2))

'''(출력)
2 <class 'int'>
8
'''

print(cube('2'))

'''
TypeError : ** or pow() : 'str' and 'int'
'''

```





## 1) function

- Void function

  - 명시적인 return 값이 없는 경우, None을 반환하고 종료

    

- Value returning function

  - 함수 실행 후, return문을 통해 값 반환
  - return을 하게 되면, 값 반환 후 함수가 바로 종료



### 1. def 함수에서 return의 개념

```python
## jupyter


In[1] : print('hello')
        hello
        
# =============================

In[2] : float('3.5')
Out[2] : 3.5 -> # Out 뜬다 : 출력한 게 아니라, 마지막에 나온 값이다.
                            # print 안 했는데 보이게끔 도와준 것


# =============================


In[3] : a = print('hello')

        b = float('3.5)
        print(a, b) # a에 None이 저장됨, print 자체는 return이 없다
        
        hello
        None 3.5
        
       #  --> a = 'hello'
            # print(a) 해야 hello 출력됨
            

```





- return은 함수 안에서만 사용되는 키워드
- print는 출력을 위해 사용되는 함수
- REPL(Read-Eval-Print Loop)환경에서는 마지막으로 작성된 코드의 리턴 값을 보여주므로(ex. jupyter) 같은 동작을 하는 것으로 착각할 수 있음



###  2. return 안 해줬을 때

```python

def void_product(x, y) :
    print('f{x} x {y} = {x * y})
    
ans = void_product(4, 5)

In[1] : print(ans)
        None # 함수에 return 안 해줘서 None이 뜬다

```





### 3. 값 여러 개 return

```python
def minus_and_product(x, y) :
    return x - y
    return x * y
    
y = minus_and_product(4, 5)
y # -1 하나의 값만 반환


# =============================


def minus_and_product(x, y) :
    return x - y, x * y   # 튜플로 반환
    
y = minus_and_product(4, 5)
y # (-1, 20)


# =============================


def rectangle(width, height) :
    return width * height, (width + height) * 2

print(rectangle(30, 20)) # (600, 100) 하나의 튜플
```



### 

## 2) Parameter, Argument

- **parameter** : 함수를 실행할 때, 함수 내부에서 사용되는 식별자 / 매개변수
- **Argument** : 함수를 호출할 때, 넣어주는 값 / 전달인자

```python
def function(ham) : # parameter : ham
    return ham

function('spam') # argument : 'spam'
```







## 3) 키워드 직접 지정 가능



### 1. print()에서 호출 할 때 키워드 지정

```python
def add(x, y) :
    return x + y

print(add(1, 2)) # 위치 - 내부에서 바인딩 x = 1 ; y = 2
print(add(y=2, x=1)) # 내가 직접 x와 y 값을 지정
```



- 키워드로 지정하는 순간 위치가 이미 박살남
- **위치 지정할 거면 다 해줘야 함**
- **안 할 거면 다 안 해야 함**

```python
print(add(x=1, 2)) -- def 호출!!
# SyntaxError (문법적 에러): positional argument follows keyword argument
```





### 2. 단, 함수 생성 시에 Default 값을 줄 수 있음

- **뒤(y)만 줄 수 있음!!!!!!!!!!!!** 

- 앞(x)은 지정 못 함!!!!!!!!!!!!!!

  ```python
  def add(x, y=0) :
      return x + y
      
  ## add(2) 라고 호출 시
  ## x = 2가 되어 계산됨
  ```

  



## 4) Packing / Unpacking

- def function(*args) // 튜플

```python
def add(*args) : # for문으로 무한히 받는 add 생성
    for arg in args :
        print(arg)
        
add(2)
add(2, 3, 4, 5) # args는 타입이 뭘까?
                # 튜플 // ** 두 개는 딕셔너리
```

```python
def add(*args) :
    print(args, type(args)) # (1, 2, 3) <class 'tuple'> - add(1, 2, 3)
                            # (1,) <class 'tuple'> - add(1)

    
print(add(1, 2, 3)) # None

print(add(1)) # None

add(1, 2, 3) # (1, 2, 3) <class 'tuple'>

#### None이 호출되는 경우는 해당 함수에 return이 없다는 뜻 !!
```

```python
def(*args, a) : # 앞에 쓰면 타입 에러, a 따로 지정
    return args, a
    
print(add(1, 2, 3, 4))

--> TypeError : add() missing 1 required keyword-only argument: 'a'
--> a에 인자가 있어야 하는데 없다
--> print(add 1, 2, 3, 4, a = 5)로 해줘야 함!!!! 

def another_add(a, *args) : # 뒤에 쓰면 맨 앞 값 a로 할당, 나머지 args로 할당
    return a, args
    
print(anoter_add(1, 2, 3, 4, 5)) 
--> (1, (2, 3, 4, 5)) 로 출력됨!!!
```





- def function(**kwargs) // 딕셔너리
  - 함수가 임의의 개수 Argument를 Keyword Argument로 호출될 수 있도록 지정
  - Argument들은 딕셔너리로 묶여 처리되며, parameter에 **를 붙여 표현

```python
def family(**kwargs) :
    for key, value in kwargs :
        print(key, ":", value)
        
--> family(father='고길동', monster='둘리')
# father, monster는 식별자임, 따옴표 필요 없음
# 따옴표 붙이면 'x', 'y'로 쓰는 것과 똑같음
```

```python
def add(**kwargs, a) :
    --> 정의조차 못함
    --> 딕셔너리라서 전부 kwrags로 빨려감, a값에 할당할 수 있는 인자가 없음
    --> 앞서 *args, a 는 a = 5로 할당할 수 있었지만
    --> **kwargs는 a = 5까지 빨아들임
```

```python
def add(a, **kwargs) :
    return a, kwargs
--> (1, {'b : 2}, 'c' : 3 }) 등등으로 해서 가능함
--> 맨 앞에 것만 a로 할당하고 나머지 빨아들이면 되기 때문
--> 따라서 **kwargs는 함께 정의하려면 무조건 뒤에만 써야 함!!!!!
```

```python
def greeting(name = 'john doe', age) : # 될까?
    # 기본 argument 값을 가지는 argument는 다음에 기본 값이 없는
    # argument로 정의할 수 없음
    # 뒤쪽은 기본값 둘 수 있는데, 앞에는 안 된다!!!
```





## 5) 분해(로직) / 추상화

1. 추상화 : Input -> Black box -> Output
2. 함수 : Input, Output
3. Input
   - 호출 : 위치로 호출 / 키워드로 호출
   - 정의 : 필수 / 선택(기본 값)
     많이 받을 때는 * 하나 써서 튜플로
     ** 두 개 써서 딕셔너리
4. Output : 반드시 하나의 객체 반환
   - return 안 쓸 건데요? -> None 타입 반환
   - return 값 여러 개는요? -> tuple로 반환





## 6) 함수의 범위

1. 함수는 코드 내부에 local scope를 생성
2. 그 외의 공간은 global scope로 구분
3. `scope` 
   - `global scope` : 코드 어디에서든 참조할 수 있는 공간
   - `local scope` : 함수가 만든 scope. 함수 내부에서만 참조 가능

4. `variable`
   - `global variable` : global scope에 정의된 변수
   - `local variable` : local scope에 정의된 변수



```python
< scope >
def ham() :
 a = 'spam'


# 1.
print(a) # NameError: name 'a' is not defined
        def 안에서 정의된 a는 def 내부에서만 끝난다
        
함수의 가장 기본 : local scope!
블랙박스의 결과를 받아보고 싶으면 반환 값을 변수에 저장해서 사용!
블랙박스 밖으로 결과를 주고 싶을 수 있음 -> return 해야 함!!!!!!!!!
    
# 2.
ham()
print(a) # NameError: name 'a' is not defined
```





## 7) 변수 수명주기

1. 변수는 각자의 수명주기(lifecycle)가 존재
2. `built-in scope` : 파이썬이 실행된 이후부터 영원히 유지
3. `global scope` : 모듈이 호출된 시점 이후 혹은 인터프리터가 끝날 때까지 유지
4. `local scope` : 함수가 호출될 때 생성되고, 함수가 종료될 때까지 유지
   -> return 해야 함

```python
def func() :
    a = 28
    print('local', a) # local scope
                    # a = 20, Return value = None
    
func()
print('global', a) # global scope -> 함수 종료(return) 후 수명주기 종료
                    # func = () 비어있음
```

```python
global_a = 1

def enclosed() :
    a = 20
    
    def local() :
        a = 300
        print(a) # 300 / 여기서 print(a) 실행되는 것 x 
        		# 아래 .local()에서 실행
            
    local() # 위에 local()함수 정의해주고, 이 위치에서 호출해 줌
            # 즉, 발동 됨 이 자리에서 바로 윗 줄의 print(a)가 실행되는 것
    print(a)

enclosed() # 20 / 여기서 enclosed() 함수 실행
            # print(a)가 이 자리에서 실행됨!!!!!
            
print(global_a) # 1 / 단순 global_a 가 실행

```





## 8) 이름 검색 규칙

1. 파이썬에서 사용되는 이름(식별자)들은 이름공간(namespace)에 저장되어 있음
2. 아래와 같은 순서로 이름을 찾아 나가며, LEGB Rule 이라고 부름
   - `Local scope` : 함수
   - `Enclosed scope` : 특정 함수의 상위 함수
   - `Global scope` : 함수 밖의 변수, import 모듈
   - `Built-in scope` : 파이썬 안에 내장되어 있는 함수 또는 속성
3. 즉, 함수 내에서는 바깥 scope의 변수에 **접근**은 가능하나 **수정**은 할 수 없음

```python
a = 0 ## global scope 
b = 1 ## global scope
def enclosed() :
    a = 10
    c = 3
    def local(c) :
        print(a, b, c) 
        
    local(300) # 출력 순서 (1) / 10 1 300
                # 위로 뚫고 올라갔더니 a, c가 있음
                # b를 찾아나갔더니 def local(c)가 호출되는 시점에
                # local(300)이 있으니 b = 300이 됨
                # 이 자리에서 위에 정의한 local(c) 함수가 호출이 됨
                # 여기서 print 되는 것!!!!!
                
    print(a, b, c)
    
enclosed() # 출력 순서 (2) / 10 1 3
            # 위로 뚫어서 a, c를 찾고
            # print의 영역이 def enclosed()이니까
            # 위로 뚫어서 b 긁어서 내려옴
            # 이 자리에서 enclosed() 함수 호출되어 print() 실행됨


print(a, b) # 출력 순서 (3) / 0 1
            # 맨 위의 global scope에서 찾음
            
```

```python
# sum = built-in 함수, LEGB에서 네 번째            
print(sum) # 1. built-in function  ## <built-in function sum>
print(sum(range(2))) ## 1
sum = 5 # 2. global에서 sum = 5 지정 
print(sum) ## 5
print(sum(range(2))) ## TypeError : 'int' objec is not callable
                    # 위의 global에서 sum = 5로 지정했으니
                    # built-in function으로 호출되지 않음 (LEGB상 4번째임)
```





## 9) 함수 내부에서 글로벌 변수 변경하기

```python
a = 10
def func1() : 
    global a # 무조건!!!!! 상단에 미리 global 변수 a 지정해줘야 함
    a = 3
    
print(a) ## 10
func1()
print(a) ## 3 # def 안에서 global로 global변수 a = 3을 변경해줌
```

```python
< nonlocal >
# 나 이거 글로벌까지는 아니고 내 근처에 있는 것 쓸게

x = 0
def func1() :
    x = 1
    def func2() :
        nonlocal x
        x = 2
    func2()
    print(x) # 2 함수 안에서만 잠시 다른 것 좀 쓸게~~
    
func1()
print(x) # 0 # global은 맨 위 x = 0이므로 0 출력
```

- `global a` : 글로벌 함수 불러 옴
- `nonglobal a` : 강제로 enclosed()함수가 가지고 있는 변수 가지고 와서
  **함수 내에서만** 바꿈



### <주의 사항>

1. 기본적으로 함수에서 선언된 변수는 local scope에 생성, 함수 종료시 사라짐

   

2. **해당 scope에 변수가 없는 경우(변수의 이름이 없는 경우) LEGB rule**에 의해 이름을 검색

   

3. 변수에 **접근은 가능**하지만, 해당 변수를 **수정할 수는 없음(!!!)**

   - 깰 수 있는 방법이 `global`과 `nonlocal`

     

4. 값을 할당하는 경우 해당 scope의 이름 공간에 새롭게 생성되기 때문

   

5. 단, 함수 내에서 필요한 상위 scope 변수는 argument로 넘겨서 활용할 것
   (클로저* 제외)

   - 클로저 : 어떤 함수 내부에 중첩된 형태로써 외부 scope변수에 접근 가능한 함수

     

6. 상위 scope에 있는 변수를 수정하고 싶다면 global, nonlocal 키워드를 활용 가

   - 단, 코드가 복잡해지면서 변수의 변경을 추적하기 어렵고, 예기치 못한 오류 발생
   - 가급적 사용하지 않는 것을 권장
   - **함수로 값을 바꾸고자 한다면 항상 argument로 넘기고 리턴 값을 사용하는 것 추천**
   - 알고리즘 배울 때 편하게 쓸 수는 있지만, 규칙을 깨는 것이기 때문에
   - 이외에는 가급적 사용 자제하라는 뜻

```python
umbers = [1, 2, 3, 4]

def new() :
    numbers[0] = 100
    
new()
print(numbers) # [100, 2, 3, 4]

--> 값이 바뀌는 이유 : 리스트 객체가 가지는 메모리 주소 값을 직접 바꿈
--> 리스트에 있는 첫번째 값을 집어서 바꾸기 때문
--> scope와는 별 관련 없음
```

```python
word = 'hello'

def new() :
    word.replace('h', '')
    a = word.replace('h', '')
    # print(word) # hello 
    # print(a) # ello
    
new()
print(word)

--> None이 반환됨


## 문자열String 은 imutable == 수정 불가능!!!
replace 함수를 쓴다고 해서 h에 해당하는 글자를 빈 문자열로 바꿔
단순히 반환해주는 것 뿐, 문자열을 직접적으로 바꾸는 것은 아님!


word = 'hello'


word.replace('h', '')
a = word.replace('h', '')

print(word) # hello
print(a) # ello
    
new()
print(word)


'a'가 싫어! 문제 참고, result 변수에 'a' 제외한 문자열 할당해 줌

```

