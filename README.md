# Status Server

##알아야 할 것들
###### Github의 POST 데이터는 csrf_token이 없기 때문에 django view에서 @csrf_exempt를 써줘야 합니다.

##URL
##### /mobile/stat
###### mobileapp이 처음 시작 할 때 Maintenance와 Notice, 버전을 체크 하기 위해 요청을 하는 URL로 JsonResponse로 응답합니다.
##### /mobile/pingstate/
###### ping을 보냈을 때 문제가 있었던 목록을 확인할 수 있는 화면을 보여주는 URL입니다.
##### /mobile/sendgit
###### github에서 webhook데이터를 받을 때 사용됩니다. POST방식으로 Json데이터를 전송받습니다.

##View
##### CheckPing
###### MySQL Database에 연결해서 Ping결과 이력을 보여줍니다.
##### CheckState
###### App에서 Maintenance 와 Notice, Version을 확인합니다. get parameter로 'os'와 'locale'을 받습니다. 만약 없다면 'GET_FAILE_MESSAGE'를 응답합니다. 
###### Database에서 AppName으로 조회합니다. 없거나 두개 이상의 데이터가 왔을 시(등록할 떄 Unique로 등록하여 그럴리는 없겠지만)Exception이 발생하여 "APPNAME_FAIL_MESSAGE"를 응답합니다.
###### Maintenance가 있다면 Notice와 Version정보는 받을 필요가 없기 때문에 바로 maintenance를 응답합니다. 
###### Notice가 있다면 Version정보와 함께 Jsonresponse로 응답합니다.
 
###### Get parameter로 os와 locale을 입력 받을 수 있습니다. 없을 시 JsonResponse로 GET_FAIL_MESSAGE를 return하게 됩니다.
###### locale이 주어진 리스트에 없을 시 
##### SendGit
###### git에서 webhook데이터 전송시 처리하는 view입니다.
###### 처음 webhook을 만들면 ping데이터를 보내는데 이것 또한 Json으로 전송합니다. 보낸 header에 ping이라고 적혀옵니다.
###### git에서는 csrf토큰 없이 전송하기 때문에 django에서는 오류를 발생합니다. 반드시 @csrf_exempt를 작성해주셔야 오류가 나지 않습니다.

##Model
##### Applist
###### Application목록을 가지고 있는 테이블 입니다. 
##### Maintenance
###### Maintenance목록을 가지고 있는 테이블 입니다. ForeignKey로 applist의 id를 가집니다. 새로운 데이터 입력시 자동으로 등록시간을 등록합니다.
##### Notice
###### Notice목록을 가지고 있는 테이블 입니다. ForeignKey로 applist의 id를 가집니다. N:N relation으로 등록할 때 여러개의 applist를 선택할 수 있어서 보여줄 Application을 2개이상 선택할 수 있습니다. 
##### UpdateList
###### Update목록을 가지고 있는 테이블 입니다. ForeignKey로 applist의 id를 가집니다. build_ver은 빌드 버전을 저장하는 칼럼입니다. 정수형으로 저장하여 order를 결정할 수 있는 값이어야하므로 정수형이고 Unique한 값을 가져야 합니다. rec_ver과 man_ver은 유저가 보는 버전 번호입니다.
