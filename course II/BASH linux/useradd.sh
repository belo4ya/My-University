# !/bin/bash

username=$1
password=$2

useradd -N -M $username 
echo "$username:$password" | chpasswd
