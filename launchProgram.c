// Program to compile and execute a c program

#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#define MAX_COMMAND_SIZE 500
char commandString[MAX_COMMAND_SIZE];
int main(int argc, char const *argv[])
{
    char objectFolder[] = "~/gcc/";

    char *fileName = (char *)malloc(sizeof(argv[1]));
    strcpy(fileName, argv[1]);
    char *objectFileName = (char *)malloc(sizeof(fileName));
    strncpy(objectFileName, fileName, strlen(fileName)-2);
    
    strcat(commandString, "g++ ");
    strcat(commandString, fileName);
    strcat(commandString, " -o ");
    strcat(commandString, objectFolder);
    strcat(commandString, objectFileName);
    strcat(commandString, " && chmod 755 ");
    strcat(commandString, objectFolder);
    strcat(commandString, objectFileName);
    strcat(commandString, " && ./");
    strcat(commandString, objectFolder);
    strcat(commandString, objectFileName);
    system(commandString);
    return 0;
}
