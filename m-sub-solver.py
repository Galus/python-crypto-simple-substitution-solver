#!/usr/bin/env python3

import sys
import numpy as np
from string import ascii_lowercase, ascii_uppercase

ENGLISH_LETTER_FREQUENCIES = {
    "e": 0.1249,
    "t": 0.0928,
    "a": 0.0804,
    "o": 0.0764,
    "i": 0.0757,
    "n": 0.0723,
    "s": 0.0651,
    "r": 0.0628,
    "h": 0.0505,
    "l": 0.0407,
    "d": 0.0382,
    "c": 0.0334,
    "u": 0.0273,
    "m": 0.0251,
    "f": 0.0240,
    "p": 0.0214,
    "g": 0.0187,
    "w": 0.0168,
    "y": 0.0166,
    "b": 0.0148,
    "v": 0.0105,
    "k": 0.0054,
    "x": 0.0023,
    "j": 0.0016,
    "q": 0.0012,
    "z": 0.0009,
}

# Source: http://norvig.com/mayzner.html
# This is a (26 x 26) array containing the digram frequencies for the English language
# and is used for scoring potential solutions. The rows and columns are sorted in order
# of frequency, meaning that e.g. the element at [0, 0] corresponds to the digram "ee",
# the element at [4, 5] is the digram "in", and so on. All numbers are percentages.
# fmt: off
DIGRAM_MATRIX_ENGLISH = np.array([
    #  e      t      a      o      i      n      s      r      h      l      d      c      u      m      f      p      g      w      y      b      v      k      x      j      q      z
    [0.378, 0.413, 0.688, 0.073, 0.183, 1.454, 1.339, 2.048, 0.026, 0.530, 1.168, 0.477, 0.031, 0.374, 0.163, 0.172, 0.120, 0.117, 0.144, 0.027, 0.255, 0.016, 0.214, 0.005, 0.057, 0.005],
    [1.205, 0.171, 0.530, 1.041, 1.343, 0.010, 0.337, 0.426, 3.556, 0.098, 0.001, 0.026, 0.255, 0.026, 0.006, 0.004, 0.002, 0.082, 0.227, 0.003, 0.001, 0.000, 0.000, 0.000, 0.000, 0.004],
    [0.012, 1.487, 0.003, 0.005, 0.316, 1.985, 0.871, 1.075, 0.014, 1.087, 0.368, 0.448, 0.119, 0.285, 0.074, 0.203, 0.205, 0.060, 0.217, 0.230, 0.205, 0.105, 0.019, 0.012, 0.002, 0.012],
    [0.039, 0.442, 0.057, 0.210, 0.088, 1.758, 0.290, 1.277, 0.021, 0.365, 0.195, 0.166, 0.870, 0.546, 1.175, 0.224, 0.094, 0.330, 0.036, 0.097, 0.178, 0.064, 0.019, 0.007, 0.001, 0.003],
    [0.385, 1.123, 0.286, 0.835, 0.023, 2.433, 1.128, 0.315, 0.002, 0.432, 0.296, 0.699, 0.017, 0.318, 0.203, 0.089, 0.255, 0.001, 0.000, 0.099, 0.288, 0.043, 0.022, 0.001, 0.011, 0.064],
    [0.692, 1.041, 0.347, 0.465, 0.339, 0.073, 0.509, 0.009, 0.011, 0.064, 1.352, 0.416, 0.079, 0.028, 0.067, 0.006, 0.953, 0.006, 0.098, 0.004, 0.052, 0.052, 0.003, 0.011, 0.006, 0.004],
    [0.932, 1.053, 0.218, 0.398, 0.550, 0.009, 0.405, 0.006, 0.315, 0.056, 0.005, 0.155, 0.311, 0.065, 0.017, 0.191, 0.002, 0.024, 0.057, 0.008, 0.001, 0.039, 0.000, 0.000, 0.007, 0.000],
    [1.854, 0.362, 0.686, 0.727, 0.728, 0.160, 0.397, 0.121, 0.015, 0.086, 0.189, 0.121, 0.128, 0.175, 0.032, 0.042, 0.100, 0.013, 0.248, 0.027, 0.069, 0.097, 0.001, 0.001, 0.001, 0.001],
    [3.075, 0.130, 0.926, 0.485, 0.763, 0.026, 0.015, 0.084, 0.001, 0.013, 0.003, 0.001, 0.074, 0.013, 0.002, 0.001, 0.000, 0.005, 0.050, 0.004, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000],
    [0.829, 0.124, 0.528, 0.387, 0.624, 0.006, 0.142, 0.010, 0.002, 0.577, 0.253, 0.012, 0.135, 0.023, 0.053, 0.019, 0.006, 0.013, 0.425, 0.007, 0.035, 0.020, 0.000, 0.000, 0.000, 0.000],
    [0.765, 0.003, 0.151, 0.188, 0.493, 0.008, 0.126, 0.085, 0.005, 0.032, 0.043, 0.003, 0.148, 0.018, 0.003, 0.002, 0.031, 0.008, 0.050, 0.003, 0.019, 0.000, 0.000, 0.005, 0.001, 0.000],
    [0.651, 0.461, 0.538, 0.794, 0.281, 0.001, 0.023, 0.149, 0.598, 0.149, 0.002, 0.083, 0.163, 0.003, 0.001, 0.001, 0.001, 0.000, 0.042, 0.001, 0.000, 0.118, 0.000, 0.000, 0.005, 0.001],
    [0.147, 0.405, 0.136, 0.011, 0.101, 0.394, 0.454, 0.543, 0.001, 0.346, 0.091, 0.188, 0.001, 0.138, 0.019, 0.136, 0.128, 0.000, 0.005, 0.089, 0.003, 0.005, 0.004, 0.001, 0.000, 0.002],
    [0.793, 0.001, 0.565, 0.337, 0.318, 0.009, 0.093, 0.003, 0.001, 0.005, 0.001, 0.004, 0.115, 0.096, 0.004, 0.239, 0.001, 0.001, 0.062, 0.090, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000],
    [0.237, 0.082, 0.164, 0.488, 0.285, 0.000, 0.006, 0.213, 0.000, 0.065, 0.000, 0.001, 0.096, 0.001, 0.146, 0.000, 0.001, 0.000, 0.009, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000],
    [0.478, 0.106, 0.324, 0.361, 0.123, 0.001, 0.055, 0.474, 0.094, 0.263, 0.001, 0.001, 0.105, 0.016, 0.001, 0.137, 0.000, 0.001, 0.012, 0.001, 0.000, 0.001, 0.000, 0.000, 0.000, 0.000],
    [0.385, 0.015, 0.148, 0.132, 0.152, 0.066, 0.051, 0.197, 0.228, 0.061, 0.003, 0.000, 0.086, 0.010, 0.001, 0.000, 0.025, 0.001, 0.026, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000],
    [0.361, 0.007, 0.385, 0.222, 0.374, 0.079, 0.035, 0.031, 0.379, 0.015, 0.004, 0.001, 0.001, 0.001, 0.002, 0.001, 0.000, 0.000, 0.002, 0.001, 0.000, 0.001, 0.000, 0.000, 0.000, 0.000],
    [0.093, 0.017, 0.016, 0.150, 0.029, 0.013, 0.097, 0.008, 0.001, 0.015, 0.007, 0.014, 0.001, 0.024, 0.001, 0.025, 0.003, 0.003, 0.000, 0.004, 0.000, 0.000, 0.000, 0.000, 0.000, 0.002],
    [0.576, 0.017, 0.146, 0.195, 0.107, 0.002, 0.046, 0.112, 0.001, 0.233, 0.002, 0.002, 0.185, 0.003, 0.000, 0.001, 0.000, 0.000, 0.176, 0.011, 0.004, 0.000, 0.000, 0.023, 0.000, 0.000],
    [0.825, 0.000, 0.140, 0.071, 0.270, 0.000, 0.001, 0.001, 0.000, 0.000, 0.000, 0.000, 0.002, 0.000, 0.000, 0.000, 0.000, 0.000, 0.005, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000],
    [0.214, 0.001, 0.017, 0.006, 0.098, 0.051, 0.048, 0.003, 0.003, 0.011, 0.001, 0.000, 0.003, 0.002, 0.002, 0.001, 0.003, 0.002, 0.006, 0.001, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000],
    [0.022, 0.047, 0.030, 0.003, 0.039, 0.000, 0.000, 0.000, 0.004, 0.001, 0.000, 0.026, 0.005, 0.000, 0.002, 0.067, 0.000, 0.000, 0.003, 0.000, 0.002, 0.000, 0.003, 0.000, 0.000, 0.000],
    [0.052, 0.000, 0.026, 0.054, 0.003, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.059, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000],
    [0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.148, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000],
    [0.050, 0.000, 0.025, 0.007, 0.012, 0.000, 0.000, 0.000, 0.001, 0.001, 0.000, 0.000, 0.002, 0.000, 0.000, 0.000, 0.000, 0.000, 0.002, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.003],
])

