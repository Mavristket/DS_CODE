#include <iostream>
using namespace std;

class nana {
    int top = -1;
    int stack[6];
    int maxelement = 6;

public:
    void push(int item) {
        if (top == maxelement - 1) {
            cout << "Stack Overflow" << endl;
        } else {
            top++;
            stack[top] = item;
            cout << "Item added: " << item << endl;
        }
    }

    void pop() {
        if (top == -1) {
            cout << "Stack Underflow" << endl;
        } else {
            cout << "Item removed: " << stack[top] << endl;
            top--;
        }
    }

    void display() {
        if (top == -1) {
            cout << "Stack is empty" << endl;
        } else {
            cout << "Stack elements are: ";
            for (int i = top; i >= 0; i--) {
                cout << stack[i] << " ";
            }
            cout << endl;
        }
    }
};

int main() {
    nana n;
    int choice, item;

    while (true) {
        cout << "\n--- STACK MENU ---\n";
        cout << "1. Push\n";
        cout << "2. Pop\n";
        cout << "3. Display\n";
        cout << "4. Exit\n";
        cout << "Enter your choice: ";
        cin >> choice;

        switch (choice) {
            case 1:
                cout << "Enter item to push: ";
                cin >> item;
                n.push(item);
                break;

            case 2:
                n.pop();
                break;

            case 3:
                n.display();
                break;

            case 4:
                cout << "Exiting program..." << endl;
                return 0;

            default:
                cout << "Invalid choice" << endl;
        }
    }
}
