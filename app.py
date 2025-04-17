from flask import Flask, jsonify, request

app = Flask(__name__)

# Strona główna
@app.route('/')
def home():
    return jsonify({"message": "Witaj w moim API!"})

# Strona hello, przyjmująca parametr name
@app.route('/hello')
def hello():
    name = request.args.get('name', default='World')  # Domyślnie 'World' jeśli brak parametru
    return jsonify({"message": f"Hello {name}!"})

# Nowa strona - /api/v1.0/predict
@app.route('/api/v1.0/predict')
def predict():
    try:
        # Pobieramy dwie liczby z zapytania GET
        num1 = float(request.args.get('num1'))
        num2 = float(request.args.get('num2'))
        
        # Sprawdzamy regułę decyzyjną
        if num1 + num2 > 5.8:
            return jsonify({"prediction": 1, "features": {"num1": num1, "num2": num2}})
        else:
            return jsonify({"prediction": 0, "features": {"num1": num1, "num2": num2}})
    
    except (TypeError, ValueError):
        # W przypadku błędnych danych wejściowych (np. brak liczb)
        return jsonify({"error": "Nieprawidlowe parametry, prosze podac dwie liczby."}), 400

if __name__ == '__main__':
    app.run(debug=True)
