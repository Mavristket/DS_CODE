#include <iostream>
using namespace std;

int foldingHash(int key, int tableSize)
{
    int sum = 0;

    while (key > 0)
    {
        sum += key % 100;   // Take last 2 digits
        key = key / 100;    // Remove last 2 digits
    }

    return sum % tableSize; // Final index
}

int main()
{
    int key, tableSize;

    cout << "Enter key: ";
    cin >> key;

    cout << "Enter table size: ";
    cin >> tableSize;

    int index = foldingHash(key, tableSize);

    cout << "Hash Index is: " << index;

    return 0;
}