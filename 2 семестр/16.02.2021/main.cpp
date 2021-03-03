#include <iostream>
#include "library.h"
#include <cstring>

using namespace std;

int main()
{
    int n;
    cin >> n;
    int *a = new int[n];
    for(int i = 0; i < n; i++){
        cin >> a[i];
    }
    int *l = & a[0];
    int *r = (& (a[n - 1])) + 1;
    char s[20];
    cin >> s;
    if (strcmp(s, "bubblesort") == 0) {
        bubblesort(l, r);
    }
    if (strcmp(s, "shakersort") == 0) {
        shakersort(l, r);
    }
    if (strcmp(s, "combsort") == 0) {
        combsort(l, r);
    }
    if (strcmp(s, "selectionsort") == 0) {
        selectionsort(l, r);
    }
    if (strcmp(s, "insertionsort") == 0) {
        insertionsort(l, r);
    }
    for(int i = 0; i < n; i++){
        cout << a[i];
    }
    delete a;
    return 0;
}
