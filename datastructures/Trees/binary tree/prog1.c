// Breath first search of a binary tree

// Method 2 (using queue) 

#include<stdio.h>
#include<stdlib.h>
#define MAX_Q_SIZE 500

typedef struct node {
    int data;
    struct node *left, *right;
} BinaryTree;

// Function prototypes

BinaryTree** createqueue(int *, int *);
void enQueue(BinaryTree**, int *, BinaryTree*);
BinaryTree *deQueue(BinaryTree**, int *);


BinaryTree* newNode(int val) {
    BinaryTree *newnode = (BinaryTree*)malloc(sizeof(BinaryTree));
    newnode->data = val;
	newnode->left = NULL;
	newnode->right = NULL;

    return newnode;
}

// Enqueue and dequeue 

BinaryTree** createqueue(int *front, int *rear) {
    BinaryTree** queue = (BinaryTree**)malloc(sizeof(BinaryTree*)*MAX_Q_SIZE);
    *front = *rear = 0; 
    return queue;
}

void enQueue(BinaryTree** queue, int *rear, BinaryTree* newnode) {
    queue[*rear] = newnode;
    (*rear)++;
}

BinaryTree* deQueue(BinaryTree** queue, int *front) {
    (*front)++;
    return queue[*front-1];
}

void printLevelOrder(BinaryTree* root) {
    int front, rear;
    BinaryTree** queue = createqueue(&front, &rear);
    BinaryTree* temp = root;

    while(temp) {
        printf("%d ", temp->data);
        
        if (temp->left) {
            enQueue(queue, &rear, temp->left);
        }

        if (temp->right) {
            enQueue(queue, &rear, temp->right);
        }

        temp = deQueue(queue, &front);
    }
    
}

int main() {
    BinaryTree* root    = newNode(1);
    root->left          = newNode(2);
    root->right         = newNode(3);
    root->left->left    = newNode(4);
    root->left->right   = newNode(5);
    root->right->left   = newNode(6);
    root->right->right  = newNode(7);

    printLevelOrder(root);
    return 0;
}
