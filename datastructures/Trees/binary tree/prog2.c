// DFS (Inorder, preorder, postorder) traversal of tree

#include<stdio.h>
#include<malloc.h>

typedef struct node {
    int val;
    struct node *left, *right;
} 