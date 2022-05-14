#include <HarmonicOscillator.h>
#include <iostream>
#include <math.h>
#include <cmath>
#include <fstream>
using namespace std;

void HarmonicOscillator::oscillate(){
    double n;
    double t_;
    n = t2/dt;
    std::ofstream podaci;
    podaci.open("podaci.txt");
    
    // cout << t2 << " " << dt << " " << n << endl;

    for(int i=0; i < n; i++){
        a = (-1)*(k2/m2)*x;
        v = v + a*dt; 
        x = x + v*dt;
        t_ = dt*i;

        
        // cout << a << " " << v << " " << x << " " << t_ << endl;
        podaci << a << "," << v << "," << x << "," << t_ << "\n";
    }
 
}

HarmonicOscillator::HarmonicOscillator(double k, double m, double v0, double x0, double t){
    k2 = k;
    m2 = m;
    v = v0;
    x = x0;
    t2 = t;
}