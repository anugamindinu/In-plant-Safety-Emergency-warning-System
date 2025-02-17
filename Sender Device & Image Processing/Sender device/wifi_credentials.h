#ifndef WIFI_CREDENTIALS_H
#define WIFI_CREDENTIALS_H

//#include <ESP8266WiFi.h>
#include <WiFi.h>

// WiFi credentials
const char* ssid = "Kavinda SAC";
const char* password = "12345678";

void setupWiFi() {
  Serial.println("Connecting to WiFi...");
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\nWiFi connected!");
}

#endif
