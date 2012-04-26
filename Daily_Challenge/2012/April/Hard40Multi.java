import java.util.concurrent.Executors;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.TimeUnit;

public class Hard40Multi {
    // private static final int arraySize = 10000;
    private static final int THREADS = Runtime.getRuntime().availableProcessors();

    public static Point[] pointArray (int arraySize){
        Point[] array = new Point[arraySize];
        for (int x = 0; x < arraySize; x++) {
            array[x] = new Point(Math.random(), Math.random());
        }

        return array;
    }

    public static void main(String[] args) {
        
        int arraySize = new Integer(args[0]);
        Point[] array = pointArray(arraySize);
        double minDist = Double.MAX_VALUE;
        Point pointA = null;
        Point pointB = null;
        double relDist = Double.MAX_VALUE;
        ExecutorService pool = Executors.newFixedThreadPool(THREADS);
    
        for (Point a : array) {
            a.setArray(array);
            pool.execute(a);
        }

        pool.shutdown();
        try {
            pool.awaitTermination(Long.MAX_VALUE, TimeUnit.NANOSECONDS);
        } catch (InterruptedException e) {
            System.err.println(e.getStackTrace());
            System.exit(-1);
        }

        for (Point a : array) {
            if (a.getDist() < relDist) {
                relDist = a.getDist();
                pointA = a;
                pointB = a.getNeighbor();
            }
        }

        System.out.println("The closest points are: " + pointA + " and " + pointB + " with a distance of " + Math.sqrt(minDist));
    }
}