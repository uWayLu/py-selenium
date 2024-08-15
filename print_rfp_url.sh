#!/bin/bash
export XDG_CONFIG_HOME=/tmp/.chrome
workdir=$(dirname $(readlink -f $0))
cd $workdir
. ./.venv/bin/activate
python3 print_rfp_url.py "$@"
