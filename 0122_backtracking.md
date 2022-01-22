# 야옹님의 백트래킹 강의



1. 구현 - 재귀 함수
2. 완전탐색 

```python
# 2자리 3진수의 기본 구조

# 00
# 01
# 02
# 10
# 11
# 12
# 20
# 21
# 22

for i in range(3) :
    for j in range(3) :
        print(str(i)+str(j))
        
        
# 7진수 ,.,,
for i in range(7) :
    for j in range(7) :
        for k in range(7) :
        	print(str(i)+str(j)+str(k))
            
            
            
 ## 진수를 바꾸려면 for문 range의 수를 바꾸면 된다


# =========================

# m을 입력 받아서 3자리 m진수를 모두 출력해라
m = int(input())
for i in range(m) :
    for j in range(m) :
        for k in range(m) :
        	print(str(i)+str(j)+str(k))
            
            
            
 # ========================

# n, m을 입력 받아서 n자리 m진수를 모두 출력해라 -- 재귀 쓰는 목적은 이걸 처리하려고

# 즉, n중 반복문 구현!!! -- 재귀함수가 아니면 까다롭다

# 반복문의 중첩 개수를 받아서 그만큼의 재귀함수를 만든다



# =============================



## 3가지 템플릿 -- 거의 모든 재귀함수를 풀 수 있는 템플릿
# 1. 문제에 맞게 재귀 설계 x
# 2. 문제를 우리가 가진 틀에 맞게 변형



# 또 다른 2가지 템플릿 -- 2차원 백트래킹 // 나중에 알려줌 
```







## < 오늘의 목표 > n중 반복문 구현

1. 첫 번째 템플릿

```python
# n자리 m진수의 3가지 방식을 배운다 -> 외운다
# 문제를 n자리 m진수 문제로 변형하는 법을 배운다.


# 0-based

n, m = map(int, input().split())

arr = [ 0 for i in range(n) ]
def recur(cur) :
    if cur == n : # 모든 반복문을 돈 거다
        print(*arr) # print(3)을 하고 종료됨
        return
    
    for i in range(m) :
        arr[cur] = i
        recur(cur + 1)
        
recur(0)




# if 0 == n :
print(*arr) 가 된다

else :
    for i in range(m) :
        arr[0] = i
        recur(0 + 1)
        # recur(0+1)이 다시 for문으로 바뀜
        for j in range(m) : #아래와 같이 이중 for문이 구성됨
            arr[0] = j
            recur(1+1) # 값 1더해짐
            
            
            
            
# 3 5일 떄 출력
3 5
0 0 0
0 0 1
0 0 2
0 0 3
0 0 4
0 1 0
0 1 1
0 1 2
0 1 3
0 1 4
... 
4 4 0
4 4 1
4 4 2
4 4 3
4 4 4
```

```python
## <풀어서 써보기 > ##

# 3 5 일 떄
# n = 3, m = 5

arr = [ 0 for i in range(3)]

def recur(cur) :
    if cur == 3 :
        print(*arr)
        return
    
    for i in range(5) :
        arr[cur] = i
        recur(cur + 1)
        
recur(0)



for i in range(5) :
    arr[0] = 0
    # recur(0 + 1)
    for j in range(5) :
        arr[0] = j
        # recur(1 + 1)
        for k in range(5) :
            arr[0] = k

0 0 0
0 0 1
0 0 2
0 0 3
0 0 4
0 1 0
0 1 1
```







