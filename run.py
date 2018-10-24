import subprocess
import time
import re
from fib import fib
import subprocess

def make_num(string):
	return float(string[:-1])

print("The nth term of the fibonacci sequence is defined as \nthe (n-2) term plus the (n-1) term.\n")
n_inp = input("What term of the sequence would you like to calculate naively?\n   n = ")

pattern = re.compile("\\b[1-9][0-9]*\\b")
n = re.search(pattern, n_inp).group(0)

def run_program(run, build=[]):
	'''
	takes the command line arguments to build
	and run code in some arbitrary programming
	language

	kw args:
		build -- a list of cl args to build a program

		run -- a list of cl args to run a program

	returns:
		output string
	'''
	if build:
		subprocess.call(build)
	return subprocess.check_output(run)

def print_runtime(time, lang):
	'''
	takes the running time and language and prints
	to the terminal

	kw args:
		time (string) -- time in seconds

		lang (string) -- the corresponding language
			name
	'''
	# print time
	print("Running time in {}:".format(lang))
	print("    ", make_num(time), "seconds")
	print()

# retrive running times
ctime = run_program(['./fib', n], ['gcc', '-o', 'fib', 'fib.c'])
javatime = run_program(['java', 'Fib', n], ['javac', 'Fib.java'])
jstime = run_program(['node', 'fib.js', n])
gotime = run_program(['./fib', n, 'cd', '../../..'], ['cd', 'go/src/fib', '&&', 'go', 'build'])

# retrieve running time in Python
start = time.time()
fib(int(n))
end = time.time()

print()
print("-"*40)
print("Naive Recursive Fibonacci for n = {}".format(n))
print("-"*40)
print()

# print C time
print_runtime(ctime, "C")

# print java time
print_runtime(javatime, "Java")

# print JavaScript time
print_runtime(jstime, "JavaScript")

# print Go time
print_runtime(gotime, "Go")

# print Python time
print("Running time in Python:")
print("    ", end - start, "seconds")
print()