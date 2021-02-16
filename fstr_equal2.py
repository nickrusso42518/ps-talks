#!/usr/bin/env

def factorial(n):
    total = 0
    for i in range(n):
        print(f"{i=}, {total=}")
        total *= i + 1
        print(f"{i=}, {total=}")
    return total

print(factorial(3))
print(factorial(5))
