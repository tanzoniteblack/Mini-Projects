public class Hard40 {
    //private static final int arraySize = 10000;


    public static Point[] pointArray (int arraySize){
        Point[] array = new Point[arraySize];
        for (int x = 0; x < arraySize; x++) {
            array[x] = new Point(Math.random(), Math.random());
        }

        return array;
    }

    public static double relativeDist (Point a, Point b) {
        return ((a.getX() - b.getX()) * (a.getX() - b.getX())) + ((a.getY() - b.getY()) * (a.getY() - b.getY()));
    }

    public static void main(String[] args) {
        int arraySize = new Integer(args[0]);
        Point[] array = pointArray(arraySize);
        double minDist = Double.MAX_VALUE;
        Point pointA = null;
        Point pointB = null;

        double relDist;
        for (Point a : array) {
            for (Point b : array) {
                relDist = relativeDist(a, b);
                if (relDist < minDist) {
                    pointA = a;
                    pointB = b;
                }
            }
        }

        System.out.println("The closest points are: " + pointA + " and " + pointB + " with a distance of " + Math.sqrt(minDist));
    }
}