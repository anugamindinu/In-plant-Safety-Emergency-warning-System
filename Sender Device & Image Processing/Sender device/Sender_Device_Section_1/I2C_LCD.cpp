#include "I2C_LCD.h"

// Define the LCD object
LiquidCrystal_I2C lcd(0x27, 16, 2); // Address, columns, rows

// Function to initialize the LCD
void initializeLCD() {
  // Initialize I2C communication
  Wire.begin();

  // Initialize the LCD
  lcd.begin(16, 2); // Specify columns and rows

  // Turn on the backlight
  lcd.backlight();
}

// Function to display a message on the LCD
void displayMessage(const char* line1, const char* line2) {
  lcd.setCursor(0, 0); // Set cursor to the first column of the first row
  lcd.print(line1);
  lcd.setCursor(0, 1); // Set cursor to the first column of the second row
  lcd.print(line2);
}

// Function to clear the LCD screen
void clearLCD() {
  lcd.clear(); // Clear the LCD screen
}