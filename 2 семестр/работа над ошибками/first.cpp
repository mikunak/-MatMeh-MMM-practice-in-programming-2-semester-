#include <iostream>
#include <cstdlib>
using namespace std;

class AoA
{
    size_t m;
    int** A;
    int* data;
public:
    AoA(int* Array_k, size_t m);
    ~AoA();
    AoA(const AoA& A);
    const AoA& operator=(const AoA& A);
    int get(size_t i, size_t j);
    void put(size_t i, size_t j, int val);
};

AoA::AoA(int* Array_k, size_t m): m(m), A(new int* [m])
{
    size_t size = 0;
    for (int i = 0; i < m; i++) size += Array_k[i];
    data = new int[size];
    int temp = 0;
    for (int i = 0; i < m; i++)
    {
        A[i] = data + temp;
        temp += Array_k[i];
    }
}

int AoA::get(size_t i, size_t j)
{
    if (i >= m) throw "Out of m";
    if (j >= (size_t)(A[i] - A[i + 1])) throw "Out of k[i]";
    return A[i][j];
}

AoA::~AoA()
{
    delete[] A;
    delete[] data;
}

void AoA::put(size_t i, size_t j, int x)
{
    A[i][j] = x;
}


int main() {
    int *A = new int[10];
    for(int i = 0; i < 10; i++)
    {
            A[i] = rand() % 100;
    }
    size_t size = 10;
    AoA temp(A, size);
    for (int i = 0; i < size; i++)
    {
        for (int j = 0; j < A[i]; j++) temp.put(i, j, rand() % 100);
    }
    for (int i = 0; i < size; i++)
    {
        cout << A[i] << ' ';
        for (int j = 0; j < A[i]; j++)
        {
            cout << temp.get(i, j) << ' ';
        }
        cout << "\n";
    }

    return 0;
}
