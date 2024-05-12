public class CircularQueue {
    private String[] queue;
    private int front, rear, size;

    public CircularQueue(int size) {
        this.size = size;
        queue = new String[size];
        front = rear = -1;
    }

    // Method to add an element to the queue
    public void enqueue(String element) {
        if ((rear + 1) % size == front) {
            System.out.println("The circular queue is full");
        } else {
            if (front == -1) { // First element being added
                front = 0;
            }
            rear = (rear + 1) % size;
            queue[rear] = element;
        }
    }

    // Method to remove an element from the queue
    public String dequeue() {
        if (front == -1) {
            System.out.println("The circular queue is empty");
            return null;
        }
        String temp = queue[front];
        if (front == rear) { // Queue has only one element
            front = rear = -1;
        } else {
            front = (front + 1) % size;
        }
        return temp;
    }

    // Method to display the elements of the queue
    public void display() {
        if (front == -1) {
            System.out.println("The circular queue is empty");
        } else {
            System.out.print("Elements in the circular queue are: ");
            for (int i = front; i != rear; i = (i + 1) % size) {
                System.out.print(queue[i] + " ");
            }
            System.out.println(queue[rear]); // Print last element
        }
    }
}
