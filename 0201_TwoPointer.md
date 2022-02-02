# 투포인터

# 연속 부분 수열 => 투포인터, 누적합(prefix sum)으로 어지간하면 풀린다 + binary search



- 1 5 8 7 3 
  - 1 8
  - 1 7
  - 1 8 7
  - 1 7 8



## 1. 특정 조건을 만족하는 연속 부분 수열을 찾는다.

## 2. 특정 조건을 만족하는 두 개의 수를 찾는다.



- 10 5
- 1 2 3 4 2 5 3 1 1 2 // 2 3, 5, 3 1 1 => 3개

1. 1은 뒤로 갈수록 증가할 수밖에 없다.

2. 끝점을 찾자.

3. 즉, 시작점을 찾고, 끝점을 점점 늘려가는 개념



```python
# 10 5
# 1 2 3 4 2 5 3 1 1 2
# s (시작점)
#     e (끝점)
# 6
#   s
#     e

1. 1을 시작점으로 했을 때, 5보다 작았으니까 e가 계속 뒤로 갔다
2. 5보다 클 때 e는 그대로 두고, s를 뒤로 보내자
3. 5를 찾은 상황에서는 - 하나 카운트
	1) s를 뒤로 보내도 되고
    2) e를 뒤로 보내도 되고 사실 누굴 옮겨도 상관 없음
    3) 왜냐면 값 맞추려고 앞뒤로 보내다 보면 맞춰짐
4. e가 뒤로 끝까지 가면 뭐가 없으니까 리스트에 + [0] 해주자

    
```

```python
# 2003


n, m = map(int, input().split())
arr = list(map(int, input().split())) + [0]

s = 0
e = 0
total = arr[0]
ent = 0

while e < n : ## e < n보다 작을 때니까 e를 n과 같이 맞춰주면서 끝내면 됨
    if total == m :
        cnt += 1
        e += 1
        total += arr[e]
        
    elif total < m :
        e += 1
        total += arr[e]
    else :
        total -= arr[s]
        s += 1
```

```python
# 3273

# 9
# 5 12 7 10 6 9 1 2 3 11
# 13

문제에서 순서 중요하다고 안 하면 그냥 일단 정렬부터 하고 해라

# 1 2 3 5 6 7 9 10 11 12
# s                    e
# 13되면은 카운트하고 아무거나 옮겨
# 1 2 3 5 6 7 9 10 11 12
#     s       e
# 13보다 크면 e가 앞으로 오고, 13보다 작으면 s가 뒤로 가라
```

```python
n = int(input())
arr = list(map(int, input().split()))
x = int(input())

s = 0
e = n - 1
cnt = 0
while s < e : # 둘이 같을 때 멈춰라
    if arr[s] + arr[e] == x :
        cnt += 1
        s += 1
    elif arr[s] + arr[e] < x :
        s += 1
    else :
        e -= 1
        
print(cnt)
```

```python
1. 특정 조건을 만족하는 연속하는 부분 수열을 찾느다.
# s = 0, e = 0 출발
# 반복 조건 : e < n
# 같이 뒤로 간다

2. 특정 조건을 만족하는 두 개의 수를 찾는다.
# s = 0, e = n-1 출발
# 반복 조건 : s < e
# 서로에게 다가간다
```

```python
# 2309

arr = [int(input()) for i in range(9)]
total = sum(arr)

arr.sort()

s = 0
e = 8
while s < e :
    if arr[s] + arr[e] == total - 100 :
        for i in range(9) :
            if i == s or i == e :
                continue
                print(arr[i])
                
        break
    elif arr[s] + arr[e] < total - 100 :
        s += 1
    else :
        e -= 1
```

````python
# 2467

# 5
# -99 -2 -1 4 98
#  s           e

# -99 98 : 절댓값 1
# -99 입장에서 98을 더했을 때 절댓값 1이니까 이거보다 좋으려면 더 큰 수를 더해야 한다. 근데 98이 제일 큰 수니까 더이상 이거보다 좋은 수를 더할 순 없다.
# 따라서 s를 뒤로 이동시켜야 한다.

# -99 -2 -1 4 98
#      s       e
# e 입장에서 이미 양수이고 이미 -99보다 더 좋은 수를 더할 수는 없음
# 따라서 e를 앞으로 보냄
````

