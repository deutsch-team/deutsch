#!/bin/bash

echo "Jetzt entfernen? [J/N]"
read -r entfernen
if [ "$entfernen" == "J" ] || [ "$entfernen" == "j" ]; then
  cd /usr/share/ || (
    echo "Fehler."
    exit
  )
  sudo rm -r Deutsch/
else
  echo "Entfernen abgebrochen!"
fi
