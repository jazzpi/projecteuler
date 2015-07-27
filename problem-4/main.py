#!/usr/bin/env python3
from math import floor

max_palindrome = 0
min_number = 1
for i in range(1, 1000):
    if i < min_number:
        continue
    for j in range(min_number, 1000):
        if j < min_number:
            continue
        product = i * j
        if product < max_palindrome:
            continue
        str_ = str(product)
        if str_ == str_[::-1]:
            max_palindrome = product
            min_number = floor(product / 999)
print(max_palindrome)
