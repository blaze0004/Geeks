// Postorder from inorder and preorder


#include<stdio.h>
int search(int arr[], int x,int n) {
    int i;
    for(i = 0; i < n; i++){
        if (arr[i] == x) return i;
    } return -1;
}
void printPostorder(int in[], int pre[], int n) {

    int root = search(in, pre[0], n);

    
    if (root != 0) {
        printPostorder(in, pre+1, root);
    }

    if (root != n-1) {
        printPostorder(in+root+1, pre+root+1, n-root-1);
    }

    printf("%d ", pre[0]);
    

}
int main(int argc, char const *argv[])
{
    int in[] = {4, 2, 5, 1, 3, 6};
    int pre[] = {1, 2, 4, 5, 6, 3};
    int n = sizeof(in)/sizeof(in[0]);
    printPostorder(in, pre, n);
    printf("\n");
    return 0;
}
