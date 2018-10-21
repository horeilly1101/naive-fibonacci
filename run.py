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

# retrieve running time in C
subprocess.call(['gcc', '-o', 'fib', 'fib.c'])
ctime = subprocess.check_output(['./fib', n])

# retrieve running time in java
subprocess.call(['javac', 'Fib.java'])
javatime = subprocess.check_output(['java', 'Fib', n])

# retrieve running time in js
jstime = subprocess.check_output(['node', 'fib.js', n])

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
print("Running time in C:")
print("    ", make_num(ctime), "seconds")
print()

# print java time
print("Running time in Java:")
print("    ", make_num(javatime), "seconds")
print()

# print JavaScript time
print("Running time in JavaScript:")
print("    ", make_num(jstime), "seconds")
print()

# print Python time
print("Running time in Python:")
print("    ", end - start, "seconds")
print()