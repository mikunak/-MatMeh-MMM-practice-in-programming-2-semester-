#include <iostream>
#include <vector>

using namespace std;


inline int parent(int i) {
    return i >> 1;
}

inline int left_child(int i) {
    return i << 1;
}

inline int right_child(int i) {
    return (i << 1) + 1;
}


template<class T>
void heapify(vector<T>& t, int cur, int offset) {

    if (cur + offset > t.size())
        return;

    heapify(t, left_child(cur), offset);
    heapify(t, right_child(cur), offset);

    if(cur > 1 && t[cur + offset - 1] < t[parent(cur) + offset - 1])
        swap(t[cur + offset - 1], t[parent(cur) + offset - 1]);

}

template<class T>
void heap_sort(vector<T>& t) {
    for (int i = 0; i < t.size(); ++i) {
        heapify<T>(t, 1, i);
    }
}


template<class T>
void print(vector<T>& t) {
    for (auto i = t.begin(); i != t.end(); ++i)
        cout << *i << " ";
    cout << endl;

}


int main()
{
    vector<int> t;
    t.push_back(9);
    t.push_back(8);
    t.push_back(6);

    vector<string> s;
    s.push_back("xxx");
    s.push_back("xx");
    s.push_back("x");

    print<int>(t);
    heap_sort<int>(t);
    print<int>(t);

    print<string>(s);
    heap_sort<string>(s);
    print<string>(s);

}
