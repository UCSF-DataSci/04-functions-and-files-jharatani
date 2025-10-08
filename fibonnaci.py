#!/usr/bin/env python3
"""
Fibonacci Sequence

Create a program that generates Fibonacci numbers less than a limit and writes them to a file. The _Fibonacci_ sequence is a sequence in which each number is the sum of the two preceding ones: 

`0, 1, 1 (0+1), 2 (1+1), 3 (2+1), 5 (3+2), ...`

	- Use a function to generate Fibonacci numbers as a list
	- Use `with` statements for file operations
	- Handle potential file I/O errors with `try`/`except`
	- Use command-line arguments (via `argparse`) to specify the upper limit and output file name

Task: Generate the Fibonacci numbers less than 100 and write them to `fibonacci_100.txt`
"""

import argparse

def fibonnaci_sequence(limit):
	# Generate Fibonacci numbers less than the given limit.
	nums = [0,1]
	while nums[-1] +nums[-2] < limit:
		nums.append(nums[-1] + nums[-2])
	return nums

def main():
	parser = argparse.ArgumentParser(description="Generate Fibonacci numbers less than a limit and write them to a file.")
	parser.add_argument("limit", type=int, help="Upper limit for Fibonacci numbers")
	parser.add_argument("output_file", type=str, help="Output file name")
	args = parser.parse_args()

	fibs = fibonnaci_sequence(args.limit)

	try:
		with open(args.output_file, 'w') as f:
			for n in fibs:
				f.write(str(n) + "\n")
		print(f"Fibonacci numbers less than {args.limit} written to {args.output_file}")
	except IOError as e:
		print(f"An error occurred while writing to the file: {e}")

if __name__ == "__main__":
	main()
