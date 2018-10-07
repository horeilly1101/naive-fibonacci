import java.util.*;

public class Fib {
  /*
  * Implements a naive recursive implementation of the
  * fibonacci sequence. fib(i) returns the ith element
  * of the sequence. (Note: we assume that 1 is the 0th
  * and 1st element.)
  */
  public static Long fib(Long i) {
    return (i == 0 || i == 1) ? 1 : fib(i - 1) + fib(i-2);
  }

  public static void main(String[] args) {
  	// keep track of time
    long startTime = System.nanoTime();

    // execute program
    fib(Long.parseLong(args[0]));
    long endTime   = System.nanoTime();
    long totalTime = endTime - startTime;

    // convert from nanoseconds
    System.out.println(totalTime * Math.pow(10, -9));

  }
}
