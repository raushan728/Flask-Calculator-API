from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()

    # Input values
    num1 = data.get('num1')
    num2 = data.get('num2')
    operation = data.get('operation')

    if num1 is None or num2 is None or operation is None:
        return jsonify({'error': 'Missing input'}), 400

    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        return jsonify({'error': 'Invalid number format'}), 400

    # Perform calculation
    if operation == 'add':
        result = num1 + num2
    elif operation == 'sub':
        result = num1 - num2
    elif operation == 'mul':
        result = num1 * num2
    elif operation == 'div':
        if num2 == 0:
            return jsonify({'error': 'Cannot divide by zero'}), 400
        result = num1 / num2
    else:
        return jsonify({'error': 'Invalid operation'}), 400

    return jsonify({
        'num1': num1,
        'num2': num2,
        'operation': operation,
        'result': result
    })

if __name__ == '__main__':
    app.run(debug=True)
