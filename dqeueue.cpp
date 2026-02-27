#include <iostream>
using namespace std;

#define SIZE 5

class Deque {
    int arr[SIZE];
    int front;
    int rear;

public:
    Deque() {
        front = -1;
        rear = -1;
    }

    // Check if full
    bool isFull() {
        return (front == 0 && rear == SIZE - 1) || (front == rear + 1);
    }

    // Check if empty
    bool isEmpty() {
        return (front == -1);
    }

    // Insert at Front
    void insertFront(int value) {
        if (isFull()) {
            cout << "Deque is Full\n";
            return;
        }

        if (front == -1) { // First element
            front = rear = 0;
        }
        else if (front == 0) {
            front = SIZE - 1;
        }
        else {
            front--;
        }

        arr[front] = value;
    }

    // Insert at Rear
    void insertRear(int value) {
        if (isFull()) {
            cout << "Deque is Full\n";
            return;
        }

        if (front == -1) { // First element
            front = rear = 0;
        }
        else if (rear == SIZE - 1) {
            rear = 0;
        }
        else {
            rear++;
        }

        arr[rear] = value;
    }

    // Delete from Front
    void deleteFront() {
        if (isEmpty()) {
            cout << "Deque is Empty\n";
            return;
        }

        cout << "Deleted from front: " << arr[front] << endl;

        if (front == rear) { // Only one element
            front = rear = -1;
        }
        else if (front == SIZE - 1) {
            front = 0;
        }
        else {
            front++;
        }
    }

    // Delete from Rear
    void deleteRear() {
        if (isEmpty()) {
            cout << "Deque is Empty\n";
            return;
        }

        cout << "Deleted from rear: " << arr[rear] << endl;

        if (front == rear) {
            front = rear = -1;
        }
        else if (rear == 0) {
            rear = SIZE - 1;
        }
        else {
            rear--;
        }
    }

    // Display
    void display() {
        if (isEmpty()) {
            cout << "Deque is Empty\n";
            return;
        }

        cout << "Deque elements: ";

        int i = front;
        while (true) {
            cout << arr[i] << " ";
            if (i == rear)
                break;
            i = (i + 1) % SIZE;
        }

        cout << endl;
    }
};

int main() {
    Deque dq;

    dq.insertRear(10);
    dq.insertRear(20);
    dq.insertFront(5);
    dq.display();

    dq.deleteFront();
    dq.display();

    dq.deleteRear();
    dq.display();

    return 0;
}