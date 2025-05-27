//#include <ESP8266WiFi.h>
#include <WiFi.h>
#include <WiFiUdp.h>
#include <PubSubClient.h>
//#include "time_connection.h"
#include "wifi_credentials.h"
#include "mqtt_connection.h"
#include "button_function.h"
#include "I2C_LCD.h"

void setup() {
  Serial.begin(115200);
  setupWiFi();
  setupMQTT();
  setupButtons();
  initializeLCD();
  pinMode(buzzer,OUTPUT);
  displayMessage("Section 1", "Good Condition");
  // Initialize MQTT
  
 // Initialize time (NTP)
  //setupTime();
  
}

void loop() {
  // Ensure MQTT stays connected
  if (!client.connected()) {
    reconnectMQTT();
  }
  client.loop();
   handleButtons();
  // Get and print current time from NTP
  /*String currentTime = getCurrentTime();
  Serial.println("Current Time: " + currentTime);*/

  // Optionally print more detailed time
  //printCurrentTime();

  delay(1000); // Delay between time prints
}
