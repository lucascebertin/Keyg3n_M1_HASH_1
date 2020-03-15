#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

asciiSum=0x3e7
letters=b'0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def generateKey():
    key = ''
    asciiCount = 0x0

    for keyLetter in range(10):
        randomKey = letters[random.randrange(0, len(letters))]
        asciiCount = asciiCount + randomKey
        key = key + chr(randomKey)

    return asciiCount, key

def main():
    count = 0
    someKey = ''

    while(count <= asciiSum):
        count, someKey = generateKey()

    print(someKey)

main()
