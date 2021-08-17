import googletrans 
translator = googletrans.Translator() 
from flask import Flask, render_template, request

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/test')
def test():
    return render_template('get.html')

# @app.route('/get', methods=['get'])
@app.route('/post', methods=['post'])
def get():
    keyword1 = request.form['keyword1']
    keyword2 = request.form['keyword2']
    enkeyword1 = translator.translate(keyword1, dest='en')
    enkeyword2 = translator.translate(keyword2, dest='en')
    result = str([keyword1, enkeyword1.text, keyword2, enkeyword2.text])
    return result

if __name__ == '__main__':
    app.run()