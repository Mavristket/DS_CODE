#include <iostream>
using namespace std;

class nana {
    int top = -1;
    int stack[6];
    int maxelement = 6;

public:
    void push(int item) {
        if (top == maxelement - 1) {
            cout << "Stack is overflow" << endl;
        } else {
            top++;
            stack[top] = item;
            cout << "Item added: " << item << endl;
        }
    }
};

int main() {
    nana n;
    n.push(10);
    n.push(20);
    n.push(30);
    return 0;
}

