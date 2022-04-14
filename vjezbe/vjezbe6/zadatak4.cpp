#include <iostream>
#include <cmath>
using namespace std;

void f(float a1, float b1, float a2, float b2, float c1, float c2){
    float x, y;

    if ((a1 != 0 || b1 != 0) && (a2 != 0 || b2 != 0)){

        x = ((c2 - (b2*c1)/b1)/(a2*b1 - a1*b2))*b1;
        y = (c1 - a1*x)/b1;

        cout << x << "  "<< y << endl; 
    }
    else{
        cout << "nema rjesenja" << endl;
    }
}

int main(){
    f(0,2,3,2,4,5);
}