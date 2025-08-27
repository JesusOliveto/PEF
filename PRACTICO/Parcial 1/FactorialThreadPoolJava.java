import java.math.BigInteger;
import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.Callable;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;

public class FactorialThreadPoolJava {
    public static void main(String[] args) throws InterruptedException, ExecutionException {
        int n = 100;
        ExecutorService executor = Executors.newFixedThreadPool(Runtime.getRuntime().availableProcessors());
        List<Callable<BigInteger>> tasks = new ArrayList<>();
        for (int i = 1; i <= n; i++) {
            final int num = i;
            tasks.add(() -> factorial(num));
        }
        long start = System.currentTimeMillis();
        List<Future<BigInteger>> results = executor.invokeAll(tasks);
        long end = System.currentTimeMillis();
        for (int i = 0; i < n; i++) {
            System.out.println((i+1) + "! = " + results.get(i).get());
        }
        System.out.println("Tiempo total usando ThreadPoolExecutor: " + (end - start) / 1000.0 + " segundos");
        executor.shutdown();
    }

    public static BigInteger factorial(int n) {
        BigInteger result = BigInteger.ONE;
        for (int i = 2; i <= n; i++) {
            result = result.multiply(BigInteger.valueOf(i));
        }
        return result;
    }
}
