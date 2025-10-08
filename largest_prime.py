#!/usr/bin/env python3
"""
Largest Prime Fibonacci Number

Write a program that takes a number as an argument, finds the *Fibonacci* numbers less than that number, and prints the largest prime number in the list. 

	- Use command-line arguments to specify the upper limit 
	- Implement a function to check if a number is prime
	- Import and use the Fibonacci generating function from problem 1 as a module

Task: Find the largest prime Fibonacci number less that 50000
"""

import argparse
from fibonnaci import fibonnaci_sequence

def is_prime(n):
	# Check if a number is prime.
	if n <= 1:
		return False
	for i in range(2, int(n**0.5) + 1):
		if n % i == 0:
			return False
	return True

	d = 3
	while d * d <= n:
		if n % d == 0:
			return False
		d += 2
	return True

def main():
	parser = argparse.ArgumentParser(description="Find the largest prime Fibonacci number less than a given limit.")
	parser.add_argument("limit", type=int, help="Upper limit for Fibonacci numbers")
	args = parser.parse_args()

	fibs = fibonnaci_sequence(args.limit)
	prime_fibs = [n for n in fibs if is_prime(n)]

	if prime_fibs:
		largest_prime_fib = max(prime_fibs)
		print(f"The largest prime Fibonacci number less than {args.limit} is {largest_prime_fib}")
	else:
		print(f"There are no prime Fibonacci numbers less than {args.limit}")

	print(max(prime_fibs))

if __name__ == "__main__":
	main()