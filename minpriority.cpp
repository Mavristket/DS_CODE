#include <iostream>
using namespace std;

#define SIZE 10

int pq[SIZE];
int n = 0;

// Insert element
void insert(int value) {
    if (n == SIZE) {
        cout << "Queue is Full\n";
        return;
    }
    pq[n++] = value;
}

// Delete highest priority (smallest element)
void deleteMin() {
    if (n == 0) {
        cout << "Queue is Empty\n";
        return;
    }

    int minIndex = 0;

    // Find smallest element
    for (int i = 1; i < n; i++) {
        if (pq[i] < pq[minIndex]) {
            minIndex = i;
        }
    }

    cout << "Deleted element: " << pq[minIndex] << endl;

    // Shift elements left
    for (int i = minIndex; i < n - 1; i++) {
        pq[i] = pq[i + 1];
    }

    n--;
}

// Display queue
void display() {
    cout << "Queue elements: ";
    for (int i = 0; i < n; i++) {
        cout << pq[i] << " ";
    }
    cout << endl;
}

int main() {
    insert(10);
    insert(50);
    insert(30);
    insert(20);

    display();

    deleteMin();
    display();

    return 0;
}