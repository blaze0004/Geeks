// check if given preorder inorder and postorder traversal are of same treee

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

int search(int in[], int strt, int end, int x) {
    int i;
    for(i = strt; i <= end; i++) {
        if (in[i] == x) return i;
    }
    return -1;
}

BinaryTree* buildTree(int in[], int pre[], int inStart, int inEnd) {

    static int preIndex = 0;

    if (inStart > inEnd) return NULL;

    BinaryTree* node = newNode(pre[preIndex++]);

    if (inStart == inEnd) return node;

    int inIndex = search(in, inStart, inEnd, node->val);

    node->left = buildTree(in, pre, inStart, inIndex-1);
    node->right = buildTree(in, pre, inIndex+1, inEnd);
    return node;
}
int checkPostOrder(BinaryTree* node, int postorder[], int index) {

    if (node == NULL) return index;

    index =  checkPostOrder(node->left, postorder, index);
    index = checkPostOrder(node->right, postorder, index);

    if (node->val = postorder[index]) index++;
    else return -1; 
    return index;
}

int main()
{
    int inOrder[] = {4, 2, 5, 1, 3};
    int preOrder[] = {1, 2, 4, 5, 3};
    int postOrder[] = {4, 5, 2, 3, 1};
 
    int len = sizeof(inOrder)/sizeof(inOrder[0]);
 
    // build tree from given 
    // Inorder and Preorder traversals
    BinaryTree *root = buildTree(inOrder, preOrder, 0, len - 1);
 
    // compare postorder traversal on constructed
    // tree with given Postorder traversal
    int index = checkPostOrder(root,postOrder,0);
 
    // If both postorder traversals are same 
    if (index == len)
        printf("YES\n");
    else
        printf("No\n");
 
    return 0;
}