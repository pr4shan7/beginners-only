#include<stdio.h>

int main(void)
{
	long long int n , m = 0, dec = 0, r = 1;
	int x , y;
	scanf("%lld %d %d", &n, &x, &y);		//input number n in base x to be converted to base y
	dec = dec + ( n % 10);
	for(int i = 1; n > 0; i++)
	{
		r = r * x;
		n = n / 10;
		dec = dec + (r * (n % 10 ));
	}
	n = 1;
	for(int i = 1; dec > 0; i++)
	{
		r = dec % y;
		dec = dec / y;
		m = m + (r * n);
		n = n * 10;
	}
	printf("%lld", m);				//output number in base y
	return 0;
}
