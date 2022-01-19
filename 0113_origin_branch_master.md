# 5. origin, branch, master



## 1) orgin 

- 내 원격저장소 주소의 `별명` , 관례상 origin으로 씀

- 내 컴퓨터에 있는 git을 웹상의 github에 연결해주어야 함

  ```bash
  $ git remote add origin https://github.com/MeaninGood/word.git
  
  git의 {원격저장소}에 {추가}할 건데 {별명은 origin}이고 {주소}는 이거다.
  
  # 주소 길게 쓰기 귀찮으니까 주소에 별명 달아줌
  # 한번 지정해두면 git remote add til https://github.com/MeaninGood/word.git로 지정 후
  # 이후 git remote add til만 해줘도 됨
  ```

  



## 2) master (성역)

1. master는 함부로 건들이면 큰일나요!
2. 마스터의 특정 버전에서 새로운  `branch`들 생성



## 3) branch

1. ### 명령어

   -  branch `생성`, `삭제`, `조회` 

   ```bash
   # 조회
   $ git branch
   
   # 원격 저장소의 목록 확인
   $ git branch -r
   
   # 생성
   $ git branch {branch name}
   --> 같은 이름의 branch가 이미 있는 경우 생성할 수 없다고 나옴
   
   # 삭제
   ## (병합된 것) 수정내역을 합치고 난 후에 삭제 가능
   $ git branch -d {branch name}
   
   ## (주의) 병합되지 않은 브랜치 강제 삭제
   $ git branch -D {branch name}
   
   ```
   
   
   ![image](https://user-images.githubusercontent.com/92563854/149342805-7e8fa71e-68a2-4974-a35b-5cc118da4e57.png)


   																![image](https://user-images.githubusercontent.com/92563854/149342848-fa16600f-96ab-4bd4-ae49-1f1b7cae98ee.png)

   




   - `git switch`
   
     - 현재 브랜치에서 다른 브랜치로 `HEAD`를 이동시키는 명령어
     
     - `HEAD`는 현재 브랜치를 가리키는 포인터
     
       ```bash
       # 다른 브랜치로 이동
       $ git switch {다른 브랜치 이름}
       
       # 브랜치 새로 생성과 동시에 이동
       $ git switch -c {다른 브랜치 이름}
       ```
     
       ![image](https://user-images.githubusercontent.com/92563854/149342900-3595eef8-bcc9-4b1c-a5a3-84d4c1f5141e.png)
     
       
     
     - 주의 사항
       - `git switch` 하기 전에 `commit` 했나?
       
       - `commit` 안 하면 git이 tracking 안 함 --> 오류 발생!!
       
       - `git --log` 로 확인해보기
       
         - `(HEAD -> dev)` 현재 최신 버전(first dev)
         - `(master)`는 구버전(22.01.13)에 있는 것을 알 수 있음
       
         ![image](https://user-images.githubusercontent.com/92563854/149342936-efdf558e-a6af-465f-a2db-d885cc03fca9.png)
       
         -  master로 넘어 와서 dev 브랜치와 병합해 줌
       
         - `$ git log --oneline`로 확인 : Fast-forward 확인하기!
       
           ![image](https://user-images.githubusercontent.com/92563854/149342965-51efde5f-86d9-4fee-a7ef-8d3c9a8ad36e.png)
