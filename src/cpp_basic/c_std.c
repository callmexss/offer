#include <stdio.h>

char* strcpy(char* dest, const char* src)
{
    if (!src || !dest)
        return NULL;

    char* p = dest;
    while (*src != '\0')
        *dest++ = *src++;
    *dest = '\0';
    
    return p;
}

void* memset(void *dest, int val, size_t len)
{
    unsigned char *ptr = dest;
    while (len-- > 0)
        *ptr++ = val;
    return dest;
}

int main(int argc, const char *argv[])
{
    char s1[] = "hello world";
    char s2[20];
    char* ret;
    strcpy(s2, s1);
    printf("%s\n", s2);

    char src[40];
    char dest[100];

    memset(dest, '\0', sizeof(dest));
    strcpy(src, "This is runoob.com");
    strcpy(dest, src);

    printf("最终的目标字符串： %s\n", dest);

    return 0;
}
