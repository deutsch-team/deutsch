#!/bin/bash

function deutsch-installer() {
  cd /usr/share/deutsch/software/linux || (
    echo "Fehler."
    exit
  )
  if [ "$1" == "install" ]; then
    sudo ./install.sh
  elif [ "$1" == "update" ]; then
    sudo ./update.sh
  elif [ "$1" == "remove" ]; then
    sudo ./remove.sh
  fi
}
