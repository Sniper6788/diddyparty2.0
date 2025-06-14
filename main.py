from flask import Flask, jsonify
from flask_cors import CORS
import serial
import time
import re

app = Flask(__name__)
CORS(app)

def ten():
    bt_port = 'COM5'  # Replace with your actual COM port
    baud_rate = 9600

    try:
        ser = serial.Serial(bt_port, baud_rate, timeout=2)
        print(f"Connected to {bt_port}")

        line = ser.readline().decode('utf-8').strip()
        if line:
            print("Received:", line)
            pattern = r'TEMP:(?P<temp>[\d.]+)C.*?HUM:(?P<hum>[\d.]+)%.*?MQ2:(?P<gas>\d+)'
            match = re.search(pattern, line)
            if match:
                temp = float(match.group('temp'))
                hum = float(match.group('hum'))
                mq2 = int(match.group('gas'))
                print(f'Temperature: {temp}°C')
                print(f'Humidity: {hum}%')
                print(f'MQ2 Reading: {mq2}')
                return temp, hum, mq2
            else:
                print("Could not parse the string.")
    except serial.SerialException as e:
        print("Serial Error:", e)
    except KeyboardInterrupt:
        print("Exiting gracefully...")
    finally:
        if 'ser' in locals() and ser.is_open:
            ser.close()

    return None, None, None

@app.route('/api/temp', methods=['GET'])
def get_temp():
    temp, hum, mq2 = ten()
    timestamp = int(time.time())

    if temp is None:
        return jsonify({'error': 'Sensor data not available'}), 500

    return jsonify({
        'temperature': temp,
        'humidity': hum,
        'mq2': mq2,
        'timestamp': timestamp
    })

if __name__ == '__main__':
    while True:
        app.run(debug=True)
