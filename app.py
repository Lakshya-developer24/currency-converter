from flask import Flask, request, jsonify, send_from_directory
import requests, os

app = Flask(__name__)

API_KEY = os.getenv("API_KEY")

@app.route("/")
def front():
    return send_from_directory("static", "index.html")

@app.route("/convert", methods=["GET"])
def convert_currency():
    base = request.args.get("base")
    target = request.args.get("target")
    amount = float(request.args.get("amount"))

    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{base}"
    data = requests.get(url).json()
    rate = data["conversion_rates"][target]
    result = amount * rate

    return jsonify({
        "base": base,
        "target": target,
        "rate": rate,
        "amount": amount,
        "converted": round(result, 2)
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
