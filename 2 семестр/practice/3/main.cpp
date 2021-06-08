#include <iostream>

class A
{
private:
    int a;
    double b;
    char c;
    long long d;

public:
    A(int x, double y, char t, long long z) : a(x), b(y), c(t), d(z){};
};

int &get_a(A &a) {
    return *(int*)(&a);
}


double &get_b(A &a) {
    return *(double*)((int*)(&a) + 2);
}


char &get_c(A &a) {
    return *(char*)((int*)(&a) + 4);
}

long long &get_d(A &a) {
    return *(long long*)((int*)(&a) + 6);
}

void put_a(int x, A&a){
    *(int*)(&a) = x;
}

void put_b(double x, A&a){
    *(double*)((int*)(&a) + 2) = x;
}
void put_c(char x, A&a){
    *(char*)((int*)(&a) + 4) = x;
}
void put_d(long long x, A&a){
    *(long long*)((int*)(&a) + 6) = x;
}

int main()
{
    A a(1,2,'a',4);
    std::cout<<get_a(a)<<std::endl;
    std::cout<<get_b(a)<<std::endl;
    std::cout<<get_c(a)<<std::endl;
    std::cout<<get_d(a)<<std::endl;
    put_d(5, a);
    put_a(10, a);
    put_b(11, a);
    put_c('b', a);
    std::cout<<get_a(a)<<std::endl;
    std::cout<<get_b(a)<<std::endl;
    std::cout<<get_c(a)<<std::endl;
    std::cout<<get_d(a)<<std::endl;


    return 0;
}
