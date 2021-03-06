class Particle{

    private: 
    double t, x, y, vx, vy;
    double dt = 0.01;
    double g = -9.81;
    
    double evolve();

    public:
        Particle(double v, double theta, double x0, double y0);
        //~Particle();

        double range();
        double time();

};