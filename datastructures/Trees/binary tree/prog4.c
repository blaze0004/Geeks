// Morris Inorder traversal 

#include<stdio.h>
#include<malloc.h>

typedef struct btnode {
    int val;
    struct btnode *left, *right;
} BinaryTree;

BinaryTree* newNode(int val) {
    BinaryTree* newnode = (BinaryTree*)malloc(sizeof(BinaryTree));
    newnode->val = val;
    newnode->left = newnode->right = NULL;
    return newnode;
}

void MorrisInorderTraversal(BinaryTree* root) {
    BinaryTree* current = root;
    while(current) {
        if (current->left == NULL) {
            printf("%d ", current->val);
            current = current->right;
        } else {
            BinaryTree* predecessor = current->left;

            while(predecessor->right != current && predecessor->right != NULL) {
                predecessor = predecessor->right;
            }

            if (predecessor->right == NULL) {
                predecessor->right = current;
                current = current->left;
            } else {
                predecessor->right = NULL;
                printf("%d ", current->val);
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
    MorrisInorderTraversal(root);
    
    return 0;
}
