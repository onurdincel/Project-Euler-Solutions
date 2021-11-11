# 
# Solution to Project Euler problem 5
# Copyright (c) Süleyman Onur Dinçel. All rights reserved.
# 
# https://github.com/onurdincel/Project-Euler-Solutions
# 

"""2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?"""


def calculate():
    answer = 1
    for i in range(1,21):
        answer = i * answer//gcd(i,answer)
    return str(answer)

def gcd(i,j):
    if j == 0:
        return i
    return gcd(j,i%j)

if __name__ == "__main__":
	print(calculate())