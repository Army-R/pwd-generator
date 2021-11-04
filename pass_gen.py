#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 20:58:09 2021

@author: Army-R
"""
# My own password generator

import random
import string

def char():
    upper = list(string.ascii_uppercase)

    lower = list(string.ascii_lowercase)

    special = list(string.punctuation)

    num = list(string.digits)

    character = upper + lower + special + num

    password = []

    for i in range(17):
        random_character = random.choice(character)
        password.append(random_character)

    password = "".join(password)
    return password

def main():
    password = char()
    print("Password generated: " + password)

if __name__ == "__main__":
    main()
