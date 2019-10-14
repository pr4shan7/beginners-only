#include<stdio.h>


int partition(int* a,int start,int end){		// worst O(n^2) best O(nlogn) ave O(nlogn) INplace
	int pivot=a[end],t;
	int i,pindex=start;
	for(i=start;i<end;i++){
		if(a[i]<pivot){
			t = a[pindex];
			a[pindex++] = a[i];
			a[i] = t;

		}
	}
	t = a[pindex];
	a[pindex] = a[end];
	a[end] = t;
	return pindex;
}

void quicksort(int a[],int start,int end){
	if(start<=end){
		int pindex=partition(a,start,end);
		quicksort(a,start,pindex-1);
		quicksort(a,pindex+1,end);
	}
}

int main(){
		int e[]={5,2,9,1,0,4,2,7,5,6};
	quicksort(e,0,9);
	for(int i=0;i<9;i++)
		printf("%d ",e[i]);

}
