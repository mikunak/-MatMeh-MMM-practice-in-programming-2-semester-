#include <algorithm>
using namespace std;

void bubblesort(int* l, int* r) {
	int sz = r - l;
	if (sz <= 1) return;
	bool b = true;
	while (b) {
		b = false;
		for (int* i = l; i + 1 < r; i++) {
			if (*i > *(i + 1)) {
				swap(*i, *(i + 1));
				b = true;
			}
		}
		r--;
	}
}

void shakersort(int* l, int* r) {
	int sz = r - l;
	if (sz <= 1) return;
	bool b = true;
	int* beg = l - 1;
	int* end = r - 1;
	while (b) {
		b = false;
		beg++;
		for (int* i = beg; i < end; i++) {
			if (*i > *(i + 1)) {
				swap(*i, *(i + 1));
				b = true;
			}
		}
		if (!b) break;
		end--;
		for (int* i = end; i > beg; i--) {
			if (*i < *(i - 1)) {
				swap(*i, *(i - 1));
				b = true;
			}
		}
	}
}

void combsort(int* l, int* r) {
	int sz = r - l;
	if (sz <= 1) return;
	double k = 1.2473309;
	int step = sz - 1;
	while (step > 1) {
		for (int* i = l; i + step < r; i++) {
			if (*i > *(i + step))
				swap(*i, *(i + step));
		}
		step /= k;
	}
	bool b = true;
	while (b) {
		b = false;
		for (int* i = l; i + 1 < r; i++) {
			if (*i > *(i + 1)) {
				swap(*i, *(i + 1));
				b = true;
			}
		}
	}
}

void insertionsort(int* l, int* r) {
	for (int *i = l + 1; i < r; i++) {
		int* j = i;
		while (j > l && *(j - 1) > *j) {
			swap(*(j - 1), *j);
			j--;
		}
	}
}

void selectionsort(int* l, int* r) {
	for (int *i = l; i < r; i++) {
		int minz = *i, *ind = i;
		for (int *j = i + 1; j < r; j++) {
			if (*j < minz) minz = *j, ind = j;
		}
		swap(*i, *ind);
	}
}
