# 
# Solution to Project Euler problem 3
# Copyright (c) Süleyman Onur Dinçel. All rights reserved.
# 
# https://github.com/onurdincel/Project-Euler-Solutions
# 

"""The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143?"""

def calculate():
    num = 600851475143
    answer = 1
    index = 2
    while True:
        if num % index == 0:
            num = num / index
            answer = index
        elif answer > num or index > num:
            break
        else:
            index = next_prime(index)
            if num % index != 0:
                index = next_prime(index)+1
    return str(answer)

def next_prime(n):
    for i in range(2,n):
        if (n % i) == 0:
            n+=1
            return next_prime(n)
    return n

if __name__ == "__main__":
	print(calculate())