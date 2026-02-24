#include <iostream>
#include <string>
using namespace std;

int main()
{
    string key;
    cout << "Enter key: ";
    cin >> key;

    if (key.length() >= 4)
    {
        char d1 = key[1];  // 2nd digit
        char d2 = key[3];  // 4th digit
        
        int index = (d1 - '0') * 10 + (d2 - '0');
        
        cout << "Hash Index: " << index;
    }
    else
    {
        cout << "Key too small!";
    }

    return 0;
}