const { PerformanceObserver, performance } = require('perf_hooks');

function fib(i) {
	// computes ith element of fibonacci sequence
	return (i == 0 || i == 1) ? 1 : fib(i - 1) + fib(i-2);
}

// time the function
const start = performance.now()
fib(process.argv[2])
const end = performance.now()

console.log((end - start) / 1000)