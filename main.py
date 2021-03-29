from flask import Flask, jsonify
import model

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/api/analysis/<stock>', methods=['GET'])
def analysis(stock):
    arr = model.results(stock)
    return jsonify(arr)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3016)
