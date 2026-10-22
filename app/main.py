from flask import Flask, jsonify

app = Flask(__name__)

PRODUCTS = [
    {"id": 1, "name": "Laptop", "price": 55000},
    {"id": 2, "name": "Keyboard", "price": 1500},
    {"id": 3, "name": "Mouse", "price": 700},
]


@app.get("/")
def home():
    return jsonify({
        "message": "E-Commerce DevOps API",
        "status": "running"
    })


@app.get("/health")
def health():
    return jsonify({"status": "healthy"})


@app.get("/api/products")
def get_products():
    return jsonify(PRODUCTS)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=False)
