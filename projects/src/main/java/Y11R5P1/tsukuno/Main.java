package Y11R5P1.tsukuno;

import java.util.*;

public class Main {

  public static void main(String args[]) {
    (new Main()).exec();
  }

  void solve(int w, int l, int u, int g, int pos[][]) {

    double bound[] = new double[w+1];

    int px = pos[0][0];
    int py = pos[0][1];

    for(int i=1; i<l; ++i) {

      int nx = pos[i][0];
      int ny = pos[i][1];

      double div = nx - px;

      for(int j=px+(i == 1 ? 0 : 1); j<=nx; ++j) {
        bound[j] -= (ny - py) / div * (j - px) + py;
      }

      px = nx;
      py = ny;

    }

    px = pos[l][0];
    py = pos[l][1];

    for(int i=l+1; i<l+u; ++i) {

      int nx = pos[i][0];
      int ny = pos[i][1];

      double div = nx - px;

      for(int j=px+(i == l + 1 ? 0 : 1); j<=nx; ++j) {
        bound[j] += (ny - py) / div * (j - px) + py;
      }

      px = nx;
      py = ny;

    }

    double sum = 0.0;
    for(int i=0; i<w; ++i) {
      sum += (bound[i] + bound[i+1]) / 2.0;
    }

    double req = sum / g;

    double cur = 0.0;
    int p = 0;
    double used = 0.0;

    while( g > 1 ) {

      double a = bound[p];
      double b = bound[p+1];

      double add = ((b - a) * used + a + b) * (1.0 - used) / 2.0;

      if( cur + add >= req ) {

        double hi = 1.0;
        double lo = used;

        for(int j=0; j<100; ++j) {
          double mi = (hi + lo) / 2.0;
          double cand = ((b - a) * used + a + (b - a) * mi + a) * (mi - used) / 2.0;
          if( cur + cand >= req ) { hi = mi; }
          else { lo = mi; }
        }

        System.out.println(p + hi);
        cur = 0.0;
        used = hi;
        --g;

      }

      else {
        cur += add;
        ++p;
        used = 0.0;
      }

    }

  }

  void exec() {

    Scanner cin = new Scanner(System.in);

    int t = cin.nextInt();

    for(int c=1; c<=t; ++c) {

      int w = cin.nextInt();
      int l = cin.nextInt();
      int u = cin.nextInt();
      int g = cin.nextInt();

      int pos[][] = new int[l+u][2];
      for(int i=0; i<l+u; ++i) {
        pos[i][0] = cin.nextInt();
        pos[i][1] = cin.nextInt();
      }

      System.out.println("Case #" + c + ":");
      solve(w, l, u, g, pos);

    }

  }

}
