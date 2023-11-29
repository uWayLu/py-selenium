#!/bin/bash
workdir=$(dirname $0)
. "$workdir/.venv/bin/activate"
python3 print_rfp_url.py "$@"
