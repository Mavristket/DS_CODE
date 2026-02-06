#include <iostream>
using namespace std;

void findMin(int a[], int k, int n, int &loc) {
    int min = a[k];
    loc = k;

    for (int j = k + 1; j < n; j++) {
        if (min > a[j]) {
            min = a[j];
            loc = j;
        }
    }
}

void selection(int a[], int n) {
    for (int k = 0; k < n - 1; k++) {
        int loc;
        findMin(a, k, n, loc);

        int temp = a[k];
        a[k] = a[loc];
        a[loc] = temp;

        cout << "Pass " << k + 1 << ": ";
        for (int i = 0; i < n; i++) {
            cout << a[i] << " ";
        }
        cout << endl;
    }
}

int main() {
    int n = 7;
    int a[7];

    cout << "Enter the array elements:\n";
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    selection(a, n);

    return 0;
}

