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


#include<bits/stdc++.h>
using namespace std;
class Editor {

 
        int n,q;
        vector <string> t;
        string newt, buffer;
        int currentIndex;
    
    public:
        
        int getCurrentIndex();
        void dd();
        void addatm();
        void addim();
        void copyandreplacebuffer();
        void copybufferatcurrentlineend();
        void dy();  
        string getbufferdata();    
        bool isEmptyBuffer();
};

int Editor::getCurrentIndex() {
    /* get the current index */
    return this.currentindex;
}

string Editor::getbufferdata() {
    // to get the data of buffer
    return this.buffer;
}

bool Editor::isEmptyBuffer() {
    // return true if empty buffer
    return buffer.empty();
}

void Editor::dd() {
    /* dd  -- delete the current line and move the cursor
     to the end of next line. If there is no next line, 
     move the cursor to end of the previous line.
     If all the lines are deleted, move the cursor to the
     start of the first line.
    */

   
}



