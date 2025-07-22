#include <unistd.h>
#include <stdio.h>
#include <fcntl.h>

int main()
{
    char buffer[50];
    unsigned int i;
    int fd;

    printf("Welcome to Text Editor\n");

    i = 0;
    while(i < 50)
        buffer[i++] = 0;
    
    read(0, buffer, 49);
    fd = open("testfile_c.txt", O_WRONLY|O_APPEND);
    write(fd, buffer, 50);
    write(fd, "\n", 1);
    close(fd);
    return (0);
}
