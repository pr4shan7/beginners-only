/*
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?

 */
public class Problem_7 {
	
   public static boolean isPrime(long n) {
        
      if (n < 2) {return false;}
        else if (n == 2) {return true;}
	        
      for (int i = 3; i < Math.sqrt(n) + 1; i+=2)
            { if (n % i == 0)
             
            {return false;}
            
            }
	        return true;
        }
        
        
   public static void main(String[] args) {
	  
	   int a=1;
	  
	   for(int i=3;i>0;i= i+=2)
	  
	   {
	   	   if(isPrime(i)==true)
		  
	   	   {
			a++;
	   	   }
		  
	   	   if(a==10001)
		   
	   	   {
			System.out.println(i);
			break;
		   }
	   }

  }

}


