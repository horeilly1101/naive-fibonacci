import java.util.*;

public class Play {

  public static ArrayList<Integer> sort(ArrayList<Integer> list) {
    list.sort(Comparator.comparing(Integer::new));
    return list;
  }

  public static Boolean isSorted(ArrayList<Integer> list) {
    int previous = Integer.MIN_VALUE;
    for (int i : list) {
      if (i < previous) {
        return false;
      }
      previous = i;
    }
    return true;
  }

  public static Long fib(Long i) {
    return (i == 0 || i == 1) ? 1 : fib(i - 1) + fib(i-2);
  }

  public static void main(String[] args) {
    long startTime = System.nanoTime();
    fib(Long.parseLong(args[0]));
    long endTime   = System.nanoTime();
    long totalTime = endTime - startTime;

    // convert from nanoseconds
    System.out.println(totalTime * Math.pow(10, -9));

  }
}
