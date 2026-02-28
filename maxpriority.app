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

// Delete highest priority (largest element)
void deleteMax() {
    if (n == 0) {
        cout << "Queue is Empty\n";
        return;
    }

    int maxIndex = 0;

    // Find largest element
    for (int i = 1; i < n; i++) {
        if (pq[i] > pq[maxIndex]) {
            maxIndex = i;
        }
    }

    cout << "Deleted element: " << pq[maxIndex] << endl;

    // Shift elements left
    for (int i = maxIndex; i < n - 1; i++) {
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

    deleteMax();
    display();

    return 0;
}