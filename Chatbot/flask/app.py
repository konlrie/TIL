import random
from datetime import datetime
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/mulcam')
def mulcam():
    return '20층 스카이라운지!'

@app.route('/dday')
def dday():
    today = datetime.now()
    new_year = datetime(2020, 1, 1)
    result = new_year - today
    return f'<h1>한 살 더 먹기까지 {result.days}일 남았습니다!</h1>'

# 인사하는 페이지
@app.route('/greeting/<string:name>')
def greeting(name):
    # return f'반갑습니다, {name}님!! :)'
    return render_template('greeting.html', html_name=name)

# 세제곱 결과를 돌려주는 페이지
@app.route('/cube/<int:number>')
def cube(number):
    result = number ** 3
    # return f'{number}의 세제곱의 값은 {number**3}입니다.'
    return render_template('cube.html', number=number, result=result)

# 인원 수에 맞게 메뉴를 추천해주는 페이지
@app.route('/lunch/<int:people>')
def lunch(people):
    menu = ['떡볶이', '고추잡채덮밥', '초밥', '돼지김치찜', '얼큰수제비', '꽝']
    order = random.sample(menu, people)
    return str(order)

@app.route('/movies')
def movie():
    movies = ['나이브스 아웃', '조커', '기생충']
    return render_template('movie.html', movies_list=movies)

@app.route('/ping')
def ping():
    return render_template('ping.html')

@app.route('/pong')
def pong():
    age = request.args.get('age')
    return render_template('pong.html', age=age)

@app.route('/naver')
def naver():
    return render_template('naver.html')

@app.route('/google')
def google():
    return render_template('google.html')

# 사용자로부터 입력받을 페이지를 렌더링해줌.
@app.route('/vonvon')
def vonvon():
    return render_template('vonvon.html')

# 요청을 받은 뒤 데이터를 가공해서 사용자에게 응답해줌.
@app.route('/godmademe')
def vonvonpong():
    name = request.args.get('name')
    # 데이터 리스트
    first_options = ['미모','잘생김','귀여움','못생김']
    second_options = ['친절함','싹수','애교','잘난척']
    third_options = ['코딩력','재력','무력','중력']
    # 각 데이터 리스트 별로 요소를 하나씩 무작위로 뽑음
    first_result = random.choice(first_options)
    second_result = random.choice(second_options)
    third_result = random.choice(third_options)

    # 뽑은 데이터를 템플릿에 넘겨줌
    return render_template('godmademe.html', name=name, first_result=first_result, second_result=second_result, third_result=third_result)

# 각 데이터 리스트 별로 요소를 하나씩 무작위로 뽑음

first_options = ['미모','잘생김','귀여움','못생김']
# sample 사용한 경우 (list 형태로 들어옴)
tmp = random.sample(first_options, 1)
print(tmp, type(tmp), tmp[0])
# choice 사용한 경우 (str 형태로 들어옴)
first = random.choice(first_options)
print(first, type(first))

# app.py 가장 하단에 위치
# 1. 앞으로 flask run으로 서버를 켜는게 아니라, python app.py로 서버를 실행한다.
# 2. 내용이 바뀌어도 서버를 껐다 켜지 않아도 된다.
if __name__ == '__main__':
    app.run(debug=True)