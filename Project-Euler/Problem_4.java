/*
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

 */
public class Problem_4 {

	public static void main(String[] args) {
		
        int maxProd = 0;
        
        for (int i = 999; i > 99; i--) 
        { 
            for (int j = i; j > 99; j--) 
            { 
                int prod = i * j; 
                if (prod < maxProd) 
                    break; 
                int num = prod; 
                int rev = 0; 
 
                while (num != 0) 
                { 
                    rev = rev * 10 + num % 10; 
                    num /= 10; 
                } 
 
                if (prod == rev && prod > maxProd) 
                    maxProd = prod; 
            } 
        } 
        System.out.println(maxProd);
		
	}

}
