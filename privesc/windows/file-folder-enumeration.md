# windows victim

## list all files including hidden

```cmd
gci -Force
```

## list files matching regex (hide errors)

```cmd
gci -force -recurse -filter regex* -ErrorAction SilentlyContinue
```

## list folders (recursively)

```cmd
dir <file*> /S /B
```

## files for automating windows installations

```cmd
dir /s *sysprep.inf *sysprep.xml *unattended.xml *unattend.xml *unattend.txt 2>nul
```
