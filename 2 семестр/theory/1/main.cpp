#include <iostream>
using namespace std;


struct array {
private:
    int* data;
	size_t size;
public:
	array()
    {
        size = 0;
        data = NULL;
    }

	array(size_t Size)
    {
        size = Size;
        data = new int[size];
    }

    ~array()
    {
        delete [] data;
    }

	array& operator =(const array& a)
	{
        if(data) delete[] data;
        size = a.size;
        data = new int[size];
        for(int i=0; i<size; i++)
            data[i] = a.data[i];
        return *this;
    }

	int& operator[](size_t i)
	{
        return data [i % size];
    }
};

int main() {
	int size;
	cin >> size;
	array a(size);
	for (int i = 0; i < size; i++)
		cin >> a[i];
	int k;
	cin>> k;
    cout << a[k - 1];
	return 0;
}
