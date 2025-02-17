#ifndef BUTTON_FUNCTION_H
#define BUTTON_FUNCTION_H

#include <Arduino.h>

//const int buttonPin[] = {D1, D2, D3, D4};
const int buttonPin[] = {22, 21, 19, 18}; // Use GPIO numbers for ESP32


void setupButtons() {
  for (int i = 0; i < 4; i++) {
    pinMode(buttonPin[i], INPUT_PULLUP);
  }
}

// Define button press states and timers
unsigned long pressStartTime[4] = {0, 0, 0, 0};  // Time when the button was pressed
bool buttonPressed[4] = {false, false, false, false};   // Track if the button is currently pressed

const unsigned long longPressDuration = 1000; // Threshold for long press in milliseconds

void handleButtons() {
  for (int i = 0; i < 4; i++) { // Loop through each button
    if (digitalRead(buttonPin[i]) == LOW) { // Button is pressed
      if (!buttonPressed[i]) { // If the button was not previously pressed
        buttonPressed[i] = true;
        pressStartTime[i] = millis(); // Record the press start time
      }
    } else { // Button is released
      if (buttonPressed[i]) { // If the button was previously pressed
        unsigned long pressDuration = millis() - pressStartTime[i];
        buttonPressed[i] = false; // Reset the button pressed state

        String message;
        if (pressDuration < longPressDuration) {
          // Short press: Low Risk
          if (i == 0) {
            message = "{\"Section\": \"Section 1\", \"status\": \"Low Risk\", \"priority\": \"medium\"}";
          } else if (i == 1) {
            message = "{\"Section\": \"Section 1\",  \"status\": \"Low Risk\", \"priority\": \"medium\"}";
          } else if (i == 2) {
            message = "{\"Section\": \"Section 1\",  \"status\": \"Low Risk\", \"priority\": \"medium\"}";
          } else if (i == 3) {
            message = "{\"Section\": \"Section 1\",  \"status\": \"Low Risk\", \"priority\": \"medium\"}";
          }
        } else {
          // Long press: High Risk
          if (i == 0) {
            message = "{\"Section\": \"Section 1\", \"status\": \"High Risk\", \"priority\": \"high\"}";
          } else if (i == 1) {
            message = "{\"Section\": \"Section 1\", \"status\": \"High Risk\", \"priority\": \"high\"}";
          } else if (i == 2) {
            message = "{\"Section\": \"Section 1\",  \"status\": \"High Risk\", \"priority\": \"high\"}";
          } else if (i == 3) {
            message = "{\"Section\": \"Section 1\",  \"status\": \"High Risk\", \"priority\": \"high\"}";
          }
        }

        // Publish the message if defined
        if (!message.isEmpty()) {
          if (i == 0) {
            client.publish(topic1, message.c_str());
          } 
          else if (i == 1) {
            client.publish(topic2, message.c_str());
          }
           else if (i == 2) {
            client.publish(topic3, message.c_str());
          }
           else if (i == 3) {
            client.publish(topic4, message.c_str());
          }
          Serial.println("Message sent: " + message);
        }
      }
    }
  }
}

#endif
