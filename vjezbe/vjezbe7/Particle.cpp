#include <Particle.h>
#include <math.h>
#include <cmath>
#include <iostream>
using namespace std;

double Particle::evolve(){
    while(y>=0){
        vx += 0.;
        vy += g*dt;
        x += vx*dt;
        y += vy*dt;
        t += dt;
    }
    return t;
    return x;
}

double Particle::range(){
    while(y>=0){
        evolve();
    }
    cout<< x << endl;
    return x;
}

double Particle::time(){
    while(y>=0){
        evolve();
    }
    cout<< t << endl;
    return t;
}

Particle::Particle(double v, double theta, double x0, double y0){
    theta = theta;
    v = v;
    x = x0;
    y = y0;
    t = 0;

    vx = cos(theta)*v;
    vy = sin(theta)*v;
}