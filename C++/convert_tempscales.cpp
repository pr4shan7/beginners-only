/*

Program that takes inputs of freezing and boling points of water in a temperature scale and converts the current temperature in that scale to the celsius scale

*/




#include <iostream>

using namespace std;

int main()
{

	double l1,u1;	// freezing and boiling points of water in the given scale
	double t,T;	
	
	cout<<"Enter the freezing and boiling points of water in given scale : "<<endl;
	cin>>l1>>u1;
	cout<<"Enter the current temperature in given scale : "<<endl;
	cin>>T;	
	
	

	t=((T-l1)*(100)/(u1-l1))+0;

	cout<<"The current temperature in celsius scale is : "<<t<<endl;

	return 0;
}
