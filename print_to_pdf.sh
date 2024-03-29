#!/bin/bash
workdir=$(dirname $(readlink -f $0))
cd $workdir
. ./.venv/bin/activate
chrome --headless --no-sandbox --print-to-pdf="$2" "$1" "${@:3}" \
	--no-pdf-header-footer \

