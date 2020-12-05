/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <stdio.h>
#include <stdlib.h>
#define MAXSTACK 5
//int s[MAXSTACK];
int top = -1;
//int isEmpty();
//int pop();
//void push(int);

int main()
{
    int x[MAXSTACK] = {1,2,3,4,5};
    int item;
    top = 4;
    while(top!=-1)
    {
        printf("堆疊彈出順序:%d\n",x[top]);
        top = top-1;
    }
    while(top<MAXSTACK)
    {
        
        scanf("%d",&item);
        top = top+1;
        x[top] = item;
    }
    printf("陣列已滿：%d",*x);//x是陣列的指標，指到第一個元素
       
    return 0;
}
