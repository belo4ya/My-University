# !/bin/bash

username=user$1
password=pass$1

useradd $username 
echo "$username:$password" | chpasswd
