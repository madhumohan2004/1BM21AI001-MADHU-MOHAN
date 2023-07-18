#include <iostream>
using namespace std;

class fibo{
    public:
        int n;

int fib(int n) {
   if((n==1)||(n==0)) {
      return n;

   }else {
      return (fib(n-1)+fib(n-2));
   }
}

}t;

int main(){

   cout << "Enter the number of terms of series : ";
   cin >> t.n;
   cout << "\nFibonnaci Series : ";
   for(int i=0;i<n;i++) {
      cout << " " << t.fib(i);
   }
   return 0;
}
