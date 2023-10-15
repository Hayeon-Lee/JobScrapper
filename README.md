# JobScrapper

### 소개 및 개발 흐름

https://remoteok.com 과 https://weworkremotely.com 웹 사이트에서 일자리를 scrapping 하여 사용자에게 제공합니다.

scrapping 한 결과는 html 파일에 인자로 전달되며, html 파일 내부에서 표 형식으로 배치됩니다.

이후 해당 html 파일은 Flask 서버에 의해 사용자에게 전달됩니다.

### route

* / : 찾고자 하는 직업의 키워드를 입력할 수 있는 화면입니다.

* /search?keyword={{keyword}} : root 화면에서 키워드를 입력하면 {{keyword}}에 검색값이 전달된 뒤 해당 주소로 이동되고, scrapping 결과물을 화면에서 확인할 수 있습니다.

* /export?keyword={{keyword}} : search 화면에서 export to file 버튼을 누르면 csv 파일로 다운로드가 가능한데, 이 때 다운로드로 리다이렉팅 되는 화면입니다.

### 사용 방법

1) 홈 화면에서 찾고자 하는 직업의 키워드를 입력합니다.
2) Search 버튼을 누릅니다.
3) /search로 이동되며, 해당 화면에서 scrapping 결과를 확인할 수 있습니다.
4) 해당 화면에서 export to file 버튼을 누르면 csv 파일로 결과를 다운로드 할 수 있습니다.

### 파일 설명

[extractors 폴더]
* remoteok.py: https://remoteok.com 사이트에서 Beautifulsoup를 사용하여 일자리를 스크래핑 합니다.
* wwr.py: https://weworkremotely.com 사이트에서 Beautifulsoup를 사용하여 일자리를 스크래핑 합니다.

[templates 폴더]
* home.html: 사용자에게 키워드를 입력받는 화면입니다.
* search.html: 사용자가 home에서 키워드를 입력하면 스크래핑 결과를 보여주는 화면입니다. 결과를 csv 파일로 다운로드 받고 싶을 때 /export로 이동하는 역할을 해줍니다.

* main.py
    * @app.route("/"): home.html을 전달해줍니다.
    * @app.route("/search"): 스크래핑 결과를 전달합니다. 최초로 스크래핑 한 경우 db(딕셔너리)에 저장해두며 이후 같은 키워드로 검색했을 때는 딕셔너리에서 바로 결과값을 불러와 결과반환 시간을 줄였습니다. 사용자가 만약 keyword를 입력하지 않은 경우 다시 home으로 라우팅됩니다.
    * @app.route("/export"): 스크래핑 결과를 csv 파일로 저장합니다. 사용자가 만약 주소창에서 임의로 /export로 이동할 경우 다시 home으로 라우팅됩니다. 또한 검색결과가 db(딕셔너리)에 저장되어있지 않은 상태에서 임의로 /export 주소로 이동한 경우 /search 페이지로 돌아가 db에 저장한 뒤 다운로드하게 됩니다.
* file.py: 스크래핑 결과를 csv 파일로 저장합니다.
