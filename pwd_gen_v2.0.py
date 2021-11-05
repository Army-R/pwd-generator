#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 18:49:30 2021

@author: Army-R
"""
# Password Generator 2.0

import string
import secrets

char = string.ascii_letters + string.punctuation + string.digits
pwd = ''.join(secrets.choice(char) for i in range(16))
print("Password generated: ", pwd)