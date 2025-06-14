from flask import Flask, jsonify
from flask_cors import CORS
import random
import time

app = Flask(__name__)
CORS(app)

@app.route('/api/temp', methods=['GET'])
def get_temp():
    # Simulate a temperature sensor value (replace this with actual sensor reading)
    temp = round(random.uniform(20.0, 30.0), 2)
    timestamp = int(time.time())  # current time (UNIX)

    return jsonify({'temperature': temp, 'timestamp': timestamp})

if __name__ == '__main__':
    app.run(debug=True)
