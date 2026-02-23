#include <iostream>
using namespace std;

class Queue {
    int front, rear, size;
    int capacity;
    int* arr;

public:
    Queue(int c) {
        capacity = c;
        front = 0;
        size = 0;
        rear = -1;
        arr = new int[capacity];
    }

    // Check if queue is full
    bool isFull() {
        return (size == capacity);
    }

    // Check if queue is empty
    bool isEmpty() {
        return (size == 0);
    }

    // Enqueue (Insert)
    void enqueue(int x) {
        if (isFull()) {
            cout << "Queue is Full\n";
            return;
        }
        rear++;
        arr[rear] = x;
        size++;
        cout << x << " inserted\n";
    }

    // Dequeue (Delete)
    void dequeue() {
        if (isEmpty()) {
            cout << "Queue is Empty\n";
            return;
        }
        cout << arr[front] << " removed\n";
        front++;
        size--;
    }

    // Display queue
    void display() {
        if (isEmpty()) {
            cout << "Queue is Empty\n";
            return;
        }

        for (int i = front; i <= rear; i++) {
            cout << arr[i] << " ";
        }
        cout << endl;
    }
};

int main() {
    Queue q(5);

    q.enqueue(10);
    q.enqueue(20);
    q.enqueue(30);

    q.display();

    q.dequeue();

    q.display();

    return 0;
}