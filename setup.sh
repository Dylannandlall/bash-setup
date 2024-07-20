#!/bin/bash
# Author: Dylan Nandlall
#
# Initializes environment to preferred configurations 

mv .bashrc ~/.bashrc
mv .bash_aliases ~/.bash_aliases
mv .bash_profile ~/.bash_profile

sudo apt update && sudo apt upgrade -y
	
sudo apt install vim \
		python3 \
		python3-pip \
		python3-venv \
		python3-pygments \
		git \
		gcc \
		make \
		curl \
		git 
			
mkdir ~/Downloads 2>/dev/null

curl -L "https://code.visualstudio.com/sha/download?build=stable&os=linux-deb-x64" -o vscode.deb
sudo dpkg -i vscode.deb
rm vscode.deb

source ~/.bashrc

