#!/bin/bash

echo "Jetzt aktualisieren? [J/N]"
read -r aktualisieren

if [ "$aktualisieren" == "J" ] || [ "$aktualisieren" == "j" ]; then
  cd /usr/share || (
    echo "Fehler."
    exit
  )
  sudo rm -r deutsch/
  sudo git clone https://github.com/deutsch-team/deutsch
else
  echo "Aktualisation abgebrochen!"
fi
