#!/bin/bash

MODE=$([ ! -z "$1" ] && echo $1 || echo "sql")
SCRIPT_PATH="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ENVPATH=$(echo $SCRIPT_PATH"/.direnv/bin/activate")
API_PATH=$(echo $SCRIPT_PATH"/app/api")

if [[ ! -f $ENVPATH ]]
then
    echo "Creating enviroment"
    python -m venv $SCRIPT_PATH"/.direnv"
fi

echo "Activating enviroment"
source $ENVPATH

pip install -r requirements.txt

echo "Loading: $API_PATH"
cd $API_PATH

python "$API_PATH/data/database/migrate.py"

gunicorn run:app $MODE