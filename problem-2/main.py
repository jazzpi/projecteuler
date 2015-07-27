#!/usr/bin/env python3

prev1 = 1
prev2 = 1
sum_ = 0
n = prev1 + prev2
while n < 4e6:
    if not n & 1:
        sum_ += n
    prev1, prev2 = prev2, n
    n = prev1 + prev2

print(sum_)
