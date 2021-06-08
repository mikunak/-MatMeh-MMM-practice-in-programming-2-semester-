#include <iostream>>

template <class T>
class CMatrix
{
private:
    T **data;
    int row,col;
public:
    CMatrix( int rows, int cols)
    {
        setRow(rows);
        setCol(cols);

        data = new T*[rows];

        for (int i = 0; i < row; i++) {
            data[i] = new T [cols];
        }

        for(int i = 0; i < row; i++) {
            for(int j = 0; j < cols; j++) {
                data[i][j] = (T) i * j;
            }
        }
    }
    void print();
    void setRow(int r){row = r;}
    void setCol(int c){col = c;}
    T& operator()(int row, int col);
};

template <class T>
void CMatrix<T>::print ()
{
    int i,j;

    for (i=0;i < row;i++)
    {
        for(j=0;j < col;j++)
        {
            printf("%.1f    ",(float) data[i][j]);
        }
        printf("\n");
    }
}

template<class T>
T& CMatrix<T>::operator()(int row, int col)
{
    return data[row][col];
}



int main()
{
    CMatrix <float> m(4,4);
    m.print();
    std::cout << m(1,1);

    return 0;
}
