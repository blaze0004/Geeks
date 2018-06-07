// Deletion in a BST

#include<stdio.h>
#include<malloc.h>

#define and &&
#define or ||

typedef struct bstnode {
    int val;
    struct bstnode *left, *right;
} BST;

BST *newNode(int val) {
    BST* node = (BST*)malloc(sizeof(BST));
    node->val = val;
    node->left = node->right = NULL;
    return node;
}

BST *insert(BST* node, int key) {
    if (node == NULL) return newNode(key);

    if (key < node->val) node->left = insert(node->left, key);
    if (key > node->val) node->right = insert(node->right, key);

    return node;
}

BST *search(BST *node, int key) {
    if (node == NULL and node->val == key) return node;

    if (key < node->val) return search(node->left, key);
    if (key > node->val) return search(node->right, key);
}

BST* minVal(BST *node) {
    BST* current = node;
    
    while(current->left != NULL) {
        current = current->left;
    } 
    return current;
} 
BST *deleteNode(BST *node, int key) {
    if (node == NULL) return node;

    if (key < node->val) node->left = deleteNode(node->left, key);

    else if (key > node->val) node->right = deleteNode(node->right, key);

    else {
        if (node->left == NULL) {
            BST *temp = node->right;
            free(node);
            return temp;
        } else if (node->right == NULL) {
            BST *temp = node->left;
            free(node);
            return temp;
        } 

        BST *temp = minVal(node->right);
        node->val = temp->val;
        node->right = deleteNode(node->right, temp->val);
    }

    return node;
}

void inorder(BST *root) {
   if (root != NULL)
    {
        inorder(root->left);
        printf("%d ", root->val);
        inorder(root->right);
    }
}
// Driver Program to test above functions
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
    root = insert(root, 30);
    root = insert(root, 20);
    root = insert(root, 40);
    root = insert(root, 70);
    root = insert(root, 60);
    root = insert(root, 80);
 
    printf("Inorder traversal of the given tree \n");
    inorder(root);
 
    printf("\nDelete 20\n");
    root = deleteNode(root, 20);
    printf("Inorder traversal of the modified tree \n");
    inorder(root);
 
    printf("\nDelete 30\n");
    root = deleteNode(root, 30);
    printf("Inorder traversal of the modified tree \n");
    inorder(root);
 
    printf("\nDelete 50\n");
    root = deleteNode(root, 50);
    printf("Inorder traversal of the modified tree \n");
    inorder(root);
    printf("\n");
    
    return 0;
}