import serial
import time

bt_port = 'COM6'  # Change to the COM port your HC-05 is on
baud_rate = 9600

try:
    ser = serial.Serial(bt_port, baud_rate, timeout=1)
    print(f"Connected to {bt_port}")

    while True:
        line = ser.readline().decode('utf-8').strip()
        if line:
            print("Received:", line)
        time.sleep(0.1)

except serial.SerialException as e:
    print("Serial Error:", e)
except KeyboardInterrupt:
    print("Exiting gracefully...")
finally:
    if 'ser' in locals() and ser.is_open:
        ser.close()
