#!/bin/bash
workdir=$(dirname $(readlink -f $0))
default_pdf="print_$(date +'%Y%m%d_%H%M%S').pdf"

cd $workdir
google-chrome --headless --no-sandbox --print-to-pdf="storage/${2:-$default_pdf}" "$1" "${@:3}" \
	--no-pdf-header-footer \
