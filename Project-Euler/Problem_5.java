/*
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

 */
public class Problem_5 {
	
public static int LCM(int n1, int n2) {
		
		int lcm = 0;
		
		for (int i = 1; i < n2; i++) {
			
			lcm = (n1 > i) ? n1 : i;
			
			 for (lcm = (n1 > i) ? n1 : i; lcm <= (n1*n2); lcm++) {
		         
				 if(lcm % n1 == 0 && lcm % i == 0){
		           
				   n1 = lcm;
		           break;
		    
			   }
		        
				 lcm += 1;
				 
		       }
		}  
	   return lcm;
	 }	
	
public static void main(String[] args) {
		
		System.out.println(LCM(1, 20));
	}
	
}