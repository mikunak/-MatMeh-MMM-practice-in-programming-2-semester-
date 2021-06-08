#include <iostream>

template <typename A, typename B> class pair;
template <typename A, typename B> std::ostream& operator<<( std::ostream&, const pair<A, B>&);

template<typename A, typename B>
class pair
{
public:
    A first;
    B second;
    pair();
    pair(A data1, B data2);
    pair<A, B>& operator=(pair<A, B> &p);
    friend std::ostream& operator<< <A, B>(std::ostream &out, const pair<A, B> &p);
};

template<typename A, typename B>
pair<A, B>::pair()
{
    first = NULL;
    second = NULL;
};

template<typename A, typename B>
pair<A, B>::pair(A data1, B data2)
{
    first = data1;
    second = data2;
};

template<typename A, typename B>
pair<A, B>& pair<A, B>::operator=(pair<A, B> &p)
{
    first = p.first;
    second = p.second;
    return * this;
}

template<typename A, typename B>
std::ostream& operator<<(std::ostream &out, const pair<A, B> &p)
{
    out << p.first << ", " << p.second << std::endl;
    return out;
};

int main() {
    pair <int, char> q(5, 'h');
    std::cout << q;
    return 0;
}