2. 두 번째 템플릿 - 한 케이스 내에 중복된 값이 없는 순열

   ```python
   # 3 5
   
   # 중복 제거 - 숫자 두 개가 똑같으면 출력 안 할 거임
   
   # 000 # 출력 안 할 거임
   # 001
   # 002
   # 003
   # 004
   # 010 # 
   # 011
   # 012
   # 013
   # 014
   # ... 에서
   
   # 012
   # 013
   # 014
   # 021
   # 023
   # 024 ... 이런 애들만 출력 : 순열
   ```

   ```python
   n, m = map(int, input().split())
   
   visited = [False for i in range(m)] # visited[i] : i를 이미 사용했는지 확인하는 용도
   # visited[i] : visited를 모두 False로 채워줌
   # m은 진수임, 10진수 문제면 10넣어주면 됨
   
   arr =[ 0 for i in range(n)]
   def recur(cur) :
       if cur == n : # 모든 반복문을 돈 거다
           print(*arr) # print(3)을 하고 종료됨
           return
       
       for i in range(m) :
           if visited[i] : # i가 이미 있다면 # visited[i]가 True면
               continue # i를 채우지 마라
           	
           arr[cur] = i # i가 없으면 ## arr[cur] = i로 초기화 해줘야 다음 recur(cur + 1)이 됨
         	visited[i] = True # visited[i]를 True로 바꿔라 - 뒤에서는 i를 넣지 마라
           recur(cur + 1)
           visited[i] = False # 다른 반복문으로 넘어갈 때 visited[i]는 False로 바꿔줌
               
   recur(0)
   
   ```

   ```python
   ## < 풀어서 써보기 > ##
   
   # n = 3, m = 5일 때
   
   arr = [ 0 for i in range(3)]
   
   visited = [False for i in range(5)] # F F F F F
   arr = [ 0 for i in range(3)] # 0 0 0
   
   def recur(cur) :
       if cur == 3 :
           print(*arr)
           
       for i in range(5) : # i가 1이라고 생각해보자
           if visited[i] == True :
               continue        
           arr[cur] = i
           visited[i] = True
           # recur(0 + 1)
           
           for j in range(5) :
               if visited[j] == True :
                   continue
               arr[cur] = j
               visited[j] = True
               # recur(1 + 1)
               
               for k in range(5) :
                   if visited[k] == True :
                       continue
                   arr[cur] = k
                   visited[k] = True
                   # recur(2+1) - 안 돌아가는데 그냥 적어만 둠
                   
                   visited[k] = False
               visited[j] = False    
           visited[i] = False
    
   recur(0)
   
   
   # ========================================================================
               
   arr = [0, 0, 0]
   
   visited[i] = [True, False, False, False, False] # 0일 때
   visited[j] = [False, True, False, False, False] # 1일 때
   visited[k] = [True, False, False, False, False] # 0일 때 - continue
   visited[k] = [False, True, False, False, False] # 1일 때 - continue
   visited[k] = [False, False, True, False, False] # 2일 때 - arr[2] = 2
   visited[k] = [False, False, False, True, False] # 3일 때 - arr[2] = 3
   visited[k] = [False, False, False, False, True] # 4일 때 - arr[2] = 4
   
   0 0 0 # 얘 안 함, 이미 visited[i]에서부터 True임
   0 0 1 # 얘 안 함
   0 0 2 # 얘 안 함
   0 0 3 # 얘 안 함
   0 0 4 # 얘 안 함
   0 1 0 # 얘 안 함
   0 1 1 # 얘 안 함
   0 1 2 # 얘 함
   0 1 3 # 얘 함
   0 1 4 # 얘 함
   0 2 0 # 얘 안 함
   ```





3. 세 번째 템플릿 - 중복된 케이스를 안 본다

   ```python
   # 012 - 얘만 출력
   # 021 - 밑으로는 실질적으로 같으니까 안 봄
   # 102
   # 120
   # 201
   # 210
   # ...
   
   # 5 6 7 8 9
   # 9 8 5 7 6 같은 거임, 하나만 뽑겠다
   
   # => 오름차순만 남긴다
   # ==> 비내림차순(오름차순x)만 남긴다 !!! (000 얘네도 출력해줘야 하기 때문에)
   
   
   n, m = map(int, input().split())
   arr = [0 for i in range(110)]
   
   def recur(cur, start) :
       if cur == n :
           print(*arr)
           return
       
       for i in range(start, m) :
           arr[cur] = i
           recur(cur + 1, i + 1)
           
   recur(0, 0)
   
   
   ```

   ```python
   ## < 풀어서 써보기 > ##
   
   # n = 3, m = 5 일 때
   
   def recur(cur, start) :
       if cur == n :
           print(*cur)
           
       for i in range(0, 5) : # start : 0 -> 1 -> 2 
           arr[cur] = i # arr[0]
           # recur(0 + 1, i + 1)
           for j in range(1, 5) : # start : 1 -> 2 -> 3
               arr[cur] = j #arr[1]
               # recur(1 + 1, i + 1)
               for k in range(2, 5) : # start : 2 -> 3 -> 4
                   arr[cur] = k # arr[2]
   
   recur(0, 0)
   
   # =====================================
   # for문 돌 때마다 start값이 1씩 증가하며 수열 생성
   
   0 1 2
   0 1 3
   0 1 4
   0 2 3
   0 2 4
   0 3 4
   1 2 3
   1 2 4
   1 3 4
   2 3 4
   ```

   