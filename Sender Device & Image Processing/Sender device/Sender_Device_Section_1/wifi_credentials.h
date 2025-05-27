#ifndef WIFI_CREDENTIALS_H
#define WIFI_CREDENTIALS_H

//#include <ESP8266WiFi.h>
#include <WiFi.h>
#include "I2C_LCD.h"
// WiFi credentials
const char* ssid = "Kavinda SAC";
const char* password = "12345678";

void setupWiFi() {
  Serial.println("Connecting to WiFi...");
   clearLCD();
      displayMessage("Connecting to", "WiFi..........");
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
    /*
    digitalWrite(LED_BUILTIN, LOW);
    delay(250);
    digitalWrite(LED_BUILTIN, HIGH);
    delay(250);*/
  }
  Serial.println("\nWiFi connected!");
   clearLCD();
      displayMessage("WIFI", "Connected");
    /*digitalWrite(LED_BUILTIN, LOW);
    delay(2000);
    digitalWrite(LED_BUILTIN, HIGH);
    delay(2000);
    digitalWrite(LED_BUILTIN, LOW);*/
}
#endif