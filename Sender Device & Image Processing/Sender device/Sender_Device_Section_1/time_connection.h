#ifndef TIME_CONNECTION_H
#define TIME_CONNECTION_H

//#include <ESP8266WiFi.h>
#include <WiFi.h>
#include <WiFiUdp.h>
#include <NTPClient.h>

// NTP setup
const long utcOffsetInSeconds = 19800; // Adjust this for your timezone (e.g., 19800 for GMT+5:30)
const char* ntpServer = "pool.ntp.org"; // NTP Server
WiFiUDP ntpUDP;
NTPClient timeClient(ntpUDP, ntpServer, utcOffsetInSeconds);

// Function to initialize NTP
void setupTime() {
  // Initialize the NTP client
  timeClient.begin();
  Serial.println("NTP Client Initialized");
}

// Function to fetch current time
String getCurrentTime() {
  timeClient.update();
  return timeClient.getFormattedTime();  // Get time in HH:MM:SS format
}

// Function to get current time components
void printCurrentTime() {
  unsigned long epochTime = timeClient.getEpochTime();  // Epoch time (seconds since Jan 1, 1970)
  int currentHour = timeClient.getHours();
  int currentMinute = timeClient.getMinutes();
  int currentSecond = timeClient.getSeconds();

  Serial.printf("Epoch: %lu, Time: %02d:%02d:%02d\n", epochTime, currentHour, currentMinute, currentSecond);
}

#endif
