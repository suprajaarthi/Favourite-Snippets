#include<stdio.h>
#include <stdlib.h>
void swap(char *x,char *y)
{
    char temp;
    temp=*x;
    *x=*y;
    *y=temp;
}
int permute(char *a,int l,int n)
{
    int i;
    if (l==n)
    {
        printf("%s\n",a);
    }
    else{
        for(i=l;i<=n;i++)
        {
            swap((a+l),(a+i));
            permute(a,l+1,n);
            swap((a+l),(a+i));
        }
    }
}
int main()
{
    char s[1001];
    scanf("%s",s);
    int n=strlen(s);
    permute(s,0,n-1);
    return 0;
}
