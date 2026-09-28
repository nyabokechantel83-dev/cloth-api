from flask import Flask, request, jsonify

app = Flask(__name__)

products = []
next_id = 1


@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to Cloth API"
    })


@app.route("/products", methods=["GET"])
def get_products():
    return jsonify(products), 200


@app.route("/products/<int:product_id>", methods=["GET"])
def get_product(product_id):
    product = next(
        (product for product in products if product["id"] == product_id),
        None
    )

    if product is None:
        return jsonify({
            "error": "Product not found"
        }), 404

    return jsonify(product), 200


@app.route("/products", methods=["POST"])
def create_product():
    global next_id

    data = request.get_json()

    if not data:
        return jsonify({
            "error": "Request body is required"
        }), 400

    name = data.get("name")
    price = data.get("price")
    category = data.get("category")
    stock = data.get("stock")

    if not isinstance(name, str) or not name.strip():
        return jsonify({
            "error": "Name must be a non-empty string"
        }), 400

    if not isinstance(price, (int, float)) or isinstance(price, bool) or price <= 0:
        return jsonify({
            "error": "Price must be a number greater than 0"
        }), 400

    if not isinstance(category, str) or not category.strip():
        return jsonify({
            "error": "Category must be a non-empty string"
        }), 400

    if not isinstance(stock, int) or isinstance(stock, bool) or stock < 0:
        return jsonify({
            "error": "Stock must be a non-negative integer"
        }), 400

    product = {
        "id": next_id,
        "name": name.strip(),
        "price": price,
        "category": category.strip(),
        "stock": stock
    }

    products.append(product)
    next_id += 1

    return jsonify(product), 201


@app.route("/products/<int:product_id>", methods=["PATCH"])
def update_product(product_id):
    product = next(
        (product for product in products if product["id"] == product_id),
        None
    )

    if product is None:
        return jsonify({
            "error": "Product not found"
        }), 404

    data = request.get_json()

    if not data:
        return jsonify({
            "error": "Request body is required"
        }), 400

    if "name" in data:
        if not isinstance(data["name"], str) or not data["name"].strip():
            return jsonify({
                "error": "Name must be a non-empty string"
            }), 400

        product["name"] = data["name"].strip()

    if "price" in data:
        if (
            not isinstance(data["price"], (int, float))
            or isinstance(data["price"], bool)
            or data["price"] <= 0
        ):
            return jsonify({
                "error": "Price must be a number greater than 0"
            }), 400

        product["price"] = data["price"]

    if "category" in data:
        if not isinstance(data["category"], str) or not data["category"].strip():
            return jsonify({
                "error": "Category must be a non-empty string"
            }), 400

        product["category"] = data["category"].strip()

    if "stock" in data:
        if (
            not isinstance(data["stock"], int)
            or isinstance(data["stock"], bool)
            or data["stock"] < 0
        ):
            return jsonify({
                "error": "Stock must be a non-negative integer"
            }), 400

        product["stock"] = data["stock"]

    return jsonify(product), 200


@app.route("/products/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):
    product = next(
        (product for product in products if product["id"] == product_id),
        None
    )

    if product is None:
        return jsonify({
            "error": "Product not found"
        }), 404

    products.remove(product)

    return "", 204


if __name__ == "__main__":
    app.run(debug=True)