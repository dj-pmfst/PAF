#include <iostream>

using namespace std;

void f(double x1, double y1, double x2, double y2){
    double a, b, c;
    string jednadzba;

    a = (y2) - (y1);
    b = (x1) - (x2);
    c = a*(x1) + b*(y1);
    jednadzba = "Jednadžba pravca je y= -(" + to_string(a/b) + ")x + " + to_string(c/b);
    cout << jednadzba<< endl;
}

int main(){
    double x1, y1, x2, y2;
    f(1,2,3,4);
    return 0;
}