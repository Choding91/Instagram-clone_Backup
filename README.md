# django-instagram-clone

[스파르타코딩클럽 내일배움캠프 AI 3기] B5팀 첫번째 인스타 클론코딩 프로젝트  



![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

## 프로젝트 소개
**인스타그램 클론 코딩**은 B5팀이 `Django`를 기반으로  **인스타그램** 서비스를 하나하나 구현한 첫번째 프로젝트입니다.


## 프로젝트 목표

- Instagram을 **분석**해서 **구조**를 직접 **설계**합니다.
- **Django 프로젝트 기본 구조**를 익힙니다.
- Django 배운 내용을 기반으로 **필수기능**을 완벽하게 이해합니다. 
- Git branch를 이용해서 *협업**하는 과정을 이해합니다.
    - 역할을 분담하여 모든 팀원이 프론트/백엔드 **구현**한다.
    - 단순히 구현 후 끝나는 것이 아닌 **코드 리뷰**와 **피드백**을 통해 함께 성장합니다.
    - 기존의 코드를 지속적으로 개선하기 위해 **리팩토링**을 진행합니다.
    
    
## 와이어프레임
### IA
![image](https://user-images.githubusercontent.com/12287842/194214627-2f8bf782-9aa2-4d8e-a8b7-1c9b5740dfa8.png)

## DB설계
![image](https://user-images.githubusercontent.com/12287842/194216665-f545faad-4a50-4b9a-9a5b-0927634aee13.png)

## API설계
### User 앱 
| 기능 | 메소드 | URL | request | response |
| --- | --- | --- | --- | --- |
| 로그인 | POST | /signin | {‘email’ : email, ‘pw’ : pw} | redirect(“/”) |
| 회원가입 | POST | /signup | {‘email’: email,‘name’ : name,‘username’ : username,‘pw’ : pw} | redirect(“/signin”) |
| 로그아웃 | GET | /logout |  | redirect(“/signin”) |
| 비밀번호 변경 | POST | /findpassword | {‘email’:email} | redirect(“/signin”) |
| 프로필 | GET | /profile_update |  | UserModel |
| 프로필 수정 | POST | /profile | {‘name’ : name,‘username’ : username,‘website’: website,‘bio’:bio,‘email’: email,‘phone’:phone, | redirect(“/profile”)|

### SNS 앱
| 기능 | 메소드 | URL | request | response |
| --- | --- | --- | --- | --- |
| 전체 게시글 조회 | GET | / |  | FeedModel |
| 상세 게시글 조회 | GET | /feed/<id> | {‘id’ : id} | FeedModel |
| 게시글 작성 | POST | /feed/create/ | {‘content : content} | redirect (f'/feed/{new_feed_id}') |
| 게시글 수정 | POST | /feed/update/<id> | {‘id’ : id, ‘content : content} | redirect(f'/feed/{id}') |
| 게시글 삭제 | GET | /feed/delete/<id> | {‘id’ : id} | redirect(“feed/<feed_id>”) |
| 댓글 조회 | GET | /comment/<feed_id> | {‘post_id’:post_id} | FeedCommentModel |
| 댓글 작성 | POST | /comment/create/<feed_id> | {comment : “댓글 내용”} | redirect(f'/feed/{id}') |
| 댓글 삭제 | GET | /comment/delete/<id> | {‘id’ : id} | (f'/feed/{current_feed_id}') |


## 프로젝트 결과 시연연상
[![B5팀 프로젝트 시연영상](http://img.youtube.com/vi/YEA9-4yuGwI/0.jpg)](https://www.youtube.com/watch?v=YEA9-4yuGwI&t=17s)



## Contributors

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/LeeHyunji">
        <sub><b>이현지</b></sub></a><br />
        <sub><b>Developer</b></sub></a><br />
        <sub><b>✈Team Leader</b></sub></a><br />
        <a href="https://github.com/LeeHyunji" title="Code">💻</a>
    </td>
    <td align="center">
      <a href="https://github.com/seoungjuyu">
        <sub><b>유승주</b></sub></a><br />
        <sub><b>Developer</b></sub></a><br />
	<sub><b></b></sub></a><br />
        <a href="https://github.com/seoungjuyu" title="Code">💻</a>
    </td>
    <td align="center">
      <a href="https://github.com/son950610">
        <sub><b>손상훈</b></sub></a><br />
        <sub><b>Developer</b></sub></a><br />  
	<sub><b></b></sub></a><br />
        <a href="https://github.com/son950610" title="Code">💻</a>
    </td>
    <td align="center">
      <a href="https://github.com/Choding91">
        <sub><b>조인걸</b></sub></a><br />
        <sub><b>Developer</b></sub></a><br />    
	<sub><b></b></sub></a><br />
        <a href="https://github.com/Choding91" title="Code">💻</a>
    </td>
    <td align="center">
      <a href="https://github.com/jetaime95">
        <sub><b>주세민</b></sub></a><br />
        <sub><b>Developer</b></sub></a><br />    
	<sub><b></b></sub></a><br />
        <a href="https://github.com/jetaime95" title="Code">💻</a>
    </td>
  </tr>
</table>  
