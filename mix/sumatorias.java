package mix;

import java.util.Scanner;

public class sumatorias {
	public static void main(String[] args){
		//Para leer por teclado, archivos
		Scanner sc = new Scanner(System.in);

		int n = sc.nextInt();
		int x = sc.nextInt();

		double s = 0;
		boolean b = false;

		for (int i = 1; i < (n + 1); i = i + 1) {
			double expo = Math.pow(2, i);
			int deno = 1;

			for (int j = 1; j < i * 2; j++) {
				deno = deno * j;
			}

			if (b == false){
				s = s - Math.pow(x,expo) / deno;
				b = true;
			}
			else {
				s = s + Math.pow(x, expo) / deno;
				b = false;
			}
		}
		System.out.println(s);
	}
}
