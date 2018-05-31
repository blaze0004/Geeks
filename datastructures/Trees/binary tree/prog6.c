// Morris PostOrder Traversal (Wrong Implementation)

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

void MorrisPostOrderTraversal(BinaryTree* root) {
    BinaryTree* current = root;
    while (current) {
        if (current->left == NULL) {
            current = current->right;
        } else {
            BinaryTree* predecessor = current->left;
            while(predecessor->right && predecessor->right != current) {
                predecessor = predecessor->right;
            }

            if (predecessor->right == NULL) {
                predecessor->right = current;
                current = current->left;
            } else {
                printf("%d ", predecessor->val);
                predecessor->right = NULL;
                current = current->right;
            }
        }
    }
    printf("\n");
}


int main(int argc, char const *argv[])
{
    BinaryTree* root    = newNode(1);
    root->left          = newNode(2);
    root->right         = newNode(3);
    root->left->left    = newNode(4);
    root->left->right   = newNode(5);

    printf("Inorder is:\n");
    MorrisPostOrderTraversal(root);
    
    return 0;
}
