#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() 
{
    char s[1500] = "0", ts[1500];
    int i;
    while(strlen(s) <= 1000)
    {
        for(i=0;s[i];i++)
            if (s[i] == '1')    ts[i] = '0';
            else                ts[i] = '1';
        ts[i] = '\0';
        strcat(s,ts);
    }
    
    int testCases;
    scanf("%d",&testCases);
    while(testCases--)
    {
        int inputIndexValue;
        scanf("%d",&inputIndexValue);
        printf("%c\n",s[inputIndexValue]);
    }
    return 0;
}