def inside(stringlist,plaintext):
    if all([x in plaintext for x in stringlist]):
        return True
    return False

ENGLISH_ALPHABET_SIZE = 26

def main(args):
    print(f"{args=}")
    command = args[0]
    print(f"{command=}")
    if command == "sub":
        filename = args[1]
        alphabet = str(args[2])
        if len(alphabet) < ENGLISH_ALPHABET_SIZE:
            alphabet = ascii_lowercase
        subkey = str(args[3])
        if len(subkey) != len(alphabet):
            print("Alphabet and subkey length must match")
            print("Substitution",f"{filename=}",f"{alphabet=}",f"{subkey=}")
            return 1
        print("Substitution",f"{filename=}",f"{alphabet=}",f"{subkey=}")
        with open(filename, 'r') as file:
            ciphertext = file.read()
            plaintext = ""
            #ziplut = dict(sorted(zip(list(subkey),list(alphabet))))
            ziplut = dict((zip(subkey,alphabet)))
            lut = {}
            for index, character in enumerate(alphabet):
                lut[character] = subkey[index]
            print(f"{lut=}")
            print(f"{ziplut=}")
            for i,cipherletter in enumerate(ciphertext):
                #print('processing letter:',f"{cipherletter=}")
                if cipherletter.isupper():
                    plainletter = lut[cipherletter.lower()].upper()
                elif cipherletter not in lut:
                    plainletter = cipherletter
                else:
                    plainletter = lut[cipherletter]
                #print('\t replacing ', cipherletter, ' with ', plainletter)
                plaintext += plainletter
                #print('ciphertext:')
                #print(ciphertext)
                #print('plaintext:')
                #print(plaintext)
            print('ciphertext:')
            print(ciphertext)
            print('plaintext:')
            print(plaintext)
            print('alphabet:', alphabet)
            print('subkey  :', subkey)
        return 0
    else:
        print("Unknown command:", command)
        exit

if __name__ == "__main__":
    main(sys.argv[1:])
