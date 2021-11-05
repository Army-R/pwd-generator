#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 20:58:09 2021

@author: Army-R
"""
# My own password generator

import secrets
import string

def char():
    
    characters = string.ascii_letters + string.punctuation + string.digits

    password = []

    for i in range(16):
        random_characters = secrets.choice(characters)
        password.append(random_characters)

    password = "".join(password)
    return password

def main():
    password = char()
    print("Password generated: " + password)

if __name__ == "__main__":
    main()
