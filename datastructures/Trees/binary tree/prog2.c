// DFS (Inorder, preorder, postorder) traversal of tree

#include<stdio.h>
#include<malloc.h>

typedef struct node {
    int val;
    struct node *left, *right;
} BinaryTree;

BinaryTree* newNode(int val) {
    BinaryTree* newnode = (BinaryTree*)malloc(sizeof(BinaryTree));
    newnode->val = val;
    newnode->left = newnode->right = NULL;
    return newnode;
}

void printInorder(BinaryTree* node) {
    if (node == NULL) {
        return;
    } 

    printInorder(node->left);
    printf("%d ", node->val);
    printInorder(node->right);
}


void printPreorder(BinaryTree* node) {
    if (node == NULL) {
        return;
    } 
    printf("%d ", node->val);
    printPreorder(node->left);
    printPreorder(node->right);
}
void printPostorder(BinaryTree* node) {
    if (node == NULL) {
        return;
    } 
    printPostorder(node->left);
    printPostorder(node->right);
    printf("%d ", node->val);
}


 
int main(int argc, char const *argv[])
{
    BinaryTree* root    = newNode(1);
    root->left          = newNode(2);
    root->right         = newNode(3);
    root->left->left    = newNode(4);
    root->left->right   = newNode(5);
    root->right->left   = newNode(6);
    root->right->right  = newNode(7);

    printf("PreOrder: \n");
    printPreorder(root);
    printf("\nInorder: \n");
    printInorder(root);
    printf("\nPostorder: \n");
    printPostorder(root);
    printf("\n");
    return 0;
}
