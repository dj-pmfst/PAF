#include <iostream>
#include <cmath>

using namespace std;

string f(double x1, double y1, double x2, double y2, double r){
    string tocka;

    if (pow(x1 - x2, 2) + pow(y1-y2, 2) < pow(r, 2))
        tocka = "Točka se nalazi unutar kružnice.";
    else if (pow(x1 - x2, 2) + pow(y1-y2, 2) > pow(r, 2))
        tocka = "Točka se nalazi izvan kružnice.";
    else
        tocka = "Točka se nalazi na kružnici.";
    return tocka;
}

int main()
{
    cout <<f(1,2,3,4,5)<< endl;
    return 0;
}