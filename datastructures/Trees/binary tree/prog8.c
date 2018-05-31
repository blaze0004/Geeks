// Construct a btree using inorder and preorder array

#include<stdio.h>
#include<malloc.h>

typedef struct btnode {
    int val;
    struct btnode *left, *right;
} BinaryTree;

BinaryTree* newNode(int val) {
    BinaryTree* temp = (BinaryTree*)malloc(sizeof(BinaryTree));
    temp->val = val;
    temp->left = temp->right = NULL;
    return temp;
}

void printInorder(BinaryTree* root) {
    if (root == NULL) return;
    printInorder(root->left);
    printf("%c ", root->val);
    printInorder(root->right);
    
}
int search(char in[], int strt, int end, char x) {
    int i;
    for(i = strt; i<= end; i++) 
        if (in[i] == x) return i;
    return -1;
}

BinaryTree* buildTree(char in[], char pre[], int inStrt, int inEnd) {
    static int preIndex = 0;

    if (inStrt > inEnd) return NULL;

    BinaryTree* node =  newNode(pre[preIndex++]);

    if (inStrt == inEnd) return node;

    int inIndex = search(in, inStrt, inEnd, node->val);

    node->left = buildTree(in, pre, inStrt, inIndex-1);
    node->right = buildTree(in, pre, inIndex+1, inEnd);
    
    return node;
}
    


int main() {
    char in[] = {'D', 'B', 'E', 'A', 'F', 'C'};
    char pre[] = {'A', 'B', 'D', 'E', 'C', 'F'};
    int len = sizeof(in)/sizeof(in[0]);
    BinaryTree* root = buildTree(in, pre, 0, len-1);
    printInorder(root);
    printf("\n");
    return 0;
}