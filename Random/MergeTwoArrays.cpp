#include<iostream>
using namespace std;
int MergeTwoArrays(int Arr[m], int Arr1[n])
{
	for(int i = 0; int j=0; i<=m; j<=n; i++;)
	{	if(Arr[i] == -1)
			{	
				if (Arr[i-1] <= A[j])
					{	
						Arr[i] = A[j];
						j = j+1;
					}
			}
	}
	
}
int CheckOrder(int Arr[m])
{
	for(int i = 0; int j = 1; i<=m; j<=m-1; i++; j++)
		{
			if(Arr[i] > Arr[j])
				{
					int temp = Arr[i]
					Arr[i] = Arr[j]
					Arr[j] = temp
				}
		}

}	

void print(int Arr[], int m)
{
	for(int i = 0; i<=m; i++)
	{
		cout<<Arr[m];
	}
}		
