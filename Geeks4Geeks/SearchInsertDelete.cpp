#include<iostream>
using namespace std;
int SpaceAvailable(int A[],int n,int a,int sizeofarray)
{
	if (sizeofarray > n)
	{
		A[n] = a;	
		n = n+1;
	}
	return 1;
}
int Print(int A[],int n)
{
	for(int i=0;i<=n;i++)
	{
		cout<<A[i];
	}
	return 1;
}

int main ()
{
int A[20] = {1,2,3,4,5};
int sizeofarray = sizeof(A)/sizeof(A[0]);
int a, n = 5;
// cout<<"Enter the number of elements in the Array";
// cin>>n;
cout<<"Enter the element to be inserted";
cin>>a;
int x = SpaceAvailable(A,n,a,sizeofarray);
int y = Print(A, n);
return 1;
}

