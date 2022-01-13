# 4. Git Repository로 끝말잇기 하기



## [나 : 끝말잇기 할 파일 저장소에 올리기]   

1. new repository 생성  

   ![image](https://user-images.githubusercontent.com/92563854/149281207-86cedd8f-3403-426b-9813-c0bf9c26a053.png)




2. 내 컴퓨터에 세팅해주기

   - Word 폴더 생성 - 폴더 내에서 Git bash here 클릭

     ![image](https://user-images.githubusercontent.com/92563854/149281268-489fffa4-6600-441c-8bb0-ebc4b19bb87b.png)

     

     

   - `$ git init` 으로 초기화

   - `$ touch word.md`로 끝말잇기 할 파일 생성

   - `$ start word.md`로 만든 파일 실행

     ![image](https://user-images.githubusercontent.com/92563854/149281287-bc62e6b7-58b6-4ca3-be2a-8477b65a07a6.png)

     

     

   - 끝말잇기 할 단어 쓰고 저장

     ![image](https://user-images.githubusercontent.com/92563854/149281307-09d44d5e-e8ba-4197-91a3-4a5dd5a3dc3c.png)

     

     

   - `$ git status`로 확인

     ![image](https://user-images.githubusercontent.com/92563854/149281326-62d1c299-faf9-4caa-b112-eaa17fddf47e.png)

     

     

   - ` add - commit` 해 줌

     ![image](https://user-images.githubusercontent.com/92563854/149281349-cb813d28-449c-4190-9c06-5055cac244aa.png)

     

     

   - `$ git remote add origin https://github.com/MeaninGood/word.git` 으로 저장소 등록
   
   - $ git remote -v`로 확인
   
     ![image](https://user-images.githubusercontent.com/92563854/149281394-a259e0a5-9fe8-41cc-ac3a-ab6ae638da43.png)
   
     
   
     
   
   - `$ git push -u origin master` 
   
     - **첫 저장 시**에만 `-u` 붙여줌!!
     - 이후 생략 가능
   
     ![image](https://user-images.githubusercontent.com/92563854/149281441-7f374827-b7ca-4bd6-b9f9-fef8d59f0012.png)
   
     
   
     
   
   - Repository 확인 - 생성 완료
   
     ![image](https://user-images.githubusercontent.com/92563854/149281463-1a684162-2239-4267-891c-8a2cf2c7654f.png)
   
     
     
     



3. 만든 repository에 상대방 초대하기 - 내 Repository를 상대방이 자유롭게 쓸 수 있음

   - `Setting - Manage access - Add people` 로 상대방 초대하기

     ![image](https://user-images.githubusercontent.com/92563854/149281480-af527c04-722d-4c64-bf2f-f799d2413d4b.png)

     

     
     
     ![image](https://user-images.githubusercontent.com/92563854/149281499-e881c747-5117-4422-9b18-428078d17dfc.png)
     
     





## [상대방 : 끝말잇기할 저장소 가져오기]

1. `$  git clone {레포지토리 주소}` 로 저장소 본인 로컬로 복제

   ![image](https://user-images.githubusercontent.com/92563854/149281517-6159a621-da43-47e9-b97a-f68ecdbae788.png)
   
   



2. 끝말잇기 연결한 후 ` add - commit - push`로 업로드

   



## [서로 `git pull`로 업데이트 된 것 확인하며 이어가기]

- `word.md` 파일 껐다 켰다 하며 확인

- or `git bash`창에서 `$ git pull` 입력

  - 변경 사항 없을 때 : `Already up to date.`라고 나옴

    ![image](https://user-images.githubusercontent.com/92563854/149281533-7c0ad370-6500-4df4-b17f-78f199634864.png)

    
  
  - 변경 사항 있을 때 : 변경 내역 뜸
  
    ![image](https://user-images.githubusercontent.com/92563854/149281546-08241615-09b6-400d-8bbd-7d7640764a6d.png)
    
    
    
    
