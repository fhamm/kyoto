#!/bin/bash 

INSTALLER_PATH=$(readlink -f $0)
INSTALLER_DIRECTORY=$(dirname "${INSTALLER_PATH}")
MAIN_PATH=$INSTALLER_DIRECTORY/src/main.py

chmod +x src/main.py

ln -s $MAIN_PATH /usr/local/bin/kyoto
