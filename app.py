from flask import Flask
from flask import request, jsonify

app = Flask(__name__)

@app.route('/calc', methods=['GET', 'POST'])
def calc():
    #Получаем параметры из URL
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    op = request.args.get('op', default='add')

    # Простейшие операции
    if op == 'add':
        result = a + b
    elif op == 'sub':
        result = a - b
    elif op == 'mul':
        result = a * b
    elif op == 'div':
        if b == 0:
            return "Ошибка: деление на ноль!"
        result = a / b
    else:
        return "Ошибка: неизвестная операция!"

    return f"Результат: {result}"

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8000)

