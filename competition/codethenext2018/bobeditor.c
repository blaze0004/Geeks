/*

   Bob and Editor

Bob is working on his college project. He tried to make an editor like Vim, but he came up with some messed editor which will follow only following commands :

dd  -- delete the current line and move the cursor to the end of next line. If there is no next line, move the cursor to end of the previous line. If all the lines are deleted, move the cursor to the start of the first line.

:m  -- move the cursor to the end of line m

i m -- each following m lines contain text to insert.

y -- copy the current line and replace the content of the buffer with the copied line.

p -- paste the content of the buffer (the copied line) at the end of the current line and move the cursor to the end of the line. If no line is copied, ignore this command.

dy -- it will work similar to command dd and also copy the deleted line and replace the content of the buffer with the copied line.

You are given some initial text T and Q commands. You are required to print the final text after applying the given commands on T. Initially, the cursor is present at the end of the last line and the buffer is empty.

Input :

The first line of input contains an integer N, number of lines in the initial text T.

Next N lines contain the content of T.

Next line contains Q, denoting the number of commands.

It is followed by Q commands.

Output :

Print the final text T after applying the Q commands.


*/

#include<stdio.h>
#include<stdlib.h>
#include<string.h>

struct node { 
    struct node *next, *prev;
    char t[1100];
};

typedef struct node Node;

char* buffer[1100];

Node* current = NULL;
Node* head = NULL;

Node* createNode(char* text) {
    Node* newnode = (Node*)malloc(sizeof(Node));
    newnode->prev = newnode->next = NULL;
    strcpy(newnode->t, text); 
    return newnode;
}

void deleteNode() {
    if(current == NULL) {
        //free(node);
    } else if (current->next == NULL && current->prev == NULL) {
        current = NULL;
        head = NULL;
    }else if(current->next == NULL) {
        current->prev->next = NULL;
        current = current->prev;
        
    } else {
        current->prev->next = current->next;
        current = current->next;
        
    } 
    //free(node);
    return;
}

void append(char* text) {
    Node* new_node = createNode(text);
    if(current == NULL) {
        current = head = new_node;
        return;
    } else {
        current->next = new_node;
        new_node->prev = current;
        current = new_node;
    }
}

void printText() {
    Node* temp;
    temp = head;
    while(temp) {
        printf("%s", temp->t);
        temp = temp->next;
    }
    
}

void concatListText(char* text) {
    strcat(current->t, text);
}

void setCurrentToLineM(int m) {
    Node* temp = head;
    int i = 0;
    while(temp) {
        if(i == m-1) {
            current = temp;
            return;
        } else {
            temp = temp->next;
            i++;
        }
    }
    return;
}

void AddNewLines(int m) {
    int i = 0;
    string temp;
    for(i = 0; i < m; i++) {
        scanf("%s", &temp);
        if(i == 0) {
            concatListText(temp);
        } else {
            append(temp);
        }
    }
}


void CopyCurrentToBuffer() {
    buffer = current->t;
}

void pasteBufferAtEndOfCurrent() {
    if(buffer == "") {
        return;
    } else {
        concatListText(buffer);
    }
}

void copyAndDelete() {
    buffer = current->t;
    deleteNode();
}
int main() {
    int t, q;
    string ts, qs;
    scanf("%d", &t);
    while(t--) {
        scanf("%s", &ts);
        append(ts);
    }
    scanf("%d", &q);

    while(q--){
        scanf("%s", &qs);
        if(qs == "dd") {
            deleteNode();
        } else if(qs == ":m") {
            setCurrentToLineM();
        }
    }
}


// Driver Function not completed yet