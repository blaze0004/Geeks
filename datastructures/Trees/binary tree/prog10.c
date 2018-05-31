// Finding inorder successor and predecessor of a btree
// Incomplete problem at line 75

#include<stdio.h>
#include<malloc.h>

typedef struct btnode {
    int val;
    struct btnode *left, *right;
} BinaryTree;

typedef struct vectorNode{
    int val;
    struct vectorNode *prev, *next;
} Vector;


Vector* start, *end;

Vector* newVector() {
    start = (Vector*)malloc(sizeof(Vector));
    start->val = 0;
    start->prev = NULL;
    end = (Vector*)malloc(sizeof(Vector));
    start->next = end;
    end->next = 0;
    end->prev = start;
    end->val = 0;
    return start;
}


void insertAfterVector(int val, Vector* start) {
    Vector* newnode = (Vector*)malloc(sizeof(Vector));
    newnode->val = val;
    newnode->next = end;
    newnode->prev = end->prev;
    end->prev->next = newnode;
    end->prev = newnode;
    return;
}
BinaryTree* newNode(int val) {
    BinaryTree* temp = (BinaryTree*)malloc(sizeof(BinaryTree));
    temp->val = val;
    temp->left = temp->right = NULL;
    return temp;
}

Vector* inorder(BinaryTree* root, Vector* vector) {
    if (root == NULL) return;

    inorder(root->left, vector);
    //printf("%d ", root->val);
    insertAfterVector(root->val, vector);
    inorder(root->right, vector);

    return vector;
}

void printPreorder(Vector* start) {
   Vector* temp = start;
   while(temp) {
       printf("%d ", temp->val);
       temp = temp->next;
    }
    printf("\n");
}

void replaceNodeWithSum(BinaryTree* root, Vector* vector) {
    static Vector* vect = NULL;
    vect = start;
    if (root == NULL) {
        return;
    } 

    replaceNodeWithSum(root->left, vector);
    root->val = (vect->val) + (vect->next->next->val);
    vect = vect->next;
    replaceNodeWithSum(root->right, vector);
}

void printInorder(BinaryTree* root) {
    if (!root) return;
    printInorder(root->left);
    printf("%d ", root->val);
    printInorder(root->right);
}
/*
0 4 2 5 1 6 3 7 0


                 1
               /   \
              2     3
            /  \  /  \
           4   5  6   7
 */


int main() {
    BinaryTree* root = newNode(1);
    root->left = newNode(2);
    root->right = newNode(3);
    root->left->left = newNode(4);
    root->left->right = newNode(5);
    root->right->left = newNode(6);
    root->right->right = newNode(7);
    Vector* vector = newVector();
    Vector* in = inorder(root, vector);
    printPreorder(in);
    Vector* temp = in;
    replaceNodeWithSum(root, temp);
    printInorder(root);
    printf("\n");
    return 0;
}