#!/usr/bin/python

import random
import string

def RandomPasswordGenerator(passLen=10):
    #
    #
   # tama = input("Introduce longitud de la contraseña: ")
    print(passLen)
    if passLen == 8:
        password = "12345678"
    if passLen == 10:
        password = "1234567890"
    if passLen == 15:
        password = "123456789012345"
    #
    #

    return password

#RandomPasswordGenerator()