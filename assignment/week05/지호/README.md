#5주차 과제 제출

[1] 우분투 설치 : 이미지로 첨부

[2] 워게임: simple_sqli

1. 문제 파일 다운로드 후 내용 확인
2. VM 접속 (서버 생성해서 접속함)
3. 서버에서 실행해보면 로그인의 id와 password를 무작위로 입력했을 때 wrong이 나옴
4. 문제 파일의 내용 확인 - DB 부분

DATABASE = "database.db"
if os.path.exists(DATABASE) == False:
    db = sqlite3.connect(DATABASE)
    db.execute('create table users(userid char(100), userpassword char(100));')
    db.execute(f'insert into users(userid, userpassword) values ("guest", "guest"), ("admin", "{binascii.hexlify(os.urandom(16)).decode("utf8")}");')
    db.commit()
    db.close()
5. 로그인 우회, admin 계정 비밀번호 무력화하는 인젝션으로 flag 값 추출 필요
6. 아래와 같이 코드 수정
    DATABASE = "database.db"
    if os.path.exists(DATABASE) == False:
        db = sqlite3.connect(DATABASE)
        db.execute('create table users(useridchar(100), userpassword char(100));')
        db.execute(f'insert into users(userid, userpassword) values ("guest", "guest"), ("admin", "{binascii.hexlify(os.urandom(16)).decode("utf8")}");')
        db.commit()
        db.cldse()


7. POST 요청 시 user 테이블에 입력한 userid, userpassword가 일치하는 데이터 조회(pw 검증 부분을 주석처리->무력화)
8. 아래의 코드로 수정

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        userid = request.form.get('userid')
        userpassword = request.form.get('userpassword')
        res = query_db(f'select * from users where userid="{userid}" and userpassword="{userpassword}"')
        if res:
            userid = res[0]
            if userid == 'admin':
                return f'hello {userid} flag is {FLAG}'
            return f'<script>alert("hello {userid}");history.go(-1);</script>'
        return '<script>alert("wrong");history.go(-1);</script>'

app.run(host='0.0.0.0', port=8000)
9. Username에 admin' --을 적고 Password에 (스페이스바로 공백 작성)
10. 하면 username = 'admin'--', SQL에서 --부터 무시되어 로그인 우회
11. 로그인 하면 flag 값 : hello admin flag is DH{c1126c8d35d8deaa39c5dd6fc8855ed0}

//파이썬을 수강하지 않아서 해설을 보며 워게임 문제 풀이를 진행했습니다. 구체적으로는 코드에 쓰인 명렁어, 수정 방법, 수정 방향성 등을 찾아보며 풀이 진행했습니다.

[3] 워게임 2: XSS-1

1. 서버 생성 후 접속
2. 서버에 vuln(xss)page와 memo, flag가 있는 것을 확인
3. 파일 실행 후 코드 확인

#!/usr/bin/python3
from flask import Flask, request, render_template
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import urllib
import os

app = Flask(__name__)
app.secret_key = os.urandom(32)

try:
    FLAG = open("./flag.txt", "r").read()
except:
    FLAG = "[**FLAG**]"


def read_url(url, cookie={"name": "name", "value": "value"}):
    cookie.update({"domain": "127.0.0.1"})
    driver = None
    try:
        service = Service(executable_path="/usr/local/bin/chromedriver")
        options = webdriver.ChromeOptions()
        options.binary_location = "/usr/bin/google-chrome"
        for _ in [
            "headless",
            "window-size=1920x1080",
            "disable-gpu",
            "no-sandbox",
            "disable-dev-shm-usage",
        ]:
            options.add_argument(_)
        driver = webdriver.Chrome(service=service, options=options)
        driver.implicitly_wait(3)
        driver.set_page_load_timeout(3)
        driver.get("http://127.0.0.1:8000/")
        driver.add_cookie(cookie)
        driver.get(url)
    except Exception as e:
        # return str(e)
        return False
    finally:
        if driver is not None:
            driver.quit()
    return True


def check_xss(param, cookie={"name": "name", "value": "value"}):
    url = f"http://127.0.0.1:8000/vuln?param={urllib.parse.quote(param)}"
    return read_url(url, cookie)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/vuln")
def vuln():
    param = request.args.get("param", "")
    return param


@app.route("/flag", methods=["GET", "POST"])
def flag():
    if request.method == "GET":
        return render_template("flag.html")
    elif request.method == "POST":
        param = request.form.get("param")
        if not check_xss(param, {"name": "flag", "value": FLAG.strip()}):
            return '<script>alert("wrong??");history.go(-1);</script>'

        return '<script>alert("good");history.go(-1);</script>'


memo_text = ""


@app.route("/memo")
def memo():
    global memo_text
    text = request.args.get("memo", "")
    memo_text += text + "\n"
    return render_template("memo.html", memo=memo_text)


app.run(host="0.0.0.0", port=8000)

4. 플래그는 FLAG 변수에 저장되어 있음을 확인
5. /flag 엔드포인트에서 check_xss로 넘겨주는 cookie에 들어있는 값 확인하면 플래그를 얻어낼 수 있음
6. flag가 들어있는 cookie의 정보를 알기 위해서 param 값에 코드 입력
7. /memo 엔드포인트에서 param 값을 memo.html에 렌더링하여 사용자에게 보여줌. 따라서 /memo 엔트포인트에 document.cookie 값을 memo에 저장하여 이를 location.href의 ulr 주소를 넘겨주면 memo에서 플래그 얻을 수 있음

// 위 부분은 너무 어렵게 느껴져서... 해설 여러가지 참고해 봤습니다...

8. 서버-flag에 들어가서 내용을 입력하면 "good" 이라는 내용의 팝업이 출력
9. 이후 메모에 들어가서 출력값 확인하면 플래그를 확인할 수 있음
10. flag 값 : flag=DH{2c01577e9542ec24d68ba0ffb846508e}