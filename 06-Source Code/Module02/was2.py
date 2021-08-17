from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/test')
def test():
    return render_template('post.html')

@app.route('/post', methods=['POST'])
def post():
    value = [request.form['ketword00'], request.form['ketword01'], request.form['ketword10'], request.form['ketword11']]
    return value

if __name__ == '__main__':
    app.run()

검색어 두가지를 입력해주세요
[     ]keyword0
[     ]keyword1
[ 확인 ]


클라우드, cloud
클라우드 보안, cloud security
