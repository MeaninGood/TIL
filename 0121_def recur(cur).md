```python
def recur(cur) :
    # 탈출 조건
    if ... : ## 옮겨야 되는 게 없으면
    	return ## 끝내라

    # 명령어 (실행할 코드)
    
    # 재귀 호출
    
    

	# (+ 명령어)
```

```python
def recur(n, s, e, v) :
    # 탈출 조건
    if n == 0 : ## 옮겨야 되는 게 없으면
    	return ## 끝내라

    # 명령어 (실행할 코드)
    
    # 재귀 호출
    ## recur(n-1, s, v, e) n-1개를 s에서 v(가상으로 만듦)쪽으로 일단 보내 놓음
    # 1에서 3으로 다섯개를 보낸다 치면 4개를 2로 보냄
    print(str(s) + " " + str(e))
    recur(n-1, v, e, s)

	# (+ 명령어)
   

recur(int(input()) 1, 3, 2)








def recur(n, s, e, v) : # s에서 e로 옮기는 것
    # 탈출 조건
    if n == 0 : ## 옮겨야 되는 게 없으면
    	return ## 끝내라

    # 명령어 (실행할 코드)
    recur(n - 1, s, v, e) # s -> v로 n-1을 옮기고
    print(str(s) + " " + str(e)) 
    recur(n - 1, v, e, s) # v -> e로 다시 n-1 옮기고
    # 재귀 호출
    ## recur(n-1, s, v, e) n-1개를 s에서 v(가상으로 만듦)쪽으로 일단 보내 놓음
    # 1에서 3으로 다섯개를 보낸다 치면 4개를 2로 보냄


n = int(input())

print((2**n) - 1)

recur(n, 1, 3, 2)

```

```python
def recur(n) :
    if n == 0 :
        return
    
    print(n)
	recur(n - 1) # 5 -> 4 -> 3 -> 2 -> 1 ##### 역방향으로 하고 싶을 때 recur을 아래 둠
    
# ===========================================    
    
def recur(n) :
    if n == 0 :
        return
    
	recur(n - 1) # 5 -> 4 -> 3 -> 2 -> 1 #### 정방향으로 출력하고 싶을 때 위에 둠
    print(n) # 1 -> 2-> 3 -> 4 -> 5
    
# =============================================  

### 이진수 출력하기 - 10의 이진수    
def recur(n) :
    if n == 0 :
        return 
    
    recur(n // 2)
    print(n % 2) ### 1 0 1 0
    
recur(10)


def re(n) :
    return re(n//2) + re(n%2)

```

