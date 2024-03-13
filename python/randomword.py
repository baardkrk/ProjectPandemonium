from numpy.random import choice
from random import uniform

# Actually, could train a HMM for this...

start_frequencies = {
    'a': 5.7, 'b': 6.0, 'c': 9.4, 'd': 6.1, 'e': 3.9, 'f': 4.1, 
    'g': 3.3, 'h': 3.7, 'i': 3.9, 'j': 1.1, 'k': 1.0, 'l': 3.1, 
    'm': 5.6, 'n': 2.2, 'o': 2.5, 'p': 7.7, 'q': 0.59, 'r': 6.1, 
    's': 11.1, 't': 5.1, 'u': 2.91, 'v': 1.51, 'w': 2.71, 'x': 0.06, 
    'y': 0.37, 'z': 0.25
}

letter_frequencies = {
    'a': 7.8, 'b': 2.0, 'c': 4.0, 'd': 3.8, 'e': 11.0, 'f': 1.4, 
    'g': 3.0, 'h': 2.3, 'i': 8.6, 'j': 0.21, 'k': 0.97, 'l': 5.3, 
    'm': 2.7, 'n': 7.2, 'o': 6.1, 'p': 2.8, 'q': 0.19, 'r': 7.3, 
    's': 8.7, 't': 6.7, 'u': 3.3, 'v': 1.0, 'w': 1.01, 'x': 0.37, 
    'y': 1.70, 'z': 0.55
}

letters = list(letter_frequencies.keys())
sf = [x/100.0 for x in start_frequencies.values()]
lf = [x/100.0 for x in letter_frequencies.values()]
vowles = 'aeiou'


def draw_calc(word, draw, multiplier, check1, check2):
    prob = 1.0
    n = 0
    for c in reversed(word):
        if check1(c):
            break
        n += 1
    if check2(draw):
        prob = multiplier**n
    if uniform(0, 1) < prob or prob == 1.0:
        return True
    return False


def pick_letter(word):
    f = sf if len(word) == 0 else lf
    draw = choice(letters, 1, p=f)[0]
    if len(word) < 2:
        return draw

    drawn = False
    while not drawn:
        draw = choice(letters, 1, p=f)[0]

        consonants = draw_calc(word, draw, 0.4, 
            lambda x: x in vowles, 
            lambda x: x not in vowles)
        consecutive = draw_calc(word, draw, 0.4,
                                lambda x: x == word[-1],
                                lambda x: True)
        drawn = consonants and consecutive

    return draw


w = ''
for i in range(9):
    w = w + pick_letter(w)

print(w)
