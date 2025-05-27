#ifndef MQTT_CONNECTION_H
#define MQTT_CONNECTION_H

#include <PubSubClient.h>
#include "time_connection.h"  // Include the time connection file
#include "I2C_LCD.h"

// MQTT credentials
const char* mqtt_server = "test.mosquitto.org";
const char* mqtt_username = "Anuga";
const char* mqtt_password = "1020Anuga";
const char* client_id = "esp8266-client-id";
const int mqtt_port = 1883;

// Topics
const char* topic1 = "Fire";
const char* topic2 = "First_Aid";
const char* topic3 = "Technical";
const char* topic4 = "Other";
const char* topic5 = "rfid_restore";
const char* hod_fire_topic = "HOD_fire";  // New topic for HOD_Fire
const char* hod_firstaid_topic = "HOD_firstaid";  // New topic for HOD_Fire

WiFiClient espClient;
PubSubClient client(espClient);

void callback(char* topic, byte* payload, unsigned int length) {
    Serial.print("Message received on topic: ");
    Serial.println(topic);

    // Convert payload to a string
    String message;
    for (unsigned int i = 0; i < length; i++) {
        message += (char)payload[i];
    }

    Serial.print("Payload: ");
    Serial.println(message);

    // Handle messages from the HOD_Fire topic
    if (strcmp(topic, hod_fire_topic) == 0) {
        Serial.println("Message from HOD_Fire topic:");
        Serial.println(message);
          
            clearLCD();
            displayMessage(" Fire Departmeent", "On Action");
          
        // You can add additional logic here to handle the message
        // For example, display the message on the LCD
        
    }

    if (strcmp(topic, hod_firstaid_topic) == 0) {
        Serial.println("Message from HOD_FirstAid topic:");
        Serial.println(message);
       
            clearLCD();
            displayMessage(" FirstAid Departmeent", "On Action");
          
        // You can add additional logic here to handle the message
        // For example, display the message on the LCD
        
    }
}

void setupMQTT() {
    client.setServer(mqtt_server, mqtt_port);
    client.setCallback(callback);  // Ensure you handle incoming messages

    // Connect to MQTT and subscribe to topics
    if (client.connect(client_id)) {
        Serial.println("MQTT connected!");
        client.subscribe(hod_fire_topic);  // Subscribe to HOD_Fire topic
        Serial.println("Subscribed to HOD_Fire topic");
    } else {
        Serial.println("Failed to connect to MQTT");
    }
}

void reconnectMQTT() {
    while (!client.connected()) {
        Serial.println("Connecting to MQTT...");
        displayMessage("Connecting to", "MQTT........");

        if (client.connect(client_id)) {
            Serial.println("MQTT connected!");
            clearLCD();
            displayMessage("MQTT...!", "Connected");

            // Resubscribe to topics after reconnecting
            client.subscribe(hod_fire_topic);
            Serial.println("Resubscribed to HOD_Fire topic");
        } else {
            Serial.print("Failed, rc=");
            Serial.print(client.state());
            Serial.println(" trying again in 5 seconds");
            clearLCD();
            displayMessage("MQTT...!", "Failed");
            delay(5000);
        }
    }
}

#endif