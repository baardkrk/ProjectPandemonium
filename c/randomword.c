#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <openssl/rand.h>
//                  012345678901234567890
#define CONSONANTS "bcdfghjklmnpqrstvwxyz"
// #define VOWLSONANTS "yw"
#define VOWLES "aeiouyw"


/* Random integer in [0, limit) */
unsigned int random_uint(unsigned int limit) {
    union {
        unsigned int i;
        unsigned char c[sizeof(unsigned int)];
    } u;

    do {
        if (!RAND_bytes(u.c, sizeof(u.c))) {
            fprintf(stderr, "Can't get random bytes!\n");
            exit(1);
        }
    } while (u.i < (-limit % limit)); /* u.i < (2**size % limit) */
    return u.i % limit;
}


char
pick_letter(int char_num, char *word)
{
    int category = rand() % 2;
    int n = (int) random_uint((unsigned int) strlen((category > 0) ? VOWLES : CONSONANTS));
    char *c;
    c = (category > 0) ? &VOWLES[n] : &CONSONANTS[n];
    return *c;
}


int
main(int argc, char **argv)
{
    int num_letters = 9;
    char word [num_letters + 1];
    word[num_letters] = '\0';

    for (int i = 0; i < num_letters; i++) {
        word[i] = pick_letter(i, word);
    }

    printf("\n%s\n", word);
    return 0;
}
