#!/bin/bash

while true
do
    out=$(cipher_solver ciphertext.txt)
    if [[ "$out" =~ "$1" ]]; then
        echo "$out"
        exit
    fi
done
