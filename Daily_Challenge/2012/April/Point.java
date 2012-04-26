public class Point implements Runnable {
    private double x;
    private double y;
    private double relDist;
    private Point neighbor;
    private Point[] array;

    public Point (double x, double y) {
        this.x = x;
        this.y = y;
        relDist = Double.MAX_VALUE;
    }

    public double getX(){
        return x;
    }

    public double getY() {
        return y;
    }

    public double relativeDist (Point b) {
        return ((this.getX() - b.getX()) * (this.getX() - b.getX())) + ((this.getY() - b.getY()) * (this.getY() - b.getY()));
    }

    public void setArray (Point[] array) {
        this.array = array;
    }

    public Point getNeighbor () {
        return neighbor;
    }

    public double getDist () {
        return relDist;
    }

    @Override
        public String toString() {
        return "(" + x + ", " + y + ")";
    }

    @Override
        public void run() {
        double posDist;
        for (Point b : array) {
            posDist = relativeDist(b);
            if (posDist < relDist) {
                if (this == b) {
                    continue;
                }
                
                relDist = posDist;
                neighbor = b;
            }
        }
    }
}