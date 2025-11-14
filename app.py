from flask import Flask, request, jsonify

app = Flask(__name__)

@app.get("/")
def inicio():
    return "Calculadora Kubernetes funcionando 🚀"

@app.get("/sumar")
def sumar():
    try:
        a = float(request.args.get("a", 0))
        b = float(request.args.get("b", 0))
        return jsonify({"resultado": a + b})
    except:
        return jsonify({"error": "Parámetros inválidos"}), 400

@app.get("/restar")
def restar():
    try:
        a = float(request.args.get("a", 0))
        b = float(request.args.get("b", 0))
        return jsonify({"resultado": a - b})
    except:
        return jsonify({"error": "Parámetros inválidos"}), 400

@app.get("/multiplicar")
def multiplicar():
    try:
        a = float(request.args.get("a", 0))
        b = float(request.args.get("b", 0))
        return jsonify({"resultado": a * b})
    except:
        return jsonify({"error": "Parámetros inválidos"}), 400

@app.get("/dividir")
def dividir():
    try:
        a = float(request.args.get("a", 0))
        b = float(request.args.get("b", 1))
        if b == 0:
            return jsonify({"error": "No se puede dividir entre cero"}), 400
        return jsonify({"resultado": a / b})
    except:
        return jsonify({"error": "Parámetros inválidos"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
