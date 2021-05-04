#!/bin/bash

{
  echo "Jetzt installieren? [J/N]"
  read -r installieren
  if [ "$installieren" == "J" ] || [ "$installieren" == "j" ]; then
    cd /usr/share || (
      echo "Fehler."
      exit
    )
    sudo git clone https://github.com/deutsch-team/deutsch
    cd deutsch || (
      echo "Fehler."
      exit
    )
    sudo chmod +x software/linux/*.sh
    sudo ./software/linux/command.sh
  else
    echo "Installation abgebrochen!"
  fi
} || {
  echo "Git wird benötigt!"
  echo "Jetzt installieren? [J/N]"
  read -r installGit
  if [ $installGit == "J" || $installGit == "j"]; then
    sudo apt-get install git
    echo "Jetzt installieren? [J/N]"
    read -r installieren
    if [ "$installieren" == "J" ] || [ "$installieren" == "j" ]; then
      cd /usr/share || (
        echo "Fehler."
        exit
      )
      sudo git clone https://github.com/deutsch-team/deutsch
      cd Deutsch || (
        echo "Fehler."
        exit
      )
      sudo chmod +x software/linux/*.sh
      sudo ./software/linux/command.sh
    else
      echo "Installation abgebrochen!"
    fi
  fi
}
