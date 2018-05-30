// Binary Tree Structure Intro

#include<stdio.h>
#include<stdlib.h>

typedef struct Btree{
    int data;
    struct Btree *left, *right;
} BinaryTree;

BinaryTree* NewNode(int val) {
    BinaryTree* newtree = (BinaryTree*)malloc(sizeof(BinaryTree));
    newtree->data = val;
    newtree->left = newtree->right = NULL;
    return newtree;
}
int main() {
    
    BinaryTree* root = NewNode(1);
    root->left = NewNode(2);
    root->right = NewNode(3);
    return 0;
}