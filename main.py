from flask import Flask, request, jsonify
import model

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/api/analysis/', methods=['GET', 'POST'])
def form_example():
    # handling POST
    if request.method == 'POST':
        stock = request.form.get('stock')
        arr = model.results(stock)
        return jsonify(arr)

    # handling GET
    return '''
           Please enter right parameter bosq
           '''


@app.route('/api/analysis/<stock>', methods=['GET', 'POST'])
def analysis(stock):
    arr = model.results(stock)
    return jsonify(arr)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3016)
