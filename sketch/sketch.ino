#include "Arduino_RouterBridge.h"
#include <Arduino_Modulino.h>

ModulinoBuzzer buzzer;
ModulinoLatchRelay relay;

int f = 0;

void setup() {
   Modulino.begin();
   buzzer.begin();
   relay.begin();
   relay.reset();
   Bridge.begin();
   Bridge.provide("cam_flag", cam_flag);
}
void cam_flag(int state) {
   f = state;
   if(state == 0){
     relay.reset();
     buzzer.tone(5000,500);
     delay(500);
   }
   else{
     relay.set();
   }
 }

void loop() {
 cam_flag(f);
}
