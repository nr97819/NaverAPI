from flask import Flask, jsonify, request
from flask_restx import Api, Resource

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
api = Api(app)

@api.route('/search/<string:keyword>')
class was(Resource):
    def get(self, keyword): # Get 방식으로 데이터를 전송, 메서드 오버라이딩
        return jsonify(keyword)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)