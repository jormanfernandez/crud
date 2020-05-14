#!/bin/bash

SCRIPT_PATH="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ENVPATH=$(echo $SCRIPT_PATH"/.direnv/bin/activate")
CLIENT_PATH=$(echo $SCRIPT_PATH"/app/client")

if [[ ! -f $ENVPATH ]]
then
   echo "Creating enviroment"
   python -m venv $SCRIPT_PATH"/.direnv"
fi

echo "Activating enviroment"
source $ENVPATH

echo "Loading: $CLIENT_PATH"
cd $CLIENT_PATH

python run.py