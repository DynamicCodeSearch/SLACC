package Y12R5P1.vinci;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.io.PrintWriter;


public class PerfectGame {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		try {
			BufferedReader br = new BufferedReader(new FileReader(args[0]));
			PrintWriter pw = new PrintWriter(args[1]);
			String line = br.readLine();
			System.out.println(line);
			int T = Integer.valueOf(line.trim());
			for (int i=0; i<T; i++)
			{
				line = br.readLine();
				System.out.println(line);
				int n = Integer.valueOf(line);
				
				line = br.readLine();
				System.out.println(line);
				String[] ss = line.trim().split(" ");
				double[] l = new double[n];
				
				for(int j=0; j<n; j++)
				{
					l[j] = Integer.valueOf(ss[j]);
				}
				
				line = br.readLine();
				System.out.println(line);
				ss = line.trim().split(" ");
				double[] d = new double[n];
				
				for(int j=0; j<n; j++)
				{
					d[j] = Integer.valueOf(ss[j]);
				}
				
				double[] exp = new double[n];
				
				for(int j=0; j<n; j++)
				{
					if(d[j] == 0)
					{
						exp[j] = 0;
					}
					else
					{
						exp[j] = l[j] * d[j] / (100 - d[j]);
					}
				}
				
				pw.print("Case #"+(i+1)+": ");
				System.out.print("Case #"+(i+1)+": ");
				for(int j=0; j<n; j++)
				{
					int pos = 0;
					for(int k=1; k<n; k++)
					{
						if(exp[k] > exp[pos])
						{
							pos = k;
						}
					}
					
					pw.print(pos+" ");
					System.out.print(pos+" ");
					exp[pos] = -1;
				}
				pw.println();
				System.out.println();
			}
			pw.close();
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

}
