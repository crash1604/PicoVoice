// @file:- istack.c
// @author:- Chanakya Sharma
// @description:-
//              Stack implementation with following requirements
//                  - Should allow storing any data type (simple and complex)
//                  - Should have all the DS functions
// @bugs:-
//              - User must define the identificationCode
//                  - Additional functions can be used for the same
//              - Stacks can hold more than more than one data type 
//                  hence ID codes are needed to keep track of what is on the stack
// @compilation and runtime:-
//          No MakeFile provided as it is a smaller segment of code
//          MakeFile can be submitted upon request 
//              -in linux use ``` g++ istack ``` 
//              -in macOS use ``` clang istack ```
//                   then use ```./a.out```
// This program was written on Apple M1 ARM architecture and has not been used on x86 architectures for testing


// Answer to Problem questions
/*
// Q3 [C] Design and implement a stack class (i.e. struct with accompanying functions).
// The interface should allow storing any data type including complex structures.
//  Describe different implementation strategies and compare their pros and cons.
//  What is the best approach in an embedded real-time system?
//  What is the best approach when memory resources are very limited?
//  You can use “malloc” and “free” functions.

Q1. Describe different implementation strategies and compare their pros and cons.
Ans. i.) It can be implemented by using void pointers with data type codes
            pros:
                a. It is Simple implementation and no complexity change
                b. Stores data references and actual data is stored some place else
            cons:
                a. need to be wary of segmentation faults
                b. without ID codes cannot identify what data is stored where
     ii.) Use templates with struct data types
            pros:
                a. It produces clean templated code which is code structure is organised
                b. Generic functions with the help of Macros
            cons:
                a. High margin for error
                    e.g. printing an array with templated functions
                            handling pointers
                b. Complex concept
                c. extensive use of macros and hence more runtime
    
Q2. What is the best approach in an embedded real-time system?
Ans. In a real time system we would like everything to be coupled as loosly coupled to 
     avoid runtime failures. High function cohesion will make the workflow as smooth as possible.
     Need to control everything manually as there are memory constraints to be satisfied
     and specific behaviors that need to be controlled or monitored.
     Hence the best approach with real-time system is sign the data and use it with pointers.

Q3. What is the best approach when memory resources are very limited?
Ans. With limited resources use the monolithic kernal with shared space but the tradeoff would be
     a lot of pointers in different places. but would still need efficient space complexity algorithms
     along with structs as they are simple and gets the job done.
     Also, structs have lower overhead than templates
*/


// HEADER FILES
#include <stdio.h>
#include <stdlib.h>
 
// Data structure to represent a stack
struct Stack {
    void* data;
    int identificationCode;
    struct Stack* next;
};
//End of Data Structure

//Helper function to test data types
// Not a univeral function
void PrintArray(int *a){
    for ( int i=0;i<5;i++){
        printf( "%d ", a[i] );
    }
    printf( "\n" );
}
//end of helper function
//////////////////////////////////////////////
// STACK FUNCTIONS
//////////////////////////////////////////////
// Description:-
        // Stack Node Initializer
        // Allocates node sizes
        // returns node
struct Stack* newNode(void* data, int code)
{
    struct Stack* node =
      (struct Stack*)
      malloc(sizeof(struct Stack));
    node->data = data;
    node->identificationCode=code;
    node->next = NULL;
    return node;
}
// Description:-
        // Checks if the stack is Empty
int isEmpty(struct Stack* root)
{
    return !root;
}
// Description:-
        // Takes the void pointer and stores the address in data with init function
        // allocates DataType identification Code with init
        // changes the node positions
        // puts the new node on top
void push(struct Stack** root, void* data, int code)
{
    struct Stack* node = newNode(data, code);
    node->next = *root;
    *root = node;
    printf("push successful\n");
}
 
// Description:-
        // returns address stored in the void pointer
        // restructures the stack
        // Frees the memory
void *pop(struct Stack** root)
{
    if (isEmpty(*root)){
        printf("DataType code is NULL\nStack Empty");
        return NULL;
    }
    struct Stack* temp = *root;
    *root = (*root)->next;
    void * popped = temp->data;
    printf("\nDataType code is %d\n\n",temp->identificationCode);
    free(temp);
    return popped;
}
// Description:-
        // returns void pointer to data 
        // prints the ID code 
        // Does not remove the item from stack
void* peek(struct Stack* root)
{
    if (isEmpty(root))
        return NULL;
    printf("\nDataType code is %d\n\n",root->identificationCode);
    return root->data;
}

int codeCheck(struct Stack* root){
    if (isEmpty(root))
        return -1;//code -1 for empty stack
    printf("\nDataType code is %d\n\n",root->identificationCode);
    return root->identificationCode;
}
//////////////////////////////////////////////
// END OF STACK FUNCTIONS
//////////////////////////////////////////////

// Main function for minor testing
int main()
{
    struct Stack* root = NULL;
    int x = 20; //IDcode 1
    char y = 'g'; //IDcode 2
    float z = 2.2; //IDcode 3
    push(&root, &x,1);
    push(&root, &y,2);
    push(&root, &z,3);
    
    float *a = pop(&root);
    printf("%f popped from stack\n", *a );
 
    char *b = peek(root);
    printf("Top element is %c\n", *b);

    int arr[5] = {1,2,3,4,5};// IDCode 4
    push(&root, &arr, 4);
    PrintArray(peek(root));

    printf("top has the id code %d\n",codeCheck(root));
 
    return 0;
}
// End of Program