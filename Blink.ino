#include <dht.h>
#define outPin 7

dht DHT;

void setup() {
  Serial.begin(9600);  // HC-05 is connected to Serial TX/RX
}

void loop() {
  int readData = DHT.read11(outPin);
  if (readData == DHTLIB_OK) {
    float t = DHT.temperature;
    float h = DHT.humidity;

    // Send over Bluetooth (Serial)
    Serial.print("T:");
    Serial.print(t);
    Serial.print(" H:");
    Serial.println(h);
  } else {
    Serial.println("Read error");
  }

  delay(2000);
}
