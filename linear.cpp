#include <iostream>
#include <ctime>
using namespace std;

int search(int arr[], int N, int x)
{
    int flag=-1;
    clockid_t time_req;
	time_req = clock();
    for (int i = 0; i < N; i++){
        if (arr[i] == x)
            flag=i;
    }
    time_req = clock() - time_req;
	cout << "The Operation took " << (double)time_req/CLOCKS_PER_SEC << " seconds" << endl;

    return flag;
}

int main(void)
{
    int arr[] = { 2, 3, 4, 10, 40,50,90,100,110,5,1,99 };
    int x = 99;
    int N = sizeof(arr) / sizeof(arr[0]);

    // Function call
    int result = search(arr, N, x);
    (result == -1)
        ? cout << "Element is not present in array"
        : cout << "Element is present at index " << result;

    return 0;
}