```python
n = int(input())
arr = list(map(int, input().split()))

arr.sort()

s = 0
e = n - 1
x = arr[0]
y = arr[n-1]

while s < e :
    if abs(x+y) > abs(arr[s] + arr[e]) : #양끝의 합보다 작다면 갱신
        x = arr[s]
        y = arr[e]
        
    if arr[s] + arr[e] < 0 :
        s += 1
    else :
        e -= 1
        
print(x, y)
```

```python
# 9007

# 지금 n보면 1000까지니까 완탐이 된다. = n**이 된다
# 십만정도면은 n** 안 되니까 완탐 불가
# 4중for문 시간 초과 뜨니까
# 앞에 두 개, 뒤에 두 개로 반씩 나눠서 돌려보자


# 60 52 80 40
# 75 68 88 63
# 48 93 48 54
# 56 73 49 75

# 135 128 148 123 127... 60부터 뒤에 배열 하나씩 더함
# 104 121 ... 48부터 뒤에 배열 하나씩 더함
# 위에서 하나, 밑에서 하나 두 개의 수열 더하는 문제가 된다

# 둘 다 정렬
# 123 127 128 135 148
#      s
# 104 121 ...
# e

```

```python
m, n = map(int, input().split())
# 수열 길이는 어지간하면 n
# 합은 m, x 등등으로 함

arr = [list(map(int, input().split())) for i in range(4)]

a = []
b = []

for i in range(n) :
    for j in range(n) :
        a.append(arr[0][i] + arr[1][j])
        b.append(arr[2][i] + arr[3][j])
        
a.sort()
b.sort()

# s랑 e가 만나는 게 의미가 없다, 서로 다른 배열을 돌기 때문에
# s가 끝까지 가거나, e가 끝까지 가면 끝내라

s = 0
e = len(b) - 1
ans = a[s] + b[e]
while s < len(a) and e > 0 :
    if abs(ans - m) > abs(a[s] + b[e]) : # 두 값이 더 m에 가깝다면
        ans = a[s] + b[e]
        
    if a[s] + b[e] > m :
        e -= 1
        
    else :
        s += 1
        
print(ans)
```







```python
# O(n)

n = int(input()) # 얘는 한 번 실행됨

total = 0 # 얘는 한 번 실행됨
for i in range(n+1) : # 얘는 n번 실행됨
    total += i
    
print(total) # 얘는 한 번 실행됨

n = int(input()) # 얘는 한 번 실행됨



# O(n^2)

total = 0 # 얘는 한 번 실행됨
for i in range(n+1) : # 얘는 n번 실행됨
    for j in range(n+1) : # 얘도 n번 실행됨
    	total += i * j ## 즉, n^2번 실행됨
    
print(total) # 얘는 한 번 실행됨



# 1초 => 대충 1억번 정도 연산한다고 보면 됨
# 그래도 한 천만 정도로 맞춰라

# 만약 n이 십만까지 나온다고 하면, 이중for문 쓰지 말라는 거임
```

```python
# 22988

# 7 13
# 0 1 2 3 5 8 13
# 꽉 찬 건 필요가 없으니 13은 분리

# 0짜리 3개를 가져가도 무조건 하나를 받을 수 있다
# 2개, 3개를 가져가야 채울 수 있는 애들 찾기

# 2개를 채울 수 있는 애 : 8 + ? 했을 때 6.5 이상인 애들

# 8이랑 0을 더해도 하나를 받을 수 있음 - 지워줌

# 5랑 1이랑은 못 만듦
# 5랑 2는 가져가서 13하나 더 만들 수 있음 - 지워줌
# 1이랑 3은 3개씩 모아서 가져갈 수 밖에 없는 애들

# 1. 이미 가득찬 것들 제외
# 2. 투포인터로 두개씩 묶어서 제작
# 3. 남은 것들 // 3이 추가


n, m = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()

x = n
cnt = 0
s = 0
e = n - 1
for i in range(n)[::-1] :
    if arr[i] == m : # 꽉 찬 것들 제외시켜주기
        cnt += 1
        e = i - 1
       
while s < e :
    # 이거 실수 오차 남 (m/2로 쓰면) 부동소수점이라서
    # 그래서 if 2 * (arr[s] + arr[e]) >= m으로 써야 한다
    if arr[s] + arr[e] >= m / 2: 
        cnt += 1 
        x -= 2 # 두 개씩 빼 줌
        s += 1
        e -= 1
    else :
        s += 1
print(cnt + x //3)
```

