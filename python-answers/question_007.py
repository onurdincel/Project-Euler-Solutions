# 
# Solution to Project Euler problem 7
# Copyright (c) Süleyman Onur Dinçel. All rights reserved.
# 
# https://github.com/onurdincel/Project-Euler-Solutions
# 

"""By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?"""

def calculate():
    answer = 2
    index = 1
    prime_list = [2]
    while True:
        if index == 10001:
            break
        else:
            answer = next_prime(answer+1,prime_list)
            index+=1
            prime_list.append(answer)
    return str(answer)

def next_prime(n,list):
    for i in list:
        if (n % i  == 0):
            n+=1
            return next_prime(n,list)
    return n

if __name__ == "__main__":
    print(calculate())