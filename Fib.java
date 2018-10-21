import java.util.*;

public class Fib {
  /*
  * Implements a naive recursive implementation of the
  * fibonacci sequence. fib(i) returns the ith element
  * of the sequence. (Note: we assume that 1 is the 0th
  * and 1st element.)
  */
  public static Long fibNaive(Long i) {
    return (i == 0 || i == 1) ? 1 : fibNaive(i - 1) + fibNaive(i-2);
  }

  public static int fibDP(int i) {
    int[] a;
    a = new int[i + 1];
    a[0] = 1;
    a[1] = 1;
    for (int j = 0; j <= i; j++) {
      a[j] = a[j - 1] + a[j - 2];
    }
    return a[i];
  }

  public static void main(String[] args) {
  	// keep track of time
    long startTime = System.nanoTime();

    // execute program
    fibNaive(Long.parseLong(args[0]));
    long endTime   = System.nanoTime();
    long totalTime = endTime - startTime;

    // convert from nanoseconds
    System.out.println(totalTime * Math.pow(10, -9));

  }
}
