// Inorder Traversal without recursion 

#include<stdio.h>
#include<malloc.h>
#define bool int

typedef struct tnode {
    int val;
    struct tnode *left, *right;
} BinaryTree;

typedef struct snode {
    BinaryTree* node;
    struct snode *next;
} Stack;

BinaryTree* newNode(int val) {
    BinaryTree* newnode = (BinaryTree*)malloc(sizeof(BinaryTree));
    newnode->val = val;
    newnode->left = newnode->right = NULL;
    return newnode;
}
Stack* newSnode(BinaryTree* node) {
    Stack* newsnode = (Stack*)malloc(sizeof(Stack));
    newsnode->node = node; 
    newsnode->next = NULL;
    return newsnode;
}
void push(Stack** head, BinaryTree* btnode) {
    Stack* node = newSnode(btnode);
    node->next = *head;
    *head = node;
}
bool isEmpty(Stack* head) {
    return (head == NULL)? 1 : 0;
}
BinaryTree* pop(Stack** head) {
    BinaryTree* res;
    Stack* top;

    if (isEmpty(*head)) {
        printf("Stack Underflow\n");
        getchar();
        exit(0);
    } else {
        top = *head;
        res = top->node;
        *head = top->next;
        free(top);
        return res;
    }
}

void printInorder(BinaryTree* btnode) {
    Stack* stack = NULL;
    BinaryTree* current = btnode;
    bool done = 0;
    while(!done) {
        if (current != NULL) {
            push(&stack, current);
            current = current->left;
        } else {
            if (!isEmpty(stack)) {
                current = pop(&stack);
                printf("%d ", current->val);

                current = current->right;
            } else {
                done = 1;
            }
        }
    }
}
int main(int argc, char const *argv[])
{
    BinaryTree* root    = newNode(1);
    root->left          = newNode(2);
    root->right         = newNode(3);
    root->left->left    = newNode(4);
    root->left->right   = newNode(5);

    printf("Inorder is:\n");
    printInorder(root);
    printf("\n");
    return 0;
}

