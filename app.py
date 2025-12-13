from flask import Flask
from flask import request, jsonify

app = Flask(__name__)

def validate_post_data(data: dict) -> bool:

#GET
@app.route('/', methods=['GET'])
def hello():
    return 'Hello, world'

@app.route('/api', methods=['GET', 'POST'])
def api():
    if request.method == 'GET':
        return jsonify({'status' : 'test'})
    elif request.method == 'POST':
        return jsonify ({'status' : 'OK'})


if __name__== '__main__':
    app.run(debug=True, port=8080)

