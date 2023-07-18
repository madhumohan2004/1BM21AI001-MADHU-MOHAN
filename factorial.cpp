
#include<iostream>
using namespace std;

class factorial{

public:
    int n;
    int fact(int n){
    if(n==0||n==1){
        return 1;
    }
    else{
        return n*fact(n-1);
    }
    }

};



int main(){
    factorial t;
    int n;
    cout<<"Enter a number : ";
    cin>>t.n;
    int res=t.fact(t.n);
    cout<<"factorial of "<<t.n<<" is "<<res;


}
