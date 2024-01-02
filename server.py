from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/get_furnishing_type', methods=['GET'])
def get_furnishing_type():
    response = jsonify({
        'furnishing': util.get_furnishing_type()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/predict_home_price', methods=['GET', 'POST'])
def rent():
    size = float(request.form['size'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    furnishing = request.form['furnishing']

    estimated_price = util.get_estimated_price(location, size, bhk, furnishing)
    response = jsonify({
        'estimated_price': estimated_price
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    util.load_saved_artifacts()
    app.run()