#include <Wire.h>

#define ADDRESS 0x05

void setup() {
    Wire.begin(ADDRESS);
    Wire.onRequest(sendLightValue);
}

void loop() {
    // nothing
}

int randomNumber(int maxNumber)
{
    return rand() % maxNumber + 1;
}

void sendLightValue() {
    // Send a random number. Maximum number is 100
    Wire.write(randomNumber(100));
}