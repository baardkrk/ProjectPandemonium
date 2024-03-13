/*
  Morse
  
  A small program that can blink an arduino LED in
  morse code. 
  Sticking to convention where:
    - A dot is a single time unit
    - A dash is three time units 
    - Inter-element gap is one time unit
    - Short gap between letters are three time units
    - Medium gap between words are seven time units

  Author:
  Bård-Kristian Krohg
  2021.12.06
  
  https://baardkrk.github.io/
*/
#include <string.h>


int TIME_UNIT = 125;

void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
}


void 
blink(int a)
{
  digitalWrite(LED_BUILTIN, HIGH);
  delay(TIME_UNIT * ((a > 0) ? 3 : 1));
  digitalWrite(LED_BUILTIN, LOW);
  delay(TIME_UNIT);
} 


void 
blink_sequence(short int a)
{
  bool start_sequence = false;
  for (int i = (sizeof(short int) * 8) -1; i >= 0; i--) {
    if (start_sequence) {
      blink(a & (1u << i) ? 1 : 0);
    } else {
      start_sequence = a & (1u << i) ? true : false;
    }
  }
  delay(TIME_UNIT * 2);  // Between letters is 3
}


void 
blink_sentence(char *s)
{
  int l = strlen(s);
  for (int i = 0; i < l; i++) {
    if (s[i] == ' ') { delay(TIME_UNIT * 4); }  // Between words is 7
    else { blink_sequence(morse_sequence(s[i])); }
  }
}


void loop() {
  char *s = "^Automatic upstream updates$";
  blink_sentence(s);
  // blink_sequence(morse_sequence(';'));
  // delay(TIME_UNIT * 4);  // Between words 7
}
