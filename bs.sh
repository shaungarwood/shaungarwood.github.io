#!/bin/bash

cat << "EOF"

 _                 _       _
| |__   ___   ___ | |_ ___| |_ _ __ __ _ _ __  ___
| '_ \ / _ \ / _ \| __/ __| __| '__/ _` | '_ \/ __|
| |_) | (_) | (_) | |_\__ \ |_| | | (_| | |_) \__ \
|_.__/ \___/ \___/ \__|___/\__|_|  \__,_| .__/|___/
                                        |_|

      []
   []__(_____  <|
    (____ / <| <|
    (___ /  <| L`-------.
    (__ /   L`--------.  \
    /  `.    ^^^^^ |   \  |
   |     \---------'    |/
   |______|____________/]
   [_____|`-.__________]


EOF

# stole this from: https://unix.stackexchange.com/a/6348
if [ -f /etc/os-release ]; then
    # freedesktop.org and systemd
    . /etc/os-release
    OS=$NAME
    VER=$VERSION_ID
elif type lsb_release >/dev/null 2>&1; then
    # linuxbase.org
    OS=$(lsb_release -si)
    VER=$(lsb_release -sr)
elif [ -f /etc/lsb-release ]; then
    # For some versions of Debian/Ubuntu without lsb_release command
    . /etc/lsb-release
    OS=$DISTRIB_ID
    VER=$DISTRIB_RELEASE
elif [ -f /etc/debian_version ]; then
    # Older Debian/Ubuntu/etc.
    OS=Debian
    VER=$(cat /etc/debian_version)
elif [ -f /etc/SuSe-release ]; then
    # Older SuSE/etc.
    ...
elif [ -f /etc/redhat-release ]; then
    # Older Red Hat, CentOS, etc.
    ...
else
    # Fall back to uname, e.g. "Linux <version>", also works for BSD, etc.
    OS=$(uname -s)
    VER=$(uname -r)
fi

echo "-----------------------------"
echo "OS appears to be: $OS"
echo "Version: $VER"
echo "-----------------------------"
echo
echo

# install ansible and git
if [ "$OS" == "Ubuntu" ] || [ "$OS" == "Debian" ]; then
    echo "this is debian flavor machine"
    echo

    sudo apt-get -y install software-properties-common
    sudo apt-add-repository -y ppa:ansible/ansible
    sudo apt-get update
    sudo apt-get -y install git ansible
elif [[ "$OS" == CentOS* ]]; then
    echo "this is centos machine"
    echo
    sudo yum install -y epel-release
    sudo yum install -y git ansible
else
    echo "not sure what flavor this machine is"
    echo "exiting"
    exit 1
fi

# if this script is standalone, will still need to checkout repo
if [[ ! -d ~/my_bootstraps ]]; then
    git clone --depth 1 --branch master https://github.com/shaungarwood/my_bootstraps.git ~/my_bootstraps
else
    git pull ~/my_bootstraps/
fi

# install needed galaxy roles
ansible-galaxy install -r ~/my_bootstraps/requirements.yml
