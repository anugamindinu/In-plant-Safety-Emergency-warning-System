#include <ESP8266WebServer.h>
#include <ESP8266HTTPClient.h>
#include <SPI.h>
#include <MFRC522.h>
#include <ArduinoJson.h>
#include <Wire.h>
#include <LiquidCrystal_I2C.h>

#define SS_PIN D8
#define RST_PIN D0
MFRC522 mfrc522(SS_PIN, RST_PIN);

const char* ssid = "IT21388620";
const char* password = "Ishubaba";

ESP8266WebServer server(80);
WiFiClient client;

int readsuccess;
byte readcard[4];
char str[32] = "";
String StrUID;

LiquidCrystal_I2C lcd(0x27, 16, 4);

void setup() {
  Serial.begin(115200);
  SPI.begin();
  mfrc522.PCD_Init();
  lcd.init();
  lcd.backlight();

  delay(500);

  WiFi.begin(ssid, password);
  Serial.println("");

  pinMode(LED_BUILTIN, OUTPUT);
  digitalWrite(LED_BUILTIN, HIGH);

  Serial.print("Connecting");
  while (WiFi.status() != WL_CONNECTED) {
    Serial.print(".");
    digitalWrite(LED_BUILTIN, LOW);
    delay(250);
    digitalWrite(LED_BUILTIN, HIGH);
    delay(250);
    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("Wait For Moment");
    lcd.setCursor(0, 1);
    lcd.print("Connecting To Network");
  }
            lcd.clear();
            lcd.setCursor(2, 0);
            lcd.print("Programmer");
            lcd.setCursor(1, 1);
            lcd.print("Tap Your Card ");

  digitalWrite(LED_BUILTIN, HIGH);
  Serial.println("");
  Serial.print("Successfully connected to : ");
  Serial.println(ssid);
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());
  Serial.println("Please tag a card or keychain to see the UID !");
  Serial.println("");
}

void loop() {
  readsuccess = getid();

  if (readsuccess) {
    digitalWrite(LED_BUILTIN, LOW);
    HTTPClient http;
    http.begin(client, "http://172.28.12.10/SLIIT/getUID.php");
    http.addHeader("Content-Type", "application/x-www-form-urlencoded");

    String UIDresultSend, postData;
    UIDresultSend = StrUID;
    postData = "UIDresult=" + UIDresultSend;

    int httpCode = http.POST(postData);
    String payload = http.getString();

    Serial.println(UIDresultSend);
    Serial.println(httpCode);
    Serial.println(payload);

    http.end();
    delay(1000);
    digitalWrite(LED_BUILTIN, HIGH); //display status
            lcd.clear();
            lcd.setCursor(0, 0);
            lcd.print("New Card Tapped");
            lcd.setCursor(1, 1);
            lcd.print("Sending ......");
            delay(3000);
                        lcd.clear();
            lcd.setCursor(3, 0);
            lcd.print("Programmer");
            lcd.setCursor(1, 1);
            lcd.print("Tap Your Card ");

  }
}

int getid() {
  if (!mfrc522.PICC_IsNewCardPresent()) {
    return 0;
  }
  if (!mfrc522.PICC_ReadCardSerial()) {
    return 0;
  }

  Serial.print("THE UID OF THE SCANNED CARD IS : ");

  for (int i = 0; i < 4; i++) {
    readcard[i] = mfrc522.uid.uidByte[i];
    array_to_string(readcard, 4, str);
    StrUID = str;
  }
  mfrc522.PICC_HaltA();
  return 1;
}

void array_to_string(byte array[], unsigned int len, char buffer[]) {
  for (unsigned int i = 0; i < len; i++)
  {
    byte nib1 = (array[i] >> 4) & 0x0F;
    byte nib2 = (array[i] >> 0) & 0x0F;
    buffer[i * 2 + 0] = nib1  < 0xA ? '0' + nib1  : 'A' + nib1  - 0xA;
    buffer[i * 2 + 1] = nib2  < 0xA ? '0' + nib2  : 'A' + nib2  - 0xA;
  }
  buffer[len * 2] = '\0';
}