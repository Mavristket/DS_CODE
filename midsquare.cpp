#include <iostream>
using namespace std;

int midSquareHash(int key)
{
    long long square = key * key;   // Step 1: square the key
    
    string str = to_string(square); // Convert to string
    
    int len = str.length();
    int mid = len / 2;              // Find middle position
    
    // Take middle digit (for simplicity, 1 digit)
    int index = str[mid] - '0';
    
    return index;
}

int main()
{
    int key;
    
    cout << "Enter key: ";
    cin >> key;
    
    int result = midSquareHash(key);
    
    cout << "Index value is: " << result;
    
    return 0;
}