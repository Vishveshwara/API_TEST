from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/bfhl', methods=['GET', 'POST'])
def bfhl():
    if request.method == 'GET':

        return jsonify({"operation_code": 1}), 200

    elif request.method == 'POST':
        data = request.json.get('data', [])
        numbers = []
        alphabets = []
        highest_alphabet = ""

        for item in data:

            if isinstance(item, str) and item.isdigit():
                numbers.append(int(item))

            elif isinstance(item, str) and len(item) == 1 and item.isalpha():
                alphabets.append(item)

                if not highest_alphabet or item.upper() > highest_alphabet.upper():
                    highest_alphabet = item


        response = {
            "is_success": True,
            "user_id": "Vishveshwara_Uthayakumaran_18012004",
            "email": "vishveshwara.2021@vitstudent.ac.in",
            "roll_number": "21BAI1208",
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_alphabet": [highest_alphabet] if highest_alphabet else []
        }

        return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)