
#include <iostream>
using namespace std;

class hcf{
    public:
    int n1,n2;

    int gcd(int n1, int n2)
{
    if (n2 != 0)
       return gcd(n2, n1 % n2);
    else
       return n1;
}

}t;

int main()
{

   cout << "Enter two positive integers: ";
   cin >>t.n1>>t.n2;

   cout << "gcd of " << t.n1 << " & " <<  t.n2 << " is: " << t.gcd(t.n1, t.n2);

}

