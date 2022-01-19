# 2. GUI vs CLI 

## 1. GUI (그래픽 유저 인터페이스)

- 그래픽을 통해 사용자와 컴퓨터가 상호작용하는 방식



## 2. CLI (커맨드 라인 인터페이스)

* 터미널을 통해 사용자와 컴퓨터가 상호작용하는 방식

### 1. CLI 사용 이유  

- new라는 폴더를 만들고자 한다면?

  GUI : 우클릭 -> 새로만들기 -> 폴더 -> new

  CLI : mkdir 파일명으로 만듦

  ​	`mv 파일명.assets/ 폴더명/ 으로 파일을 폴더 안에 넣을 수 있음`

  

### 2. 작업 위치(경로)

* **루트 디렉토리 ( / )**

  windows의 경우 일반적으로 c드라이브를 의미

* **홈 디렉토리 ( ~ )**

  반드시 현재 작업 위치 확인해야 함

  ![image-20220112150639442](C:\Users\장지선\AppData\Roaming\Typora\typora-user-images\image-20220112150639442.png)

  

  ```
  # 상대경로
  
  * ./ : 현재 작업하고 있는 폴더를 의미
  * ../ : 현재 작업하고 있는 폴더의 상위 폴더 (부모 폴더)
  
  * TIP : ctrl + l 화면 정리
  ```

  

## 3. Git Bash 사용하는 이유

1. Unix 기반 운영체제
2. 개발자들 사이에서 쓰는 사람들이 많음



## 4. 명령어

1. `cd` : 폴더 명

   - 현재 작업 중인 디렉토리를 변경하는 명령어

   - change directory

     ```bash
     # 홈 디렉토리로 이동
     $ cd
     
     # 폴더명 자동 완성 - # + tab
     $ cd folder # tab
     
     # 상위 폴더로 이동
     $ cd ..
     ```



2. `ls` : 현재 작업 중인 파일 / 폴더 명

   - list segments

   - 현재 작업 중인 디렉토리의 폴더 / 파일 명을 보여주는 명령어

     ```bash
     # 기본 사용법
     $ ls
     
     # 모든 옵션 (숨김 파일까지) 다 보여주는 방법
     $ ls -a(all의 약자)
     
     # 파일 / 폴더의 상세 정보를 알려줌
     $ ls -l(long의 약자)
     
     # 둘 다 사용하고 싶다면
     $ ls -a -l
     ```



3. `mkdir` : 폴더 생성

   - make direcctory

   - 폴더를 생성하는 명령어

     ```bash
     # 폴더 생성
     $ mkdir folder
     
     # 폴더 여러 개 생성 - 공백을 넣어줌
     $ mkdir folder folder1
     
     # 폴더 이름 사이에 공백 넣을 때
     $ mkdir "2022년 1월 12일"
     
     # 숨김 폴더 - .을 찍어줌
     $ mkdir .folder
     ```



4. `touch` : 파일 생성

   * 파일을 생성하는 명령어

   * 폴더 생성과 생성 방법 동일

     ```bash
     $ touch test.txt
     ```

### 

5. `start` : 폴더 / 파일 열기
   * 폴더 / 파일을 여는 명령어



6. `rm` : 삭제

   * remove

   * 파일 / 폴더 삭제 명령어

     ​	GUI : 휴지통으로 보냄

     ​	CLI : **완전 삭제**

     ```bash
     # 파일 삭제
     $ rm test.txt
     
     # 폴더 삭제 - -r (reculsive 옵션)
     $ rm -r folder/
     ```



7. `mv` : 이동

   * move

   * 파일 / 폴더 이동 명령어

     ```bash
     # 파일 / 폴더 이동 - {이동시킬 파일 / 폴더}{이동할 폴더}
     $ mv test.txt TIL
     
     # 파일 / 폴더 명 변경 - {변경시킬 파일 / 폴더}{변경할 이름}
     $ mv test.txt test1.txt
     ```



## 5. Why Git & Github ?

### 1) Git을 이용한 버전 관리 - 분산 버전 관리

* 레포트최종.docx, 레포트찐최종.docx 등
* 중앙 집중식 관리가 아닌, 분산 관리로 원활한 협업 가능
* 작업 파일 날려도 다른 사람 거 끌어오면 됨 

### 2) Github를 이용한 포트폴리오