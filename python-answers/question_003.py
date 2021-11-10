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
            index = prime(index)
            if num % index != 0:
                index = prime(index)
    return str(answer)

def prime(n):
    if n % 2 == 0:
        n+=1
        return n
    elif n % 2 != 0:
        n+=2
        return n
    else:
        for i in range(2,n):
            print(n)
            if (n % i) == 0:
                n =+ 2
                return n
            else:
                n =+ 1
                return n

if __name__ == "__main__":
	print(calculate())