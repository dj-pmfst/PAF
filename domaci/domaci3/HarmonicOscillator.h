class HarmonicOscillator{

    private:
    //double x, v;
    double dt = 0.01;
    double a;

    public:
        HarmonicOscillator(double k, double m, double v0, double x0, double t);
        double m2, k2, v, x, t2;
    
    void oscillate();
};