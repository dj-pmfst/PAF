#include <iostream>
#include <cmath>
using namespace std;

int f(int a, int b, int niz[100]){
    int br=0;
    int manji, veci;
    if (a > b){
        manji = b;
        veci = a;
    }
    else{
        manji = a;
        veci = b;
    }
    for(int i = manji; i<= veci; i++){
       br++;
    }
    for(int i = 0; i<br;i++){
        niz[i] = manji + i;
        cout<<niz[i]<< endl;
    }
    for (int i = br-1; i >= 0; i--)
    {
        cout<<niz[i]<< endl;
    }
    return br;
}

void index(int idx1, int idx2, int niz[100], int br){
    int a, b; 
    a = niz[idx1];
    b = niz[idx2];
    niz[idx2] = a;
    niz[idx1] = b;  
    
    
    for(int i = 0; i<br; i++){
        cout << niz[i]<< endl;
    }
}

void sort(int niz[100], int br){
    for (int i = 0; i < br; i++){
        for(int j = 0; j < br; j++){
            if (niz[i] > niz[j]){
                int a;
                a = niz[i];
                niz[i] = niz[j];
                niz[j] = a;
            }
        }
    
    }
    for(int i = 0; i<br; i++){
        cout << niz[i]<< endl;
    }  
}

int main(){
    int br;
    int niz[100];
    br = f(-1, 10, niz);
    //index(1, 3, niz, br);
    sort(niz, br);
    return 0;
}