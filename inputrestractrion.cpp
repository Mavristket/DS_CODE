#include <iostream>
using namespace std;

#define SIZE 5

class IRDeque {
    int arr[SIZE];
    int front, rear;

public:
    IRDeque() {
        front = -1;
        rear = -1;
    }

    bool isEmpty() {
        return (front == -1);
    }

    bool isFull() {
        return (rear == SIZE - 1);
    }

    // Insert only at Rear
    void insert(int value) {
        if (isFull()) {
            cout << "Queue is Full\n";
            return;
        }

        if (front == -1)
            front = 0;

        rear++;
        arr[rear] = value;
    }

    // Delete from Front
    void deleteFront() {
        if (isEmpty()) {
            cout << "Queue is Empty\n";
            return;
        }

        cout << "Deleted from Front: " << arr[front] << endl;
        front++;

        if (front > rear)
            front = rear = -1;
    }

    // Delete from Rear
    void deleteRear() {
        if (isEmpty()) {
            cout << "Queue is Empty\n";
            return;
        }

        cout << "Deleted from Rear: " << arr[rear] << endl;
        rear--;

        if (rear < front)
            front = rear = -1;
    }

    void display() {
        if (isEmpty()) {
            cout << "Queue is Empty\n";
            return;
        }

        for (int i = front; i <= rear; i++)
            cout << arr[i] << " ";
        cout << endl;
    }
};

int main() {
    IRDeque q;

    q.insert(10);
    q.insert(20);
    q.insert(30);

    q.display();

    q.deleteFront();
    q.display();

    q.deleteRear();
    q.display();

    return 0;
}