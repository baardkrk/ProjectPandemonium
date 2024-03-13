/*
  Morse
  
  A small program that can blink an arduino LED in
  morse code. 

  Author:
  Bård-Kristian Krohg
  2021.12.06
  
  https://baardkrk.github.io/
*/


void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
}


void long_on() {
  digitalWrite(LED_BUILTIN, HIGH);
  delay(1000);
  digitalWrite(LED_BUILTIN, LOW);
  delay(500);
}


void short_on() {
  digitalWrite(LED_BUILTIN, HIGH);
  delay(500);
  digitalWrite(LED_BUILTIN, LOW);
  delay(500);
}


void 
blink_sequence(short int a)
{
  bool start_sequence = false;
  for (int i = (sizeof(short int) * 8) -1; i >= 0; i--) {
    if (start_sequence) {
      if (a & (1u << i)) {
        long_on();
      } else {
        short_on();
      }
    } else {
      start_sequence = a & (1u << i) ? true : false;
    }
  }
  delay(500);
}


void loop() {
  blink_sequence(morse_sequence(';'));
  delay(100);
}
