#!/usr/bin/env python3

import sys
from cipher_solver.simple import SimpleSolver

def inside(stringlist,plaintext):
    if all([x in plaintext for x in stringlist]):
        return True
    return False

def main(args):
    print(args)
    what_to_look_for=args[1:]
    print(f"{what_to_look_for=}")
    with open(args[0],'r') as file:
        ciphertext = file.read()
        print(f"{ciphertext=}")

        while 1:
            s = SimpleSolver(ciphertext)
            s.solve()
            plaintext = s.plaintext()
            if inside(what_to_look_for, plaintext):
                print(f"{s.plaintext()=}")
                print(f"{s.decryption_key()=}")
                exit

            d = SimpleSolver(ciphertext)
            d.solve(method="deterministic")
            plaintext = d.plaintext()
            if inside(what_to_look_for, plaintext):
                print(f"{d.plaintext()=}")
                print(f"{d.decryption_key()=}")
                exit

if __name__ == "__main__":
    main(sys.argv[1:])
