#include <Particle.h>
#include <iostream>

using  namespace std;

int main(){
    Particle p1(100, 45, 0, 0);
    Particle p2(10, 60, 0, 0);

    p1.range();
    p1.time();

    p2.range();
    p2.time();
} 