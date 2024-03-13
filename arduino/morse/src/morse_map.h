#include <ctype.h>

/*
 * Returns the morse sequence for a character
 * . := 0
 * - := 1
 * The morse sequence has leading 'zeros', and starts
 * with the first 'one'. For example:
 * 0000 0000 0000 0101 := A  (0x5)
 */
short int
morse_sequence(char a)
{
  char b = toupper(a);
  switch(b) {
    case ('A') : return 0x5;  // 
    case ('B') : return 0x18;  // 
    case ('C') : return 0x1A;  // 
    case ('D') : return 0xC;  // 
    case ('E') : return 0x2;  // 
    case ('F') : return 0x12;  // 
    case ('G') : return 0xE;  // 
    case ('H') : return 0x10;  // 
    case ('I') : return 0x4;  // 
    case ('J') : return 0x17;  // 
    case ('K') : return 0xD;  // 
    case ('L') : return 0x14;  // 
    case ('M') : return 0x7;  // 
    case ('N') : return 0x6;  // 
    case ('O') : return 0xF;  // 
    case ('P') : return 0x16;  // 
    case ('Q') : return 0x1D;  // 
    case ('R') : return 0xA;  // 
    case ('S') : return 0x8;  // 
    case ('T') : return 0x3;  // 
    case ('U') : return 0x9;  // 
    case ('V') : return 0x11;  // 
    case ('W') : return 0xB;  // 
    case ('X') : return 0x19;  // 
    case ('Y') : return 0x1B;  // 
    case ('Z') : return 0x1C;  // 
    case ('Æ') : return 0x15;  // 
    case ('Ø') : return 0x1E;  // 
    case ('Å') : return 0x2D;  // 
    case ('1') : return 0x2F;  // 
    case ('2') : return 0x27;  // 
    case ('3') : return 0x23;  // 
    case ('4') : return 0x21;  // 
    case ('5') : return 0x20;  // 
    case ('6') : return 0x30;  // 
    case ('7') : return 0x38;  // 
    case ('8') : return 0x3C;  // 
    case ('9') : return 0x3E;  // 
    case ('0') : return 0x3F;  // 
    case ('.') : return 0x55;  // 
    case (',') : return 0x73;  // 
    case (':') : return 0x78;  // 
    case ('?') : return 0x4C;  // 
    case ('-') : return 0x61;  // 
    case ('=') : return 0x31;  // 
    case ('/') : return 0x32;  // 
    case ('(') : return 0x36;  // 
    case (')') : return 0x6D;  // 
    case ('+') : return 0x2A;  // 
    case ('^') : return 0x35;  // Start
    case ('$') : return 0x2A;  // Stopp
    case ('#') : return 0x100;  // Correction
    case ('%') : return 0x22;  // Understood
    case ('*') : return 0x45;  // Ending
    case ('~') : return 0x28;  // Wait
    case (';') : return 0x238;  // Emergency
    case ('!') : return 0x26;  // 
    case ('@') : return 0x5A;  // 
    case ('Ü') : return 0x13;  // 
    case ('È') : return 0x24;  // 
    case ('É') : return 0x24;  // 
    default : return 0x0;
  }
}


void 
print_morse_sequence(short int a)
{
  printf("");
  bool start_sequence = false;
  for (int i = (sizeof(short int) * 8) -1; i >= 0; i--) {
    if (start_sequence) {
      putchar(a & (1u << i) ? '-' : '.');
    } else {
      start_sequence = a & (1u << i) ? true : false;
    }
  }
  printf("\n");
}
