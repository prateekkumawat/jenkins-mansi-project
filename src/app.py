from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from config import Config  # Ensure this file has a SQLALCHEMY_DATABASE_URI

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

# Order Model
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_name = db.Column(db.String(80), nullable=False)
    order_address = db.Column(db.String(120), unique=True, nullable=False)
    order_contact = db.Column(db.String(120), unique=True, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "order_name": self.order_name,
            "order_address": self.order_address,
            "order_contact": self.order_contact
        }

# Get all orders
@app.route('/orders', methods=['GET'])
def get_orders():
    orders = Order.query.all()
    return jsonify([order.to_dict() for order in orders])

# Create a new order
@app.route('/orders', methods=['POST'])
def create_order():
    data = request.get_json()
    new_order = Order(
        order_name=data['order_name'],
        order_address=data['order_address'],
        order_contact=data['order_contact']
    )
    db.session.add(new_order)
    db.session.commit()
    return jsonify(new_order.to_dict()), 201

# Delete an order
@app.route('/orders/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    order = Order.query.get_or_404(order_id)
    db.session.delete(order)
    db.session.commit()
    return jsonify({"message": f"Order {order_id} deleted"}), 200

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, host='0.0.0.0')

