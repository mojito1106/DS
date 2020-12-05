#include <stdio.h>
char s[50];
int top = -1;
void push(char);
char pop();

int main()
{
    int i = 0;
    char a[10] = "(())()))";
    for(int i = 0; i<10;i++)
    {
        if(a[i] == '\0') break;
        printf("%d\n", i);
        if(a[i] == '(') push(a[i]);
        else
        {
            if(top == -1) {
                printf("failed\n");
                return -1;
            }
            pop();
        }
    }
    if(top != -1) return -1;
    else {
        printf("successful");
        return 0;
    }
        
    
    
}
void push(char x)
{
    if(top == 49) printf("s is full") ;
    else
    {
        top = top+1;
        s[top] = x;
    }
    
    
}
char pop()
{
    if(top == -1) printf("s is empty");
    else
    {
        char y = s[top];
        top = top-1;
        return y;
    }
}
