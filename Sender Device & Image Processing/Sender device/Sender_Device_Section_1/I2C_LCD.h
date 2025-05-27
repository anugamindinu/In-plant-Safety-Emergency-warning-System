#ifndef I2C_LCD_H
#define I2C_LCD_H

#include <Wire.h>
#include <LiquidCrystal_I2C.h>

// Declare the LCD object
extern LiquidCrystal_I2C lcd;

// Function declarations
void initializeLCD();
void displayMessage(const char* line1, const char* line2);
void clearLCD();

#endif // I2C_LCD_H