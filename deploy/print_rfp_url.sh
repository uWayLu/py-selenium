#!/bin/bash
workdir=$(dirname $(readlink -f $0))
cd $workdir
python3 print_rfp_url.py "$1" "$workdir/storage/${2:-.}" "${@:3}"