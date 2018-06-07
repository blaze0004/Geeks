// Intro to bst : Insertion and searching 

#include<stdio.h>
#include<malloc.h>

typedef struct bstnode {
    int val;
    struct bstnode *left, *right;
} BST;

BST *newNode(int val) {
    BST *node = (BST*)malloc(sizeof(BST));
    node->val = val;
    node->left = node->right = NULL;
    return node;
}

BST *insert(BST *node, int val) {
    if (node == NULL) return newNode(val);

    if (val < node->val) node->left = insert(node->left, val);
    else node->right = insert(node->right, val);

    return node;
}

BST *search(BST *node, int key) {
    if (node == NULL && node->val == key) return node;

    if (key < node->val) return search(node->left, key);
    else return search(node->right, key);
} 

void inorder(BST *node) {
    if (node == NULL) return;

    inorder(node->left);
    printf("%d ", node->val);
    inorder(node->right);

}

int main()
{
    /* Let us create following BST
              50
           /     \
          30      70
         /  \    /  \
       20   40  60   80 */
    BST *root = NULL;
    root = insert(root, 50);
    insert(root, 30);
    insert(root, 20);
    insert(root, 40);
    insert(root, 70);
    insert(root, 60);
    insert(root, 80);
  
    // print inoder traversal of the BST
    inorder(root);
    printf("\n");
    return 0;
}
