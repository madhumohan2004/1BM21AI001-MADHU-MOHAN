#include<iostream>
using namespace std;

class tower{
public :
    int n;
    void toh(int num,char A,char B,char C){
    if(num>0){
    toh(num-1, A, C, B);
    cout<<"Move a disk "<<num<<" from "<<" "<<A<<" to"<<" "<<C<<endl;
    toh( num-1, B, A, C);
  }
}
}t;


int main(){

  cout<<"Enter the no. of disks"<<endl;
  cin>>t.n;

  t.toh(t.n,'A','B','C');//A is the source tower , C is destination tower ,B is auxiliary tower
  cout<<endl;
}
