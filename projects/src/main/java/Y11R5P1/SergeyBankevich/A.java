package Y11R5P1.SergeyBankevich;

import java.io.IOException;
import java.io.PrintWriter;
import java.util.Scanner;

public class A implements Runnable {

	public void solve() throws IOException {
		int tn = in.nextInt();
		for ( int test = 1; test <= tn; test ++ ) {
            double width = in.nextDouble();
            int l = in.nextInt();
            Point[] lb = new Point[l];
            int u = in.nextInt();
            Point[] ub = new Point[u];
            int g = in.nextInt();
            for ( int i = 0; i < l; i ++ ) {
                lb[i] = new Point( in.nextDouble(), in.nextDouble() );
            }
            for ( int i = 0; i < u; i ++ ) {
                ub[i] = new Point( in.nextDouble(), in.nextDouble() );
            }
            double area = area( lb, ub, width ) / g;
            out.println( "Case #" + test + ":" );
            for ( int i = 1; i < g; i ++ ) {
                out.println( search( lb, ub, area * i ) );
            }
		}
	}

    private double search( Point[] lb, Point[] ub, double a ) {
        double l = 0.0;
        double r = lb[lb.length - 1].x;
        for ( int i = 0; i < 100; i ++ ) {
            double x = 0.5 * ( l + r );
            double xArea = area( lb, ub, x );
            if ( xArea > a ) {
                r = x;
            } else {
                l = x;
            }
        }
        return 0.5 * ( l + r );
    }

    private double area( Point[] lb, Point[] ub, double x ) {
        double r = 0.0;
        for ( int i = 0; lb[i].x < x; i ++ ) {
            double x1 = Math.min( lb[i + 1].x, x );
            double y1 = lb[i].y + ( lb[i + 1].y - lb[i].y ) * ( x1 - lb[i].x ) / ( lb[i + 1].x - lb[i].x );
            r -= 0.5 * ( lb[i].y + y1 ) * ( x1 - lb[i].x );
        }
        for ( int i = 0; ub[i].x < x; i ++ ) {
            double x1 = Math.min( ub[i + 1].x, x );
            double y1 = ub[i].y + ( ub[i + 1].y - ub[i].y ) * ( x1 - ub[i].x ) / ( ub[i + 1].x - ub[i].x );
            r += 0.5 * ( ub[i].y + y1 ) * ( x1 - ub[i].x );
        }
        return r;
    }

    class Point {
        double x;
        double y;

        Point( double X, double Y ) {
            x = X;
            y = Y;
        }
    }

	public Scanner in;

	public PrintWriter out;

	A() throws IOException {
		in = new Scanner( System.in );
		// in = new StreamTokenizer( new InputStreamReader( System.in ) );
		out = new PrintWriter( System.out );
	}

	void close() throws IOException {
		out.close();
	}

	void check( boolean f, String msg ) {
		if ( ! f ) {
			out.close();
			throw new RuntimeException( msg );
		}
	}

	public void run() {
		try {
			solve();
			close();
		} catch ( Exception e ) {
            e.printStackTrace( out );
            out.flush();
            throw new RuntimeException( e );
		}
	}

	public static void main( String[] args ) throws IOException {
		new Thread( new A() ).start();
	}
}
