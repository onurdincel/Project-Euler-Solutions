# 
# Solution to Project Euler problem 4
# Copyright (c) Süleyman Onur Dinçel. All rights reserved.
# 
# https://github.com/onurdincel/Project-Euler-Solutions
# 

"""A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers."""

def calculate():
    answer = 0
    for i in range(100,1000):
        for j in range(100,1000):
            index = str(i*j)
            if index == index[::-1]:
                if int(index) > int(answer):
                    answer = index
    return str(answer)

if __name__ == "__main__":
	print(calculate())