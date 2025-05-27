#ifndef BUTTON_FUNCTION_H
#define BUTTON_FUNCTION_H

#include <Arduino.h>

const int buttonPin[] = {D3, D4, D5, D6, D7};
//const int buttonPin[] = { 12,14,27,26,25}; // Use GPIO numbers for ESP32
#include <PubSubClient.h>
#include "I2C_LCD.h"
#define buzzer D8

extern PubSubClient client; 

void setupButtons() {
  for (int i = 0; i < 5; i++) {
    pinMode(buttonPin[i], INPUT_PULLUP);
    
  }

}

unsigned long pressStartTime[5] = {0, 0, 0, 0, 0};  // Time when the button was pressed
bool buttonPressed[5] = {false, false, false, false, false};  // Track if the button is currently pressed


const unsigned long longPressDuration = 2000; // Threshold for long press in milliseconds

void handleButtons() {
  for (int i = 0; i < 5; i++) { // Loop through each button
    if (digitalRead(buttonPin[i]) == LOW) { // Button is pressed
      if (!buttonPressed[i]) { // If the button was not previously pressed
        buttonPressed[i] = true;
        pressStartTime[i] = millis(); // Record the press start time
      }
    } else { // Button is released
      if (buttonPressed[i]) { // If the button was previously pressed
        unsigned long pressDuration = millis() - pressStartTime[i];
        Serial.println(pressDuration);
        buttonPressed[i] = false; // Reset the button pressed state

        String message;
        if (pressDuration < longPressDuration) {
          // Short press: Low Risk
          if (i == 0) {
            message = "{\"Section\": \"section 2\", \"status\": \"Low Risk\", \"priority\": \"medium\"}";
            digitalWrite(buzzer,HIGH);
           

            clearLCD();
            displayMessage("Alert Send To", "Fire Department");
          } else if (i == 1) {
            message = "{\"Section\": \"section 2\",  \"status\": \"Low Risk\", \"priority\": \"medium\"}";
            digitalWrite(buzzer,HIGH);

            clearLCD();
            displayMessage("Alert Send To", "First Aid Department");
          } else if (i == 2) {
            message = "{\"Section\": \"section 2\",  \"status\": \"Low Risk\", \"priority\": \"medium\"}";
            digitalWrite(buzzer,HIGH);

            clearLCD();
            displayMessage("Alert Send To", "Technical Department");
          } else if (i == 3) {
            message = "{\"Section\": \"section 2\",  \"status\": \"Low Risk\", \"priority\": \"medium\"}";
            digitalWrite(buzzer,HIGH);

            clearLCD();
            displayMessage("Alert Send To", "Supervisor Department");

          }
          else if (i == 4) {
            message = "{\"Section\": \"section 2\"}";
            clearLCD();
            displayMessage("section 2", "Good Condition");
            digitalWrite(buzzer,LOW);
          }
        } else {
          // Long press: High Risk
          if (i == 0) {
            message = "{\"Section\": \"section 2\", \"status\": \"High Risk\", \"priority\": \"high\"}";
            clearLCD();
            displayMessage(" RED Alert Send To", "Fire Department");
            digitalWrite(buzzer,HIGH);

          } else if (i == 1) {
            message = "{\"Section\": \"section 2\", \"status\": \"High Risk\", \"priority\": \"high\"}";
            clearLCD();
            displayMessage(" RED Alert Send To", "Firstaid Department");
            digitalWrite(buzzer,HIGH);
          } else if (i == 2) {
            message = "{\"Section\": \"section 2\",  \"status\": \"High Risk\", \"priority\": \"high\"}";
            clearLCD();
            displayMessage(" RED Alert Send To", "Technical Department");
            digitalWrite(buzzer,HIGH);
          } else if (i == 3) {
            message = "{\"Section\": \"section 2\",  \"status\": \"High Risk\", \"priority\": \"high\"}";
            clearLCD();
            displayMessage(" RED Alert Send To", "Supervisor Department");
            digitalWrite(buzzer,HIGH);
          }
          else if (i == 4) {
            message = "{\"Section\": \"section 2\"}";
            clearLCD();
            displayMessage("section 2", "Good Condition");
            digitalWrite(buzzer,LOW);
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
          else if (i == 4) {
            client.publish(topic5, message.c_str());
          }
          Serial.println("Message sent: " + message);
        }
      }
    }
  }

}

#endif
