
/*
   Doing binary exponentiation of integers

   ONLY WORKS ON POSITIVE EXPONENTS
 */



#include <iostream>
#define ll long long
using namespace std;




int main(){

	ll n,k;

	cout<<"Enter the number and the exponent : "<<endl;
	cin>>n>>k;

	ll answer=1;

	while(k>0)
	{
		if(k&1)
			answer *= n;
		n *= n;
		k >>= 1;
	}

	cout<<"The answer is : "<<answer<<endl;
	

	return 0;
}
