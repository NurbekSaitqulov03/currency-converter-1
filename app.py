from flask import Flask, request, jsonify

app = Flask(__name__)

#usd = 11380.7 # 1 USD = 11380.7 UZS

@app.route('/api/to-usd', methods=['GET'])
def to_usd():
    """
    Convert to USD

    Returns:
        json: Converted amount
    
    Note:
        request data will be like this:
            /api/to-usd?amount=1000
        
        response will be like this:
            {
                "amount": 1000,
                "currency": "UZS",
                "converted": 88.7,
                "convertedCurrency": "USD"
            }
    """
    if request.method == "GET":
        args = request.args
        usd = args['amount']

        usd = int(usd) # 1-usd == 11360-uzs
        uzs = usd / 11360
        response_data = {
                "amount": usd,
                "currency": "UZS",
                "converted": uzs,
                "convertedCurrency": "USD"
                }
        return jsonify(response_data)
    else:
        return "No"

@app.route('/api/to-uzs', methods=['GET'])
def to_uzs():
    """
    Convert to UZS

    Returns:
        json: Converted amount
    
    Note:
        request data will be like this:
            /api/to-uzs?amount=1000
        
        response will be like this:
            {
                "amount": 1000,
                "currency": "USD",
                "converted": 1138070,
                "convertedCurrency": "UZS"
            }
    """
    if request.method == "GET":
        args = request.args
        uzs = args["amount"]
        uzs = int(uzs)
        usd = uzs*11360
        response_data = {
            "amount": uzs,
            "currency": "USD",
            "converted": usd,
            "convertedCurrency": "UZS"
        }
        return jsonify(response_data)
    else:
        return "No"

if __name__ == '__main__':
    app.run(debug=True)    