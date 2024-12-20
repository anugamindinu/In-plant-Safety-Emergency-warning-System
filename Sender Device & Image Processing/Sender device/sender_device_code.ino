#include <WiFi.h>           // Include WiFi library for ESP32 or ESP8266
#include <PubSubClient.h>   // Include MQTT library

// Wi-Fi Credentials
const char* ssid = "YourSSID";
const char* password = "YourPassword";

// MQTT Broker Address
const char* mqtt_server = "broker.hivemq.com";

// Initialize WiFi and MQTT Clients
WiFiClient espClient;
PubSubClient client(espClient);

// Callback function for received messages
void callback(char* topic, byte* payload, unsigned int length) {
  Serial.print("Message arrived on topic: ");
  Serial.println(topic);
  Serial.print("Message: ");
  for (int i = 0; i < length; i++) {
    Serial.print((char)payload[i]);
  }
  Serial.println();
}

// Reconnect to MQTT broker if connection is lost
void reconnect() {
  while (!client.connected()) {
    Serial.print("Attempting MQTT connection...");
    if (client.connect("ArduinoClient")) {  // Set client ID
      Serial.println("connected");
      client.subscribe("test/topic");      // Subscribe to a topic
    } else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" trying again in 5 seconds...");
      delay(5000);
    }
  }
}



void setup() {
  Serial.begin(115200);

  // Connect to Wi-Fi
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }
  Serial.println("Connected to WiFi");

  // Set MQTT server and callback
  client.setServer(mqtt_server, 1883);
  client.setCallback(callback);
}

void loop() {
  // Reconnect to MQTT broker if disconnected
  if (!client.connected()) {
    reconnect();
  }
  client.loop();

  // Publish a message every 5 seconds
  static unsigned long lastPublishTime = 0;
  if (millis() - lastPublishTime > 5000) {
    lastPublishTime = millis();
    client.publish("test/topic", "Hello MQTT");  // Publish to a topic
    Serial.println("Message published");
  }
}

