// Insertion in a Binary Tree

#include<stdio.h>
#include<malloc.h>
#define bool int
typedef struct btnode {
    int val;
    struct btnode *left, *right;
} Btree;

typedef struct Queue {
    struct btnode **array;
    int front, rear, size;
    unsigned capacity;
} Queue;

// Queue function delete, insert, empty, create, rear, front;

Queue* createQueue(int capacity) {
    Queue *queue = (Queue*)malloc(sizeof(Queue));

    queue->front = queue->size = 0;
    queue->capacity = capacity;
    queue->rear = capacity-1;
    queue->array = (Btree**)malloc(sizeof(Btree*) * queue->capacity);
    return queue;
} 

int isFull(Queue* queue) {
    return (queue->size == queue->capacity); 
}

int isEmpty(Queue *queue) {
    return (queue->size == 0);
}

void enqueue(Queue *queue, Btree *btnode) {
    if (isFull(queue)) return;

    queue->rear = (queue->rear+1)%queue->capacity;
    queue->array[queue->rear] = btnode;
    queue->size += 1;
        
}

Btree *dequeue(Queue *queue) {
    if (isEmpty(queue)){  return; }
    
    Btree *temp = (queue->array[queue->front]);
    queue->front = (queue->front+1)%queue->capacity;
    queue->size -= 1;
    return temp;
}

Btree *newNode(int val) {
    Btree *node = (Btree*)malloc(sizeof(Btree));
    node->val = val;
    node->left = node->right = NULL;
    return node;
}

void insert(Btree* root, int val) {
    if (root == NULL) {
        root = newNode(val);
        return;
    }
    Queue *queue = createQueue(100);
    enqueue(queue, root);
    
    while(!isEmpty(queue)) {
        Btree *temp = dequeue(queue);
        //printf("%d ", temp->val);
        if (!temp->left) {
            temp->left = newNode(val);
            break;
        } else {
            enqueue(queue, temp->left);
        }

        if (!temp->right) {
            temp->right = newNode(val);
            break;
        } else {
            enqueue(queue, temp->right);
        }
    }

}

void inorder(Btree* root) {
    if (root) {
        inorder(root->left);
        printf("%d ", root->val);
        inorder(root->right);
    }
}

void printQueueDetail(Queue *queue) {
    int i = queue->size;

    printf("Size of Queue: %d.\nCapacity of Queue: %d\nFront of Queue: %d\nRear of Queue: %d.\nValue of Front and Rear: %d %d", queue->size, queue->capacity, queue->array[queue->front]->val, queue->array[queue->rear]->val, queue->front, queue->rear);
    for(i = queue->front; i <= queue->rear; (i++)%queue->capacity) {
        printf("%d ", queue->array[i]->val);
    }
}
int main(int argc, char const *argv[])
{
    Btree *root = newNode(1);
    
    root->left = newNode(2);
    root->right = newNode(3);
    insert(root, 4);
    insert(root, 5);
    insert(root, 6);
    insert(root, 7);
    inorder(root);
    printf("\n");
    return 0;
}
