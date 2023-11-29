from flask import Flask, request, jsonify

app = Flask(__name__)

def calcular_fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * calcular_fatorial(n-1)

def calcular_fibonacci(n):
    if n <= 1:
        return n
    else:
        return calcular_fibonacci(n-1) + calcular_fibonacci(n-2)

@app.route('/')
@app.route('/index')
def index():
    return jsonify({'Mensagem': 'Index'})

@app.route('/myapi', methods=['POST'])
def myapi():
    if request.is_json:
        data = request.get_json()

        if 'fact' in data and -20 <= data['fact'] <= 20:
            fatorial = calcular_fatorial(data['fact'])
        else:
            fatorial = None

        if 'fib' in data and -20 <= data['fib'] <= 20:
            fibonacci = calcular_fibonacci(data['fib'])
        else:
            fibonacci = None

        result = {'fatorial': fatorial, 'fibonacci': fibonacci}
        return jsonify(result)
    else:
        return jsonify({'error': 'A solicitação deve ser em JSON'}), 400

if __name__ == '__main__':
    app.run(debug=True)
