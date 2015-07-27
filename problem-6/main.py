#!/usr/bin/env python3
# Too easy in python3

sum_ = 0
sum_of_squares = 0
for i in range(1, 101):
    sum_ += i
    sum_of_squares += i * i
square_of_sums = sum_ * sum_
print(abs(square_of_sums - sum_of_squares))
