/*
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

 */
public class Problem_3 {

	public static void main(String[] args) {
		
		long i = 1;
	    long n = 600851475143l;
	    long x = 0;
	       
	       for (i = 1; i <= n; i++) {
	           
	           if (n % i == 0) {n = n/i; x = i;}
	         
	       }  
	           System.out.println(x);

	}

}
