#include <iostream>
using namespace std;

int main() {
    int tableSize = 10;
    int hashTable[10];

    // Initialize table with -1 (means empty)
    for(int i = 0; i < tableSize; i++) {
        hashTable[i] = -1;
    }

    int n, key;
    cout << "Enter number of elements: ";
    cin >> n;

    for(int i = 0; i < n; i++) {
        cout << "Enter key: ";
        cin >> key;

        int index = key % tableSize;

        hashTable[index] = key;
    }

    cout << "\nHash Table:\n";
    for(int i = 0; i < tableSize; i++) {
        cout << i << " --> " << hashTable[i] << endl;
    }

    return 0;
}