// Morris preorder traversal 

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

void MorrisPreorderTraversal(BinaryTree* root) {
    BinaryTree* current = root;

    while(current) {
        if (current->left == NULL) {
            printf("%d ", current->val);
            current = current->right;
        } else {
            BinaryTree* predecessor = current->left;
            while(predecessor->right != NULL && predecessor->right != current) {
                predecessor = predecessor->right;
            }

            if (predecessor->right == NULL) {
                printf("%d ", current->val);
                predecessor->right = current;
                current = current->left;
            } else {
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

    printf("Morris Preorder Traversal is:\n");
    MorrisPreorderTraversal(root);
    
    return 0;
}
