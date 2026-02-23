
#include <iostream>
#include <cmath>
using namespace std;

int hashFunction(int key, int m)
{
    double A = 0.618;              // constant value
    double value = key * A;        // Step 1: multiply
    double fractional = value - floor(value);  // Step 2: take decimal part
    int index = floor(m * fractional);         // Step 3 & 4

    return index;
}

int main()
{
    int key, m;

    cout << "Enter key: ";
    cin >> key;

    cout << "Enter table size: ";
    cin >> m;

    int result = hashFunction(key, m);

    cout << "Index value is: " << result;

    return 0;
}